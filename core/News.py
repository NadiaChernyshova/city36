import requests
import json
from bs4 import BeautifulSoup

class News:
    
    def __init__(self):
        self.url = 'http://downtown.ru/'

    def get_html(self):
        response = requests.get(self.url)
        return response.text

    def parse(self):
        soup = BeautifulSoup(self.get_html(), 'lxml')
        articles = soup.find_all('article', class_='b-post-view m-post-view__mid')
        res = []
        for article in articles:
            title = article.find('a', class_="b-post-view__title").text
            desc = article.find('div', class_="b-post-view__desc").text
            link = article.find('a', class_="b-post-view__title").get('href')
            link = self.url + link
            res.append({"title": title, "desc": desc, "link": link})

        return res