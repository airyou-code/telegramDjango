from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.handlers.start.static_text import github_button_text


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(
            github_button_text, url="https://github.com/ohld/django-telegram-bot"
        ),
    ]]

    return InlineKeyboardMarkup(buttons)
