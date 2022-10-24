from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

# клавиатура главного меню
main_menu_KeyBoard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
main_menu_KeyBoard.add("Посмотреть все анкеты")
main_menu_KeyBoard.add("Посмотреть мои симпатии")
main_menu_KeyBoard.add("Моя анкета")

# клавиатура изменения меню
change_anket_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
change_anket_menu.add("Изменить фото")
change_anket_menu.add("Изменить описание")
change_anket_menu.add("Отмена")


# клавиатура админа
admin_KeyBoard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
admin_KeyBoard.add("Hello")
admin_KeyBoard.add("Изменить данные для входа")
admin_KeyBoard.add("Отмена")

# клавиатруа когда заканчиваеться все анкеты
end_anekets_KeyBoard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
end_anekets_KeyBoard.add("Смотреть старые анкеты")
end_anekets_KeyBoard.add("Отмена")


# клавиатру, которая появляеться когда ты просматриваешь все анкеты
next_anket = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
next_anket.add(InlineKeyboardMarkup(text="Следущая", callback_data="next"), InlineKeyboardMarkup(text="Нравиться", callback_data="like"))
next_anket.add(InlineKeyboardMarkup(text="Назад", callback_data="back"))

# клавиатура когда ты просматриваешь симпатии, которые к тебе пришли
sympathy_KeyBoard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
sympathy_KeyBoard.add(InlineKeyboardMarkup(text="Нравиться", callback_data="like_symp"), InlineKeyboardMarkup(text="Не Нравиться", callback_data="not_like_symp"))

