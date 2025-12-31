from datetime import datetime as DT
from pyrogram import Client
import asyncio
import sys
import os

from start_threading import start_thread

try:
    with open('groups.txt', 'r') as file:
        needs_groups = file.read().split('\n')
        async def main():
            if os.path.exists("Session.session"):
                client = Client('Session')
            else:
                API_ID = input("На сайте https://my.telegram.org/apps получите API_ID #: ")
                API_HASH = input("На сайте https://my.telegram.org/apps получите API_HASH #: ")
                client = Client('Session', int(API_ID), API_HASH)

            print(f'Приложение Стартовало: {str(DT.now()).split(".")[0]}')

            async with client:
                print("Запускаю обработчик сообщений для всех целевых чатов...")
                await start_thread(client, needs_groups)

        # Запускаем основную функцию асинхронно
        if __name__ == "__main__":
            asyncio.run(main())
except Exception as a:
    print(a)
    input('\nНажмите ENTER Для Завершения...')