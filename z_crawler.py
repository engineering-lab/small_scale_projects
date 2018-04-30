import requests
from bs4 import BeautifulSoup

def search_spider(max_pages):
    page = 2
    while page <= max_pages:
        url = 'https://www.gumtree.com/computers-software/so145sq/page' +str(page)
        data_vault = requests.get(url)
        plain_text = data_vault.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'listing-link'}):
            href = "https://gumtree.com" + link.get('href')
            print(href)
            page+= 1


search_spider(3)





