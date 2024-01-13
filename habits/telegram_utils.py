import asyncio
from aiogram import Bot

from config import settings

async def send_notification(chat_id, text):
    bot_token = settings.bot_token
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text)

# Пример использования
async def on_startup(dp):
    chat_id = "1391984681"  # Замените на реальный идентификатор чата
    text = "Ваше тестовое уведомление"
    await send_notification(chat_id, text)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # Запускаем loop в on_startup, чтобы убедиться, что он работает
    loop.run_until_complete(on_startup(None))
