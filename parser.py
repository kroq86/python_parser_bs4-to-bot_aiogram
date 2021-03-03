from bs4 import BeautifulSoup
import requests
import logging
import os
import sys
from collections import OrderedDict

stdoutOrigin=sys.stdout 
sys.stdout = open("parser2.txt", "w")

url = 'http://samotlor.tv'
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
 
sys.stdout.close()
sys.stdout=stdoutOrigin

filename = r'parser2.txt'
with open(filename, encoding='utf-8') as file:
    uniq = OrderedDict.fromkeys(file)
with open(filename, 'w', encoding='utf-8') as file:
    file.writelines(uniq)