import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class NewsSource:
    def __init__(self, name, alias, url, scrape):
        self.name = name
        self.alias = alias
        self.url = url
        self.scrape_snippet = scrape()["snippet"]
        self.scrape_content = scrape()["content"]

    def fetch(self):
        return self.scrape_snippet(self.url)

    def read(self, article_snippet):
        out = "\033[1m" + article_snippet["headline"] + "\033[0m" + "\n\n"
        out += self.scrape_content(article_snippet)
        return out
        
def getNewsFeed(source):
    articles = source.fetch()

    return []

# News source scrapers
def scrapeCBC():
    def scrapeSnippets(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        news_cards = soup.find_all("a", class_="card")
        news_items = []

        for card in news_cards:
            headline_element = card.find(class_="headline")
            
            if headline_element == None:
                continue

            news_items.append({
                "headline": headline_element.text,
                "url": urljoin(url, card["href"])
            })
        return news_items
    
    def scrapeContent(article_snippet):
        page = requests.get(article_snippet["url"])
        soup = BeautifulSoup(page.content, "html.parser")
        content_element = soup.find(class_="story")
        out = ""

        for string in content_element.strings:
            out += string
        return out

    return { 
        "snippet": scrapeSnippets, 
        "content": scrapeContent
    }
    
    
def scrapeHackerNews():
    def scrapeSnippets(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        item_rows = soup.find_all("tr", class_="athing")
        news_items = []

        for row in item_rows:
            headline_wrapper_element = row.find("span", class_="titleline")
            headline_element = headline_wrapper_element.find("a")

            if headline_element == None:
                continue

            news_items.append({
                "headline": headline_element.text,
                "url": headline_element["href"]
            })
        return news_items
    def scrapeContent(article_snippet):
        url = article_snippet["url"]
        return f"HackerNews does not display article content!\n\nPlease read the article by following this link:\n{url}\n\n"
    
    return {
        "snippet": scrapeSnippets,
        "content": scrapeContent
    }
