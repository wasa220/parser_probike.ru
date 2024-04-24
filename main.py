from bs4 import BeautifulSoup as bs
import requests

URL = "https://pro-bike.ru/"
response = requests.get(URL)
soup = bs(response.text, "lxml")

footer = soup.find_all("div", class_ = "main-footer_links_col")
raw_footer_links = []
for block in footer[4:6]:
    raw_footer_links.append(block.find_all('a'))
print(raw_footer_links)