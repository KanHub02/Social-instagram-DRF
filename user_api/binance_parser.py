
from cgitb import html
from time import time
from xml.sax.handler import DTDHandler
from bs4 import BeautifulSoup
import requests
import datetime


URL_TITLE = "https://www.binance.com/ru/trade/BTC_BUSD?_from=markets&theme=dark&type=spot"

HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
}

def get_html(URL):
    request = requests.get(url=URL, headers=HEADER)
    return request


def get_price_data(html):
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("div", class_="css-1jx6fr9")
        data = []
        for i in items:
            data.append(i.find("div", class_="css-1qkv3vk").get("h1"))
            print(data)


# def get_title_data(html):
#         soup = BeautifulSoup(html, "html.parser")
#         items = soup.find_all("div", class_="css-leyy1t")
#         data = []
#         for i in items:
#             data.append(i.find("div", class_="css-1ap5wc6").get_text(),)
#         for i in data:
#             print(f"{i}\n")
    

html=get_html(URL_TITLE)
get_price_data(html.text)
# def start_scrapy():
#     html = get_html(URL)
#     if html.status_code == 200:
#         data = []
#         data.append({
#             'title': get_title_data(html.text),
#             "price": get_price_data(html.text)
#         })
#         print(data)


# start_scrapy()