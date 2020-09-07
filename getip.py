#!/usr/bin/python
from bs4 import BeautifulSoup as BS
import requests

r = requests.get("https://2ip.ru/")
pars = BS(r.content, 'html.parser')

res = pars.select('.main-content .ip-block .ip-info .ip span')
print(res[0].text)
