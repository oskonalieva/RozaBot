from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from config import bot, dp, ADMINS
from aiogram import types, Dispatcher


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"здравствуй {message.from_user.first_name}")


async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('сообщение должно быть ответом')


async def game(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.text.startswith('game'):
            emojies = ['⚽', '🏀', '🎲', '🎰', '🎯', '🎳']
            emoji = random.choice(emojies)
            await bot.send_dice(message.chat.id, emoji=emoji)
    else:
        await message.answer('ты не админ!')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Сколько хромосом у человека?"
    answers = [
        '90',
        '67',
        '47',
        '46',
        '12',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo = open('media/mem 1.jpeg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from config import bot, dp, ADMINS
from aiogram import types, Dispatcher
from parser.parser_wheel import parser



# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"здравствуй {message.from_user.first_name}")


async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('сообщение должно быть ответом')


async def game(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.text.startswith('game'):
            emojies = ['⚽', '🏀', '🎲', '🎰', '🎯', '🎳']
            emoji = random.choice(emojies)
            await bot.send_dice(message.chat.id, emoji=emoji)
    else:
        await message.answer('ты не админ!')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Сколько хромосом у человека?"
    answers = [
        '90',
        '67',
        '47',
        '46',
        '12',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo = open('media/mem 1.jpeg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

async def parsser_wheels(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,

            f"{item['link']}"
            f"{item['logo']}\n"
            f"# {item['size']}\n"
            f"цена - {item['price']}\n"
            )







def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(game)
    dp.register_message_handler(parsser_wheels, commands=["wheel"])
