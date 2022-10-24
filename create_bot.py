import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


# запускает логгирование
logging.basicConfig(level=logging.INFO)

# отдет боту токен
bot = Bot(token="5538535273:AAHxu8JdYlERo1VXprFWzbXL-jMHxHURaiA")
# запескает диспетчер
dp = Dispatcher(bot, storage=MemoryStorage())


