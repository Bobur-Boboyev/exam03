from telegram import (InlineKeyboardButton, 
                      InlineKeyboardMarkup,
                      Update)
from telegram.ext import CallbackContext
from image_service import ImageService

class Handlers:
    def __init__(self, service: ImageService):
        self.service = service

    def start_command(self, update: Update, context: CallbackContext):
        keyboard = [
            [
                InlineKeyboardButton("🐶 Dog", callback_data='dog'),
                InlineKeyboardButton("🐱 Cat", callback_data='cat'),
                InlineKeyboardButton("🦊 Fox", callback_data='fox')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Qaysi hayvon rasmini ko\'rmoqchisiz?', reply_markup=reply_markup)

    def button_handler(self, update: Update, context: CallbackContext):
        query = update.callback_query
        animal = query.data
        query.answer()

        keyboard = [
            [InlineKeyboardButton("Yana 😎", callback_data=animal)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        image_url = self.service.fetch_random_image(animal)

        context.bot.send_photo(chat_id=query.message.chat_id, photo=image_url, reply_markup=reply_markup)

    def dog_command(self, update: Update, context: CallbackContext):
        url = self.service.fetch_random_image("dog")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

    def cat_command(self, update: Update, context: CallbackContext):
        url = self.service.fetch_random_image("cat")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

    def fox_command(self, update: Update, context: CallbackContext):
        url = self.service.fetch_random_image("fox")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)