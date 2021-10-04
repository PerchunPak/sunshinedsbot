"""
"ладно" считатель - Простой в использовании бот Discord, который считает, сколько раз каждый пользователь сказал ладно
Написано в 2019 by NinjaSnail1080 (Дискорд: @NinjaSnail1080#8581), улучшено и переведено Perchun_Pak
Dockerized by Kogeki
"""

from discord.ext.commands import Bot, is_owner, when_mentioned
from discord.ext.tasks import loop
from discord import Intents, Status, Activity, ActivityType, Client
from datetime import datetime
from re import finditer, IGNORECASE
from asyncpg import create_pool as pg_create_pool

from config import TOKEN, POSTGRES  # Не забывайте что вам нужно указать свои данные в config.py

bot_intents = Intents.default()
bot_intents.members = True

bot = Bot(
    command_prefix=when_mentioned,
    description="ладно считатель",
    case_insensitive=True,
    help_command=None,
    status=Status.invisible,
    intents=bot_intents,
    fetch_offline_members=True
)

bot.ready_for_commands = False
bot.load_extension("commands")
bot.load_extension("error_handlers")


async def create_pool():
    """Создает таблицы в бд, если они уже есть - загружает их"""

    bot.pool = await pg_create_pool(POSTGRES)
    async with bot.pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS lwords (
                id BIGINT PRIMARY KEY,
                total BIGINT NOT NULL DEFAULT 0
            )
        ;""")

        await conn.execute("""
                INSERT INTO lwords
                (id)
                VALUES (0)
                ON CONFLICT (id)
                    DO NOTHING
            ;""")

        query = await conn.fetch("SELECT * FROM lwords;")

    bot.lwords = {}
    for i in query:
        bot.lwords.update({i.get("id"): dict(i)})


@bot.event
async def on_connect():
    print("\nУстановлено соединение с дискордом")


@bot.event
async def on_ready():
    await create_pool()

    print('\nЗашел как:\n'
          f'{bot.user}\n'
          f'{bot.user.id}\n'
          '-----------------\n'
          f'{datetime.now().strftime("%X %d.%m.%Y")}\n'
          '-----------------\n'
          f'Шардов: {str(bot.shard_count)}\n'
          f'Серверов: {str(len(bot.guilds))}\n'
          f'Пользователей: {str(len(bot.users))}\n'
          '-----------------')

    update_db.start()
    bot.ready_for_commands = True
    bot.started_at = datetime.utcnow()
    bot.app_info = await bot.application_info()

    await bot.change_presence(status=Status.online, activity=Activity(
        name='кто сколько раз сказал "ладно"', type=ActivityType.competing))


@bot.event
async def on_message(message):
    if not bot.ready_for_commands or message.author.bot:
        return

    if message.guild is not None:
        for m in finditer(r"\b(ладно)(s\b|\b)", message.content, IGNORECASE):
            if message.author.id not in bot.lwords:
                bot.lwords.update(
                    {message.author.id: {"total": 0, "id": message.author.id}})
            bot.lwords[message.author.id]["total"] += 1
            bot.lwords[0]["total"] += 1

    ctx = await bot.get_context(message)
    if ctx.valid:
        await bot.invoke(ctx)
    else:
        if bot.user in message.mentions and len(message.mentions) == 2:
            await message.channel.send(f"Вам нужно написать `@{bot.user} count <user>` чтобы "
                                       f"получить статистику другого пользователя.\nИспользуйте"
                                       "`@{bot.user} help` для помощи с другими командами")
        elif bot.user in message.mentions:
            await message.channel.send(f"Используйте `@{bot.user} help` для списка моих команд")


@bot.event
async def on_message_delete(message):
    if not bot.ready_for_commands or message.author.bot:
        return

    if message.guild is not None:
        for m in finditer(r"\b(ладно)(s\b|\b)", message.content, IGNORECASE):
            if message.author.id not in bot.lwords:
                bot.lwords.update(
                    {message.author.id: {"total": 0, "id": message.author.id}})
            bot.lwords[message.author.id]["total"] -= 1
            bot.lwords[0]["total"] -= 1

    ctx = await bot.get_context(message)
    if ctx.valid:
        await bot.invoke(ctx)


@loop(minutes=5, loop=bot.loop)
async def update_db():
    """Обновляет ДБ каждые 5 минут"""

    async with bot.pool.acquire() as conn:
        await conn.execute("""
            INSERT INTO lwords
            (id)
            VALUES {}
            ON CONFLICT
                DO NOTHING
        ;""".format(", ".join([f"({u})" for u in bot.lwords])))

        for data in bot.lwords.copy().values():
            await conn.execute("""
                UPDATE lwords
                SET total = {}
                WHERE id = {}
            ;""".format(data["total"], data["id"]))


@bot.command(hidden=True)
@is_owner()
async def reload(ctx):
    """Перезагружает некоторые файлы бота"""

    bot.reload_extension("commands")
    bot.reload_extension("error_handlers")
    await ctx.send("Файлы перезагружены")


@bot.command(hidden=True)
@is_owner()
async def restartdb(ctx):
    await create_pool()
    await ctx.send("ДБ перезагружена")


@bot.command(hidden=True)
@is_owner()
async def restartudb(ctx):
    update_db.cancel()
    update_db.start()
    await ctx.send("Отменено и запущено `update_db`")


try:
    bot.loop.run_until_complete(bot.start(TOKEN))
except KeyboardInterrupt:
    print("\nЗакрытие")
    bot.loop.run_until_complete(bot.change_presence(status=Status.invisible))
    for e in bot.extensions.copy():
        bot.unload_extension(e)
    print("Выходим")
    bot.loop.run_until_complete(Client.close(bot))
finally:
    update_db.cancel()
    print("Закрыто")
