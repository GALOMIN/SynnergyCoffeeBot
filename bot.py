import asyncio
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import CallbackQuery

import keyboards as kb

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
#Объект бота
bot = Bot(token='5830215115:AAGZyc_qy02L5RC71xV3HdIFRaiDdehNPLE')
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands=["start"], commands_prefix="/")
async def cmd_start(message:types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://okoffe.ru/wp-content/uploads/2018/05/Aromatnyj-napitok.jpg",
                         caption="Приветствую тебя в нашей замечательной кафейне!\nНаша кофейня рада принимать любого посетителя, которое хочет разбавить свои серые будни чашечкой ароматного кофе ☕️",
                          reply_markup=kb.greet_kb)

#Колбэк на команду /start
#@dp.callback_query_handler(text="Start")
#async def start_callback(query: CallbackQuery):
#    await bot.send_photo(chat_id=message.from_user.id,
#                         photo="https://okoffe.ru/wp-content/uploads/2018/05/Aromatnyj-napitok.jpg",
#                         caption="Приветствую тебя в нашей замечательной кафейне!\nНаша кофейня рада принимать любого посетителя, которое хочет разбавить свои серые будни чашечкой ароматного кофе ☕️",
#                          reply_markup=kb.greet_kb)

#Сообщение "Меню 💼"
@dp.message_handler(lambda message: message.text == "Меню 💼")
async def cmd_start(message:types.Message):
    await message.answer("Пожалуйста, выберите подходящую вам категорию 👇", reply_markup=kb.keyboard)

#Кнопка "назад"
@dp.callback_query_handler(text="Start")
async def start_callback(call: CallbackQuery):
    await call.message.answer(cmd_start)

# Запуск процесса поллинга новых апдейтов
async def main():
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 