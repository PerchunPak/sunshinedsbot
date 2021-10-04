[![Run Tests](https://github.com/PerchunPak/sunshinedsbot/actions/workflows/actions.yml/badge.svg?branch=main)](https://github.com/PerchunPak/sunshinedsbot/actions/workflows/actions.yml)

# Sunshine Discord Bot

Наш дискорд бот, полностью переведен на русский
Мой первый проект, поэтому может содержать много ошибок

## Установка

1. **Установите [Python 3.6 или выше](https://www.python.org/downloads)**

Рекомендовано [Python 3.9](https://www.python.org/downloads/release/python-397), именно на нем тестируется бот.

2. **Клонируйте репозиторий**

Используйте `git clone https://github.com/PerchunPak/PingerBot.git` и `cd PingerBot`

3. **Установите зависимости**

Используйте `pip install -Ur requirements.txt`

4. **Создайте базу данных в формате PostGreSQL**

Вам нужна будет версия 9.5 или выше. База данных будет хранить пинги и добавленные сервера. Централизованной базы данных нет.

5. **Настройте Конфигурацию.**

В корневом каталоге есть файл под названием `config.py`, который содержит две переменные, необходимые для запуска бота. Один из них - `TOKEN`, который представляет собой строку, содержащую токен бота Discord. Другой переменной является `POSTGRES`, которая представляет собой строку, содержащую параметры подключения для базы данных Postgres, созданной на шаге 4.

## Хостинг через Docker

1. **Повторите все шаги выше.**

2. **Используйте `docker-compose up`**

---

**Важная Заметка**: Вам нужно включить привилегию `SERVER MEMBERS` для работы бота. [Следуйте этим инструкциям.](https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents)

**Важная Заметка 2**: Нет, я не собираюсь выпускать "ладно" считатель отдельным ботом, так как к нему не будет никакого интереса.

## Большое спасибо

"ладно" counter it is forked from https://github.com/NWordCounter/bot

Большое спасибо [WINGS07](https://github.com/WINGS07), [Nikita244](https://github.com/Nikita244) и особенное спасибо моему брату [JeffyOLOLO](https://github.com/JeffyOLOLO) за большую помощь в программировании (да, я не знаю ни единого языка программирования)

[<img alt="Deployed with FTP Deploy Action" src="https://img.shields.io/badge/Deployed With-FTP DEPLOY ACTION-%3CCOLOR%3E?style=for-the-badge&color=2b9348">](https://github.com/SamKirkland/FTP-Deploy-Action)
