from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from handlers.base_handler import BaseHandler


class ByeHandler(BaseHandler):
    @classmethod
    def register(cls, app):
        app.add_handler(CommandHandler('bye', cls.callback))

    @staticmethod
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f'Bye {update.effective_user.first_name}')
