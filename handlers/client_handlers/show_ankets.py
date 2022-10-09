from database import sqlliteClient
import KeyBoards.KeyBoards as KB
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from create_bot import bot, dp

ankets = []
num_anket = 0
my_anket = []


async def show_ankets(message: types.Message):
    global ankets
    global num_anket
    global my_anket
    ankets = sqlliteClient.take_all_ankets(message.from_user.id)

    for anket in ankets:
        if anket[0] == message.from_user.id:
            my_anket = anket
            num_anket = anket[6]
            break

    await message.answer(text="Анкеты:", reply_markup=ReplyKeyboardRemove())
    try:
        sqlliteClient.increase_cur_anket(message.from_user.id, num_anket)

        await message.answer_photo(photo=ankets[num_anket][5], caption= \
            f"{ankets[num_anket][1]}, {ankets[num_anket][2]}\n {ankets[num_anket][4]}", reply_markup=KB.next_anket)
        num_anket += 1
    except IndexError as e:
        await message.answer("Все анкеты были просмотрены", reply_markup=KB.end_anekets_KeyBoard)


async def next_anket(callback: types.CallbackQuery):
    global ankets
    global num_anket
    try:
        sqlliteClient.increase_cur_anket(callback.from_user.id, num_anket)

        await callback.message.answer_photo(photo=ankets[num_anket][5], caption= \
            f"{ankets[num_anket][1]}, {ankets[num_anket][2]}\n {ankets[num_anket][4]}", reply_markup=KB.next_anket)
        num_anket += 1
    except IndexError as e:
        await callback.message.answer("Все анкеты были просмотрены", reply_markup=KB.end_anekets_KeyBoard)


async def like_anket(callback: types.CallbackQuery):
    global ankets
    global num_anket
    global my_anket
    try:
        sqlliteClient.increase_cur_anket(callback.from_user.id, num_anket)

        await callback.message.answer("Ваша симпатия была отправлена")
        sqlliteClient.add_sympathy(callback.from_user.id, ankets[num_anket - 1][0])
        await callback.message.answer_photo(photo=ankets[num_anket][5], caption= \
            f"{ankets[num_anket][1]}, {ankets[num_anket][2]}\n {ankets[num_anket][4]}", reply_markup=KB.next_anket)

        await bot.send_message(chat_id=ankets[num_anket - 1][0], Text="У вас новая симпатия")

        num_anket += 1
    except IndexError as e:
        await callback.message.answer("Все анкеты были просмотрены", reply_markup=KB.end_anekets_KeyBoard)


async def show_my_sympathies(message: types.Message):
    pass


async def reload_ankets(message: types.Message):
    if num_anket == len(ankets):
        sqlliteClient.reload_ankets(message.from_user.id)
        await show_ankets(message)
    else:
        pass
