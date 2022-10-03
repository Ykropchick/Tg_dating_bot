from aiogram.types import ReplyKeyboardMarkup

main_menu_KeyBoard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

main_menu_KeyBoard.add("Посмотреть все анкеты")
main_menu_KeyBoard.add("Посмотреть мои симпатии")
main_menu_KeyBoard.add("Моя анкета")

change_anket_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

change_anket_menu.add("Изменить фото")
change_anket_menu.add("Изменить описание")
change_anket_menu.add("Отмена")

admin_KeyBoard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

admin_KeyBoard.add("Hello")
admin_KeyBoard.add("Изменить данные для входа")
admin_KeyBoard.add("Отмена")