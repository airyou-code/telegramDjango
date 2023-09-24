from telegram import Update
from telegram.ext import CallbackContext

from bot.handlers.start import static_text
from users.models import Person
from bot.handlers.start.keyboards import make_keyboard_for_start_command


def command_start(update: Update, context: CallbackContext) -> None:
    u, created = Person.get_user_and_created(update, context)
    # if created:
    #     text = static_text.start_created.format(first_name=u.first_name)
    # else:
    #     text = static_text.start_not_created.format(first_name=u.first_name)
    # print(u)
    update.message.reply_text("Привет, это ваш бот!")
