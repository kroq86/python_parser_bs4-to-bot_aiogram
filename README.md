# python_parser_bs4-to-bot_aiogram
Parsing site with python and BS4 and send to Telegram bot via aiogram

## Welcome to python_parser_bs4-to-bot_aiogram

Это скрипт написанный для компании Самотлор, в свободное от работы время. 

```markdown
Особо горжусь этой функцией 


def parse():
    global new_news
    new_news = []
    news = []
    news_item = []
    i = random.randint(0,31)
    global url
    url = 'http://samotlor.tv' + array[i]
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    news = soup.findAll('div', class_="sppb-addon-content")
    for news_item in news:
        if news_item.find('p') is not None:
            try: new_news.append(news_item.text)
            except Exception: parse()

[Link](url) and ![Image](src)
```


