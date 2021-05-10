import requests
import sqlite3
from bs4 import BeautifulSoup 

def scrape_book(url):
    respones = requests.get(url)
    soup =BeautifulSoup(respones.text,"html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book),get_price(book),get_rating(book))
        all_books.append(book_data)    

    save_books(all_books)
    
def save_books(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute('CREATE TABLE books (title TEXT,price REAL,rating INTEGER)')
    c.executemany("INSERT INTO books VALUES (?,?,?)",all_books)
    
    connection.commit()
    connection.close()

def get_title(book):
    return  book.find("h3").find("a")["title"]
def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("Â£",""))

def get_rating(book):
    paragraph = book.select(".star-rating")[0]
    rating=paragraph.get_attribute_list("class")[-1]
    ratings = {"zero":0,"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
    return ratings[rating]

scrape_book("https://books.toscrape.com/catalogue/category/books/history_32/index.html")
