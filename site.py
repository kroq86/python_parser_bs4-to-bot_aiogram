from bs4 import BeautifulSoup
import requests
import logging
import os
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

with open("parser.txt") as file:
    array = [row.strip() for row in file]

i = random.randint(0,31)
url = 'http://samotlor.tv' + array[i]
print(url)
page = requests.get(url)

API_TOKEN = '1666903357:AAEhDQ9L04D6NCr6qwhKyss1zy69NZvTbr0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

new_news = []
news = []
news_item = []

soup = BeautifulSoup(page.text, "html.parser")

news = soup.findAll('div', class_="sppb-addon-content")

bug = soup.findAll('div', class_="article-full-image")

kek = str(bug)
lol = kek[43:108]

for news_item in news:
    if news_item.find('p') is not None:
        new_news.append(news_item.text)    
print(new_news)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Показать", "На сайте"]
    keyboard.add(*buttons)
    global i
    i=i+2
    print(i)
    await message.reply(f"".join(lol))
    await message.reply(f"\n".join(new_news))
    await message.answer("Показать следующую новость?", reply_markup=keyboard)

@dp.message_handler(Text(equals="Показать"))
async def with_puree(message: types.Message):
    global i
    i=i+2
    print(i)
    await message.reply(f"".join(lol))
    await message.reply(f"\n".join(new_news))


@dp.message_handler(Text(equals="На сайте"))
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Samotlor.tv", url="https://samotlor.tv"),
        types.InlineKeyboardButton(text="Vkontakte", url="https://vk.com/samotlor_tv")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Cсылки", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



