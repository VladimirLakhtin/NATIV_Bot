import asyncio

from create_bot import dp, bot
from models import init_db


async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
