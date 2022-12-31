import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("ID получен!")


async def go_to_library():
    await bot.send_message(chat_id=chat_id, text="Сегодня надо в библиотеку!")


async def scheduler():
    aioschedule.every().saturday.at('11:00').do(go_to_library)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_id, lambda word: "напомни" in word.text)