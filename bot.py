from vkbottle import Bot, Message
from config import TOKEN

bot = Bot(TOKEN)


@bot.on.message(text="My name is <name>", lower=True)
async def wrapper(ans: Message, name):
    await ans("Hello, {}".format(name))


if __name__ == '__main__':
    bot.run_polling(skip_updates=False)
