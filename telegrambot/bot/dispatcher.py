"""
    Telegram event handlers
"""
from telegram.ext import Updater, CommandHandler

from backend.settings import DEBUG
# from bot.handlers.admin import handlers as admin_handlers
# from bot.handlers.location import handlers as location_handlers
from bot.handlers.start import handlers as start_handlers
from backend.settings import TELEGRAM_TOKEN
# from bot.handlers.broadcast_message import handlers as broadcast_handlers
from bot.main import bot


def setup_dispatcher(dp):

    dp.add_handler(CommandHandler("start", start_handlers.command_start))

    return dp

# n_workers = 0 if DEBUG else 4
# dispatcher = setup_dispatcher(
#     Updater(bot.token, use_context=True)
# )
