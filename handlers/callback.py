from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Next->', callback_data='button_call_2')
    markup.add(button_call_2)
    question = 'Кто соверщенналетний'
    answer = [
        '<10', '>10<18', '18+'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Изи',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton('Next->', callback_data='button_call_3')
    markup.add(button_call_3)
    question = 'Какой это перс из аниме Ванпис?'
    answer = [
        'Рарано Зора',
        'Усоп',
        'Нами',
        'Ло',
        'Мугивара Луффи'
    ]
    photo = open('media/1.gif', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation='Изи',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        # reply_markup=markup
    )


async def question_1(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Хорошо Идем', )


async def question_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_6 = InlineKeyboardButton("Нет денег",
                                         callback_data="button_call_6")
    button_call_7 = InlineKeyboardButton("Не хочу",
                                         callback_data="button_call_7")
    markup.add(button_call_6, button_call_7)
    await bot.send_message(call.message.chat.id, 'Почему?',
                           reply_markup=markup)


async def question_2_1(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Хорошо', )


async def question_2_2(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Ладно', )


async def question_2_3(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Ок', )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == 'button_call_2')
    dp.register_callback_query_handler(question_1,
                                       lambda call: call.data == 'button_call_4')
    dp.register_callback_query_handler(question_2,
                                       lambda call: call.data == 'button_call_5')
    dp.register_callback_query_handler(question_2_1,
                                       lambda call: call.data == 'button_call_5')
    dp.register_callback_query_handler(question_2_2,
                                       lambda call: call.data == 'button_call_6')
    dp.register_callback_query_handler(question_2_3,
                                       lambda call: call.data == 'button_call_7')