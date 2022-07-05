from bs4 import BeautifulSoup
import requests

URL = "https://rezka.ag/series/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}



def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    serials = []

    for i in items:
        serials.append(
            {
                "link": i.find('div', class_="b-content__inline_item-cover").find('a').get('href'),
                "title": i.find('div', class_="b-content__inline_item-link").find('a').getText(),
                "img": i.find('div').find('a').find('img').get('src')
            }
        )
    return serials


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        serials = get_data(html.text)
        return serials
    else:
        raise Exception("Error!")