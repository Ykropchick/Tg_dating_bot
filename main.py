from create_bot import Bot, dp
from handlers import reg_client_hendlers, admin
import logging
from database import sqlliteClient, sqlliteAdmin
from aiogram.utils import executor

# зарускает бд клиентов
sqlliteClient.sql_start()
# зарускате бд админов
sqlliteAdmin.sql_start()

logging.info("Sql is started")

# регистрирует хендлеры клиентов
reg_client_hendlers.register_handlers_client(dp)
# регистрирует хендлеры админов
admin.register_handlers_client(dp)

# начинает работу бота
executor.start_polling(dp, skip_updates=True)



