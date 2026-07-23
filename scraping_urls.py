from bs4 import BeautifulSoup
import requests

url = "https://pik.warszawa.pl/kina-plenerowe-w-warszawie/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="pikKinoGrid_3")
cinema_cards = results.find_all("div", class_="pik-kino-karta-body")

for cinema in cinema_cards:
    links = cinema.find_all("a")[0]["href"]
    print(f"{links}")