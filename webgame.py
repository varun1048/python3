from bs4 import BeautifulSoup 
from time import sleep
from csv import DictWriter
import requests

all_quotes = []
url="/page/1"
while url:
    res = requests.get(f"https://quotes.toscrape.com{url}")
    print(url)
    soup = BeautifulSoup(res.text,"html.parser")
    quotes = soup.find_all(class_="quote") 

    for quote in quotes:
        all_quotes.append({
            "text":quote.find(class_="text").get_text(),
            "author":quote.find(class_="author").get_text(),
            "bio-link":quote.find('a')['href']
        })

    next_btn = soup.find(class_="next")
    url = next_btn.find('a')["href"] if next_btn else None
    # sleep(2)


with open("data.csv","w") as file:
    header = ["text","author","bio-link"]
    csv_wirter = DictWriter(file,fieldnames=header)
    csv_wirter.writeheader()
    for a in all_quotes:
        csv_wirter.writerow({
            "text":a["text"]
            ,"author":a["author"]
            ,"bio-link":a["bio-link"]
        })      
    


