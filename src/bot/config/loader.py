import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from pathlib import Path

from AuthoConclusionBot.settings import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
storage = JSONStorage(f'{Path.cwd()}/{"fsm_data.json"}')
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, storage=storage)


if __name__ == "__main__":
    storage.write(Path.cwd())
