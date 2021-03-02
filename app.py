from bs4 import BeautifulSoup
import requests
import logging
import os
from aiogram import Bot, Dispatcher, executor, types

url = 'http://samotlor.tv'
page = requests.get(url)

#print(page.status_code)

API_TOKEN = '2412414124124114'
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

new_news = []
news = []
news_item = []

soup = BeautifulSoup(page.text, "html.parser")
#soup2 = str(soup)
#with open('my_file.txt', 'w') as f:
#    f.write(soup2)  


news = soup.findAll('h4', class_="entry-title")
#print(news)

for news_item in news:
    if news_item.find('a') is not None:
        new_news.append(news_item.text)

#for i in range(len(new_news)):
    #print(new_news[i])

#with open('my_file3.txt', 'w') as f:
#    f.write("\n".join(new_news))  
#f.close()       

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"\n".join(new_news))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



