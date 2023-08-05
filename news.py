import requests
from bs4 import BeautifulSoup

class NewsSource:
    def __init__(self, name, alias, url, scrape):
        self.name = name
        self.alias = alias
        self.url = url
        self.scrape = scrape

    def fetch(self):
        return self.scrape(self.url)
         
def getNewsFeed(source):
    articles = source.fetch()

    return []

# News source scrapers
def scrapeCBC(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    news_cards = soup.find_all("a", class_="card")
    news_items = []

    for card in news_cards:
        headline_element = card.find(class_="headline")
        
        if headline_element == None:
            continue

        news_items.append({
            "headline": headline_element.text
        })
    return news_items

# Format models into strings 
def formatSnippets(article_snippets):
    out = "\n"

    for i, snippet in enumerate(article_snippets[1:5]):
        headline = snippet["headline"]
        out += "\033[1m" + str(i + 1) + ". " + headline + "\033[0m" + "\n\n"
    return out

