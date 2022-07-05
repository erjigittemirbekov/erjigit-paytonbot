import random
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot, dp, ADMIN
from prosto_parser import serials, multiki, anime
from database import psql_db

async def start_comand(message: types.Message):

    user_id = message.from_user.id
    username = f"@{message.from_user.username}"
    fullname = message.from_user.full_name

    psql_db.cursor.execute(
        "INSERT INTO users (id. username, fullname) VALUES (%s, %s, %s)",
    )
    psql_db.db.commit()

    await message.reply(f'Hello {message.from_user.full_name} 😂')

async def mem_comand(message: types.Message):
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next->', callback_data='button_call_1')
    markup.add(button_call_1)
    question = 'Кто такой лев'
    answer = [
        'Лох', 'Бабник', 'Царь зверей', 'Бегун'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Изи',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def question(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton('Да',
                                         callback_data='button_call_4')
    button_call_5 = InlineKeyboardButton('Нет',
                                         callback_data='button_call_5')
    markup.add(button_call_4, button_call_5)
    await bot.send_message(message.chat.id, 'Пойдешь в кино?',
                           reply_markup=markup)





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

async def parser_serials(message: types.Message):
    data = serials.parser()
    for i in data:
        await bot.send_message(message.from_user.id,
                               f"{i['title']}\n\n{i['link']}")

async def parser_multiki(message: types.Message):
    data = multiki.parser()
    for i in data:
        await bot.send_message(message.from_user.id,
                               f"{i['title']}\n\n{i['link']}")

async def parser_anime(message: types.Message):
    data = anime.parser()
    for i in data:
        await bot.send_message(message.from_user.id,
                               f"{i['title']}\n\n{i['link']}")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_comand, commands=['start']),
    dp.register_message_handler(mem_comand, commands=['mem']),
    dp.register_message_handler(quiz_1, commands=['quiz']),
    dp.register_message_handler(question, commands=['Qu']),
    dp.register_message_handler(parser_serials, commands=['serials'])
    dp.register_message_handler(parser_multiki, commands=['multiki'])
    dp.register_message_handler(parser_anime, commands=['anime'])
