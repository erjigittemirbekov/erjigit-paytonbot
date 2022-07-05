from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import bot_db

from config import bot, ADMIN


class FSMADMIN(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id == ADMIN:
        await FSMADMIN.photo.set()
        await message.answer(
            f"Здравствуйте {message.from_user.full_name}, отправьте фото блюдо",
        )
    else:
        await message.reply("Ты не админ и еще пиши в личку!")

async def load_photo(message: types.Message, state: FSMContext ):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMADMIN.next()
    await message.answer("Название блюдо")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMADMIN.next()
    await message.answer("Описание блюдо")


async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMADMIN.next()
    await message.answer("Цена блюдо")


async def load_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)
        await bot.send_photo(message.from_user.id,
                             data['photo'],
                             caption=f"Блюдо: {data['name']}\n"
                                     f"Описание: {data['description']}\n"
                                     f"Цена: {data['price']}\n")
        await bot_db.sql_command_insert(state)
        await state.finish()

    except:
        await message.reply("Только числа")

async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Регистрация отменена!")

def register_fsmadmin_handler(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands="cancel")
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMADMIN.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMADMIN.name)
    dp.register_message_handler(load_desc, state=FSMADMIN.description)
    dp.register_message_handler(load_price, state=FSMADMIN.price)