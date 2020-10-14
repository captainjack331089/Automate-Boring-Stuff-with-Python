import requests
import requests
def get_page_html():
    url = 'https://www.costco.com/clorox-disinfecting-wipes,-variety-pack,-85-count,-5-pack.product.100534416.html'
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("img", {"class": "oos-overlay hide"})
    return len(out_of_stock_divs)

if __name__ == '__main__':
    url = 'https://www.costco.com/clorox-disinfecting-wipes,-variety-pack,-85-count,-5-pack.product.100534416.html'
    get_page_html()
    print(check_item_in_stock(url))

    url2 = "https://www.costco.com/nature-valley-crunchy-granola-bar%2c-oats-'n-honey%2c-1.49-oz%2c-49-count-.product.100243281.html"
    print(check_item_in_stock(url2))