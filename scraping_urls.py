from bs4 import BeautifulSoup
import requests
import json 

url = "https://pik.warszawa.pl/kina-plenerowe-w-warszawie/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="pikKinoGrid_3")
cinema_cards = results.find_all("div", class_="pik-kino-karta-body")

for cinema in cinema_cards:
    url = cinema.find_all("a")[0]["href"]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    name = soup.find(itemprop="headline")
    print(name.text.strip())
    #print(type(name.text.strip()))
    div = soup.find('div', {'class':'entry-content'})
    results = [[i.text for i in b.find_all('li')] for b in div.find_all('ul')]
    print(results)
    #print(type(results))
    div_location = soup.find('div', {'class':'lokalizacja'})
    location = div_location.find('p').text
    print(location)
    #print(type(location))
    dict = {"name": name.text.strip(), "content": results, "location" : location}
    #print(dict)
    with open("cinemas.jsonl", "a", encoding='utf8') as file:
        file.write(json.dumps(dict, ensure_ascii=False) + "\n")
    