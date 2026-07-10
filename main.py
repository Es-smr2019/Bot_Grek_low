import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from database import init_db
from handlers import (
    common_router, owner_router, currency_router, games_router, marriage_router,
    profile_router, rp_router, shop_router, admin_router, inline_router
)

logging.basicConfig(level=logging.INFO)


async def main():
    await init_db()
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        common_router,
        owner_router,
        currency_router,
        games_router,
        marriage_router,
        profile_router,
        rp_router,
        shop_router,
        admin_router,
        inline_router,
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
