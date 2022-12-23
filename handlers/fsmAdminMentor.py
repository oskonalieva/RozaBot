from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import cancel_markup, submit_markup
from database.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    gruppa = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer("id ментора?", reply_markup=cancel_markup)
    else:
        await message.answer("Пиши в личке!")


async def load_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("имя ментора?")
    except ValueError:
        await message.answer("id должно быть числом")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('направление ментора')

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("возраст?)")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа")
    elif int(message.text) < 12 or int(message.text) > 50:
        await message.answer("Возростное ограничение!")
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Какая группа?")


async def load_gruppa(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gruppa'] = message.text
    await FSMAdmin.next()
    await message.answer("все правильно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("всё")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Ну и пошел ты!")
    else:
        await message.answer('НИПОНЯЛ!?')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты!")


def register_handlers_fsm_admin_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gruppa, state=FSMAdmin.gruppa)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
