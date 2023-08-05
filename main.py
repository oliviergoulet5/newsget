import requests
from bs4 import BeautifulSoup

# Prompt Toolkit
def promptInt(prompt):
    result = input(prompt)
    if not result.isdigit():
        return None
    return int(result)

def promptIntOrPanic(prompt):
    result = promptInt(prompt)
    if result == None:
        exit(1)
    else:
        return result

# News Sources
def getNewsFeed(source):
    articles = source.fetch()

    return []

class NewsSource:
    def __init__(self, name, alias, url, scrape):
        self.name = name
        self.alias = alias
        self.url = url
        self.scrape = scrape

    def fetch(self):
        return self.scrape(self.url)
         
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

def formatSnippets(article_snippets):
    out = "\n"

    for i, snippet in enumerate(article_snippets[1:5]):
        headline = snippet["headline"]
        out += "\033[1m" + str(i + 1) + ". " + headline + "\033[0m" + "\n\n"
    return out

def main():
    print("newsget v.0.0.1")
    
    print(
    """
Select a news source:

1. Canadian Broadcasting Corporation
2. New York Times
3. Hacker News
    """)

    source_option = promptIntOrPanic("Select: ")

    # Instantiate news sources
    cbc = NewsSource(name="Canadian Broadcasting Corporation", alias="CBC", url="https://www.cbc.ca/news", scrape=scrapeCBC)

    # Create dictionary of news sources
    sources = {
        1: cbc
    }

    news_source = sources[source_option]
    article_snippets = news_source.fetch()

    print(formatSnippets(article_snippets))
    
if __name__ == "__main__":
    main()
