from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from handlers.client_handlers.main_menu import *
from handlers.client_handlers.show_my_anket import *
from handlers.client_handlers.show_ankets import *


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(main_menu, Text(equals="Главное меню", ignore_case=True))
    dp.register_message_handler(main_menu, commands='start')

    dp.register_message_handler(back_to_main_menu, Text(equals="Отмена", ignore_case=True))

    dp.register_message_handler(reload_ankets, Text(equals="Смотреть старые анкеты"))

    dp.register_message_handler(show_my_sympathies, Text(equals="Посмотреть мои симпатии", ignore_case=True))
    dp.register_callback_query_handler(like_symp, Text(equals="like_symp"))
    dp.register_callback_query_handler(not_like_symp, Text(equals="not_like_symp"))

    dp.register_callback_query_handler(next_anket, Text(equals="next"))
    dp.register_callback_query_handler(like_anket, Text(equals="like"))
    dp.register_callback_query_handler(back_to_mainmenu_callback, Text(equals="back"))

    dp.register_message_handler(show_ankets, Text(equals="Посмотреть все анкеты", ignore_case=True))

    dp.register_message_handler(change_anket_menu, Text(equals="Моя анкета", ignore_case=True))

    dp.register_message_handler(message_change_photo, Text(equals="Изменить фото", ignore_case=True), state=None)
    dp.register_message_handler(take_modified_photo, state=FSMCChangeAnket.answer, content_types=['photo'])

    dp.register_message_handler(message_change_description, Text(equals="Изменить описание", ignore_case=True),
                                state=None)
    dp.register_message_handler(take_modified_description, state=FSMCChangeAnket.answer)

    dp.register_message_handler(load_name, state=FSMClient.name)
    dp.register_message_handler(load_age, lambda message: message.text.isdigit(), state=FSMClient.age)
    dp.register_message_handler(load_sex, lambda message: message.text in ['М', "м", "Ж", "ж"], state=FSMClient.sex)
    dp.register_message_handler(load_description, state=FSMClient.description)
    dp.register_message_handler(load_photo, state=FSMClient.photo, content_types=['photo'])
