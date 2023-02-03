from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Кнопочки
button_1 = KeyboardButton('Меню 💼')
button_2 = KeyboardButton('Помощь ❓')
button_3 = KeyboardButton('Контакты 🔊')
button_4 = KeyboardButton('Акционное меню 🎉')

#реплай-клавиатура
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_1, button_4, button_2, button_3)

#инлайн-клавиатура "Меню"
keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text="Выпечка 🥐", callback_data="Vipechka"),
        InlineKeyboardButton(text="Кофе ☕️", callback_data="Coffee"),
        InlineKeyboardButton(text="Назад ↩️", callback_data="Start")
    )