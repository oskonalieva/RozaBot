from config import bot, dp
from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
