from pydoc import html
import datetime
from bs4 import BeautifulSoup as BS
import requests
from pprint import pprint



HEADERS = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
              'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}



def get_url():
        url = f"https://w140.zona.plus/movies" \

        return url

def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response
def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("li", class_="results-item-wrap",
    limit = 10)
    kino = []

    for i in items:
        kino.append({
            "url": f"https://w140.zona.plus{i.find('a').get('href')}",
        })

    return kino

def parse1():

    url = get_url()
    html = get_html(url)
    data = get_data(html.text)
    return data


parse1()
