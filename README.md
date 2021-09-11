[![Run Tests](https://github.com/PerchunPak/sunshinedsbot/actions/workflows/actions.yml/badge.svg?branch=main)](https://github.com/PerchunPak/sunshinedsbot/actions/workflows/actions.yml)

# Sunshine Discord Bot

Наш дискорд бот, полностью переведен на русский
Мой первый проект, поэтому может содержать много ошибок

## Установка

1. **Установите Python 3.6 или выше**

Это нужно для запуска бота

2. **Клонируйте репозиторий**

3. **Настроить виртуальную среду**

Используйте `python3 -m venv .`

4. **Закончив установку виртуальной среды, устанавливаем зависимости**

Используйте `python3 -m pip install -U -r requirements.txt`

5. **Создайте базу данных в формате PostGreSQL**

## Хостинг в Docker

1. **Клонируйте репозиторий**
2. **Измените и переименуйте `config.py.example`.**
Используйте `docker-compose up`
Вам нужна будет версия 9.5 или выше. База данных будет хранить количество "ладно" слов для каждого пользователя. Централизованной базы данных нет.

6. **Настройте конфигурацию**

В корневом каталоге есть файл под названием `config.py`, который содержит две переменные, необходимые для запуска бота. Один из них - `TOKEN`, который представляет собой строку, содержащую токен бота Discord. Другой переменной является `POSTGRES`, которая представляет собой строку, содержащую DSN для базы данных Postgres, созданной на шаге 5.

> Взято и переведено с https://github.com/NWordCounter/bot

---

**Важная Заметка**: Вам нужно включить привилегию `SERVER MEMBERS` для работы бота. [Следуйте этим инструкциям.](https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents)

**Важная Заметка 2**: Нет, я не собираюсь выпускать "ладно" считатель отдельным ботом, так как к нему не будет никакого интереса.

## Большое спасибо

"ладно" counter it is forked from https://github.com/NWordCounter/bot

Большое спасибо [WINGS07](https://github.com/WINGS07), [Nikita244](https://github.com/Nikita244) и особенное спасибо моему брату [JeffyOLOLO](https://github.com/JeffyOLOLO) за большую помощь в программировании (да, я не знаю ни единого языка программирования)

[<img alt="Deployed with FTP Deploy Action" src="https://img.shields.io/badge/Deployed With-FTP DEPLOY ACTION-%3CCOLOR%3E?style=for-the-badge&color=2b9348">](https://github.com/SamKirkland/FTP-Deploy-Action)
