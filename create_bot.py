from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import user_router, admin_router


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()
dp.include_routers(admin_router, user_router)
