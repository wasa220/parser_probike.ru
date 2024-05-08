from bs4 import BeautifulSoup as bs
import requests


URL = "https://pro-bike.ru"


def req(url):
    response = requests.get(url = url)
    soup = bs(response.text, "lxml")
    
    return soup

categories_links = []
def get_categories_links():
    soup = req(URL)
    footer = soup.find_all("div", class_ = "main-footer_links_col")
    raw_footer_links = []
    for block in footer[4:6]:
        raw_footer_links.append(block.find_all('a'))
    raw_footer_links = raw_footer_links[0][1:] + raw_footer_links[1][:-1]

    for i in raw_footer_links:
        categories_links.append(f'{URL}{i.get('href')}')

card_links = []
def get_card_links():
    for category in categories_links[:1]:
        soup = req(category)

        cards = soup.find('div', class_ = 'items__list_catalog').find_all('a')
        for card in cards[:-5]:
            card_links.append(f'{URL}{card.get('href')}')


if __name__ == '__main__':
    get_categories_links()
    get_card_links()
    print(card_links)