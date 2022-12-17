from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, dp
from aiogram import types, Dispatcher


# @dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Сколько материков на земле?"
    answers = [
        "10",
        "4",
        "7",
        "6",
        "5",
        "1",
    ]


    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )
# @dp.callback_query_handler(text="button_call_1")
async def quiz_3(call: types.CallbackQuery):
        markup = InlineKeyboardMarkup()
        button_call_1 = InlineKeyboardButton("NEXT 3", callback_data="button_call_3")
        markup.add(button_call_1)

        question = "Сколько  хрохромосом  у шимпанзе?"
        answers = [
            "46",
            "48",
            "34",
            "124",
            "96",
            "1234",
        ]
        await bot.send_poll(
            chat_id=call.from_user.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=1,
            explanation="Ничего страшного!",
            open_period=5,
            reply_markup=markup
        )
def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")