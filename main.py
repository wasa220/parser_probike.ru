from bs4 import BeautifulSoup as bs
import requests

URL = "https://pro-bike.ru"
response = requests.get(URL)
soup = bs(response.text, "lxml")

footer = soup.find_all("div", class_ = "main-footer_links_col")
raw_footer_links = []
for block in footer[4:6]:
    raw_footer_links.append(block.find_all('a'))
raw_footer_links = raw_footer_links[0][1:] + raw_footer_links[1][:-1]

footer_links = []
for i in raw_footer_links:
    footer_links.append(f'{URL}{i.get('href')}')

card_links = []
for category in footer_links[:1]:
    response = requests.get(category)
    soup = bs(response.text, "lxml")

    # pagination = int(soup.find('div', class_ = 'pagination').find('li', class_ = 'pagination__button-skip').nextSibling.nextSibling.text)
    # print(pagination)
    cards = soup.find('div', class_ = 'items__list_catalog').find_all('a')
    for card in cards:
        print(card.get('href'))