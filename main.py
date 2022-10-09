from create_bot import Bot, dp
from handlers import reg_client_hendlers, admin
import logging
from database import sqlliteClient, sqlliteAdmin
from aiogram.utils import executor


sqlliteClient.sql_start()
sqlliteAdmin.sql_start()

logging.info("Sql is started")

reg_client_hendlers.register_handlers_client(dp)
admin.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True)



