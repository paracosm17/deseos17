import asyncio

from aiogram import Bot, Dispatcher

from deseos17.presentation.telegram.new_wish import new_wish_dialog
from .ioc import IoC
from .config import load_bot_config, BotConfig


def get_dispatcher(config: BotConfig):
    ioc = IoC(tg_token=config.bot_token)
    dp = Dispatcher(ioc=ioc)
    dp.include_router(new_wish_dialog)
    return dp


async def bot_main():
    config = load_bot_config()
    bot = Bot(config.bot_token)

    await get_dispatcher(config).start_polling(bot)


if __name__ == '__main__':
    asyncio.run(bot_main())
