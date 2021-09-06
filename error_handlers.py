"""
"ладно" считатель - Простой в использовании бот Discord, который считает, сколько раз каждый пользователь сказал ладно
Написано в 2019 by NinjaSnail1080 (Дискорд: @NinjaSnail1080#8581), улучшено и переведено Perchun_Pak
"""

from discord.ext.commands import Cog, NotOwner, NoPrivateMessage, BadArgument
from discord import Forbidden, NotFound


class ErrorHandlers(Cog):
    """Плейсхолдеры ошибок"""

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx, exception):
        exc = exception
        if isinstance(exc, NotOwner):
            return await ctx.send(f"Только мой Владелец, {self.bot.app_info.owner}, может использовать эту команду")

        elif isinstance(exc, NoPrivateMessage):
            return

        elif isinstance(exc, BadArgument):
            return

        elif isinstance(exc, Forbidden):
            return

        elif isinstance(exc, NotFound):
            return

        elif "Missing Permissions" in str(exc):
            return await ctx.send("У меня нет необходимых прав для выполнения этой команды. "
                                  "Предоставление мне разрешения администратора должно решить эту проблему")

        else:
            return await ctx.send(
                f"```Команда: {ctx.command.qualified_name}\n{exc}```Неизвестная ошибка "
                "произошла и я не смог выполнить эту команду. Простите!")


def setup(bot):
    bot.add_cog(Error_Handlers(bot))
