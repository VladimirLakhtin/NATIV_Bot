from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()
dp.include_routers(router)
