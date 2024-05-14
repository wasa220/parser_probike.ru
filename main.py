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

def get_product_data():
    for card in card_links[2:3]:
        soup = req(card)
        
        product_name = soup.find('h1', class_ = 'page-title').text
        product_code = str(soup.find('div', class_ = 'item__content_tags_code').find('span').next_sibling).strip()
        product_article = soup.find("div", class_ = 'item__info_variant_artikul').find('div', class_ = 'item__info_variant_row_value').text.strip()
        product_availability = soup.find('div', class_ = 'item__info_variant_nalichie'). find('div', class_ = 'item__info_variant_row_value').text.strip()
        product_price_old = soup.find('div', class_ = 'item__info_variant_price_old').text.strip()
        product_price = soup.find('div', class_ = 'item__info_variant_price_final').text.strip()
        product_manufacturer = soup.find('span', class_ = 'warranty__manuf_title dotted').text.strip()

        product_picture = soup.find('div', class_ = 'content-container content-container__mobile-sticky item__content').find('div', class_ = 'pb-viewer__element').find('img').get('srcset').split('\n')

        # sale_amount = product_price_old - product_price
        print(product_picture)


if __name__ == '__main__':
    get_categories_links()
    get_card_links()
    get_product_data()