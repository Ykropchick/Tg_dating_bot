import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor



logging.basicConfig(level=logging.INFO)

bot = Bot(token="5538535273:AAHxu8JdYlERo1VXprFWzbXL-jMHxHURaiA")
dp = Dispatcher(bot, storage=MemoryStorage())


