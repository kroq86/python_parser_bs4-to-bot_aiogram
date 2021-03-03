from bs4 import BeautifulSoup
import requests
import logging
import os
import sys

stdoutOrigin=sys.stdout 
sys.stdout = open("parser2.txt", "w")

url = 'http://samotlor.tv'
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
 
sys.stdout.close()
sys.stdout=stdoutOrigin