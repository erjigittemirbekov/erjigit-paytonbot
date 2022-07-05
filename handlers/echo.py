import random
from aiogram import types, Dispatcher
from config import bot, dp, ADMIN


# noinspection PyPackageRequirements
async def echo(message: types.Message):
    if message.from_user.id == ADMIN:
        games = ['🎲', '🏏', '⚽']
        # value = random.choice(games)
        if message.text.startswith('game'):
            await bot.send_message(message.chat.id, random.choice(games))
        if message.text.startswith('pin'):
            await bot.pin_chat_message(message.chat.id, message.message_id)
        await bot.send_message(message.from_user.id, message.text)
        a = int(message.text)
        if a:
            await bot.send_message(message.from_user.id, a ** 2)
    else:
        await bot.send_message(message.chat.id, "Вы не Админ!")


def register_echo_message(dp: Dispatcher):
    dp.register_message_handler(echo)