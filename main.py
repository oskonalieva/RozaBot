from config import dp
from aiogram.utils import executor
import asyncio
from handlers import client, callback, extra, fsmAdminMentor
from handlers import client, callback, extra, fsmAdminMentor, admin, notification
import logging

from database.bot_db import sql_create
from database import bot_db
bot_db.register_handlrs_bot_db(dp)
admin.register_handlers_admin(dp)
fsmAdminMentor.register_handlers_fsm_admin_mentor(dp)
callback.register_handler_callback(dp)
notification.register_handlers_notification(dp)

client.register_handler_client(dp)

extra.register_handler_extra(dp)
async def  on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

