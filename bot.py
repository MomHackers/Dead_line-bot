from vkbottle.bot import Bot
from routes import events, messages
from config import TOKEN, GROUP_ID  # Токен и id группы

bot = Bot(TOKEN, group_id=GROUP_ID)  # , debug="DEBUG"
bot.set_blueprints(events.bp, messages.bp)

if __name__ == '__main__':
    bot.run_polling()
