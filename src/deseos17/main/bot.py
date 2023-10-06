import asyncio
import os

from aiogram import Bot, Dispatcher

from deseos17.presentation.telegram.new_wish.dialog import new_wish_dialog
from .ioc import IoC


def get_dispatcher():
    ioc = IoC()
    dp = Dispatcher(ioc=ioc)
    dp.include_router(new_wish_dialog)
    return dp


async def bot_main():
    token = os.getenv("BOT_TOKEN")
    bot = Bot(token)

    await get_dispatcher().start_polling(bot)


if __name__ == '__main__':
    asyncio.run(bot_main())