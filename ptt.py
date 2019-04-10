import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.ptt.cc/bbs/LoL/M.1554832602.A.17B.html')
soup = BeautifulSoup(res.text)
print (soup.select('div[id^=main-content]')[0].text)