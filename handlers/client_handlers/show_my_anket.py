from database import sqlliteClient
import KeyBoards.KeyBoards as KB
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


class FSMCChangeAnket(StatesGroup):
    answer = State()


async def message_change_photo(message: types.Message, state=None):
    await FSMCChangeAnket.answer.set()
    await message.answer("Пришлите новое фото")


async def back_to_main_menu(message: types.Message):
    await message.answer("Выбирите действие на клавиатуре", reply_markup=KB.main_menu_KeyBoard)


async def take_modified_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    user_id = message.from_user.id
    sqlliteClient.change_photo(user_id, photo)
    await message.answer("Фото было обновлено", reply_markup=KB.change_anket_menu)
    await state.finish()


async def message_change_description(message: types.Message, state=None):
    await FSMCChangeAnket.answer.set()
    await message.answer("Пришлите новое описание")


async def take_modified_description(message: types.Message, state: FSMContext):
    description = message.text
    user_id = message.from_user.id
    sqlliteClient.change_description(user_id, description)
    await message.answer("Описание было обновлено", reply_markup=KB.change_anket_menu)
    await state.finish()


async def delete_profile(message: types.Message):
    sqlliteClient.delete_user(message.from_user.id)
    await message.answer("Ваша анкета удаленна")


async def change_anket_menu(message: types.Message):
    info = sqlliteClient.take_user_info(message.from_user.id)
    await message.answer_photo(photo=info[0][5], caption= \
        f"{info[0][1]}, {info[0][2]}\n {info[0][4]}", reply_markup=KB.change_anket_menu)
