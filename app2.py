from bs4 import BeautifulSoup
import requests
import logging
import os
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

with open("parser2.txt") as file:
    array = [row.strip() for row in file]

API_TOKEN = '00000'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

site = 'http://samotlor.tv'

def urlTake(site):
    i = random.randint(18,52)
    url = site + array[i]
    return(url)


def parse(url):
    new_news = []
    news = []
    news_item = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    news = soup.findAll('div', class_="sppb-addon-content")
    for news_item in news:
        if news_item.find('p') is not None:
            try: new_news.append(news_item.text),new_news.append(url)
            except Exception: parse(url)
    return new_news



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Показать", "На сайте"]
    keyboard.add(*buttons)
    await message.reply(f"\n".join(parse(urlTake(site))))
    await message.answer("Показать следующую новость?", reply_markup=keyboard)

@dp.message_handler(Text(equals="Показать"))
async def with_puree(message: types.Message):
    await message.reply(f"\n".join(parse(urlTake(site))))

    


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