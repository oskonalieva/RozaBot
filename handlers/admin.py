from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMINS
from database.bot_db import *


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой босс!")
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer(f"{user[0]} {user[1]} {user[2]} "
                        f"{user[3]}\n{user[4]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"delete {user[2]}",
                                         callback_data=f"delete {user[0]}")
                )
            )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))