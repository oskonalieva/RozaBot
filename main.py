from config import dp
from aiogram.utils import executor
from handlers import client, callback, extra, fsmAdminMentor
import logging

fsmAdminMentor.register_handlers_fsm_admin_mentor(dp)
callback.register_handler_callback(dp)
client.register_handler_client(dp)

extra.register_handler_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
