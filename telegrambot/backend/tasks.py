# tasks.py
from backend.celery import app
from bot.main import bot
from telegram import Update
from telegram.ext import Updater
from bot.dispatcher import setup_dispatcher


@app.task(ignore_result=True)
def process_telegram_event(update_json):
    update = Update.de_json(
        update_json,
        bot=bot
    )
    updater = Updater(bot.token, use_context=True)
    dp = setup_dispatcher(updater.dispatcher)
    dp.process_update(update)
