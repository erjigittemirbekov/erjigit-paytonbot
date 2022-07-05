import asyncio

from aiogram import types
from aiogram.utils import executor
from decouple import config

from config import dp, bot, URL
import logging
from handlers import callback, client, fsmAdminMenu, echo,notification
from database.bot_db import sql_create


async def on_startup(_):
    await bot.set_webhook(URL)
    asyncio.create_task(notification.shceduler())
    sql_create()
    print("Создан!")

async def on_shutown(dp):
    await bot.delete_webhook()


client.register_handlers_client(dp)
callback.register_handler_callback(dp)
fsmAdminMenu.register_fsmadmin_handler(dp)
notification.register_handler_notification(dp)

echo.register_echo_message(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_webhook(dispatcher=dp,
                           webhook_path="",
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutown,
                           host="0.0.0.0",
                           port=config("PORT", cast=int)
                        )