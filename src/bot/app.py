import os

import django
from aiogram import Dispatcher
from aiogram.utils import executor

# from backend.tasks import notifier, notify_epid_and_md
from . import handlers
from .config.loader import dp, scheduler



def run_bot():
    """Запускает процессы бота"""
    _setup_django()
    print("Bot started")
    scheduler.start()
    executor.start_polling(
        dp, on_shutdown=_on_shutdown, skip_updates=True
    )
    print("Bot started")


# async def _on_startup(dispatcher: Dispatcher):
#     """Регистрирует ветки handlers"""
#     handlers.setup(dispatcher)


async def _on_shutdown(dispatcher: Dispatcher):
    """Ожидает и закрывает хранилище dispatcher"""
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

    
def _setup_django():
    """Установка окружения Django внутри бота"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
    django.setup()



