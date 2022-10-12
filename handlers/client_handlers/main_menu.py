from database import sqlliteClient
import KeyBoards.KeyBoards as KB
from create_bot import bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
import logging
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove


class FSMClient(StatesGroup):
    name = State()
    age = State()
    sex = State()
    description = State()
    photo = State()


async def cm_start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id"] = message.from_user.id

    await FSMClient.name.set()
    await message.answer('Укажите ваше имя')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMClient.next()
    await message.answer("Введите свой возраст")


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    builder = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    builder.add(types.KeyboardButton(text='М'))
    builder.add(types.KeyboardButton(text='Ж'))

    await FSMClient.next()
    await message.answer("Введите свой пол", reply_markup=builder)


async def load_sex(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = message.text

    remove = ReplyKeyboardRemove()

    await FSMClient.next()
    await message.answer("Введите свое описание", reply_markup=remove)


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await FSMClient.next()
    await message.answer("Прикрепите свое фото")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        data['cur_anket'] = 0

    await sqlliteClient.sql_add_command(state)
    logging.info(f"The user data was recorded")
    await message.answer("Спасибо вся информация записана")
    await state.finish()


async def main_menu(message: types.Message, state: FSMContext):
    global cur_pos
    info = sqlliteClient.check_if_exist(message.from_user.id)
    if info:
        await message.answer("Выберите действие на клавиатуре", reply_markup=KB.main_menu_KeyBoard)
    else:
        await cm_start(message, state)



ankets = []
num_anket = 0

async def show_my_sympathies(message: types.Message):
    global ankets
    global num_anket
    try:
        ankets = sqlliteClient.take_sympathy(message.from_user.id)
        await message.answer_photo(photo=ankets[num_anket][5], caption= \
            f"{ankets[num_anket][1]}, {ankets[num_anket][2]}\n {ankets[num_anket][4]}", reply_markup=KB.sympathy_KeyBoard)
    except IndexError as e:
        await message.answer("У вас пока нет симпатий")


async def like_symp(callback: types.CallbackQuery):
    global ankets
    global num_anket
    try:
        await callback.message.answer_photo(photo=ankets[num_anket][5], caption= \
            f"{ankets[num_anket][1]}, {ankets[num_anket][2]}\n У вас взаимная сипатия \n Username:{ankets[num_anket][0]}")
        await bot.send_photo(chat_id=ankets[num_anket][0], photo=ankets[num_anket][5], caption= \
            f"{ankets[num_anket][1]}, {ankets[num_anket][2]}\n У вас взаимная сипатия \n Username:{callback.from_user.id}")
        sqlliteClient.delete_sympathy(ankets[num_anket][0], callback.from_user.id)
        num_anket += 1
        await callback.message.answer_photo(photo=ankets[num_anket][5], caption= \
            f"{ankets[num_anket][1]}, {ankets[num_anket][2]}\n {ankets[num_anket][4]}", reply_markup=KB.sympathy_KeyBoard)
    except IndexError as e:
        await callback.message.answer("У вас пока нет симпатий")

async def not_like_symp(callback: types.CallbackQuery):
    global num_anket
    global ankets
    sqlliteClient.delete_sympathy(ankets[num_anket][0], callback.from_user.id)
    try:
        num_anket += 1
        await callback.message.answer_photo(photo=ankets[num_anket][5], caption= \
            f"{ankets[num_anket][1]}, {ankets[num_anket][2]}\n {ankets[num_anket][4]}", reply_markup=KB.sympathy_KeyBoard)
    except IndexError as e:
        await callback.message.answer("У вас пока нет симпатий")




async def back_to_mainmenu_callback(callback: types.CallbackQuery):
    await callback.message.answer("Выберите действие на клавиатуре", reply_markup=KB.main_menu_KeyBoard)
