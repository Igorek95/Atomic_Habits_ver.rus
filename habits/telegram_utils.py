import asyncio

from aiogram import Bot

from config import settings


async def send_notification(chat_id, text):
    bot_token = settings.bot_token
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text)
