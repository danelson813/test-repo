import requests
from bs4 import BeautifulSoup as bs
from time import sleep


base_url = "https://books.toscrape.com/"
book_info = []
for i in range(1,3):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')

    books = soup.find_all('article')

    for book in books:
        data = {}
        link = book.find('a').get('href')
        title = book.find('h3').find('a').get('title')
        price = book.find('div', class_="product_price").find('p', class_="price_color").text[2:]
        data = {
            "link": base_url+link,
            "title": title,
            "price": price
        }
        book_info.append(data)
        book_info.append("\n")
        # sleep(2)

with open("data.csv", "a") as f:
            f.write(str(book_info))
