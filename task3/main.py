from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from image_bot import ImageBot

def main():
    # Bot yaratish
    bot = ImageBot()
    
    
    # Updater sozlash
    updater = Updater(bot.token)
    dp = updater.dispatcher
    
    # Handlerlarni qo'shish
    dp.add_handler(CommandHandler('start', bot.handlers.start_command))
    dp.add_handler(CommandHandler('dog', bot.handlers.dog_command))
    dp.add_handler(CommandHandler('cat', bot.handlers.cat_command))
    dp.add_handler(CommandHandler('fox', bot.handlers.fox_command))
    dp.add_handler(CallbackQueryHandler(bot.handlers.button_handler))
    
    # Ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()