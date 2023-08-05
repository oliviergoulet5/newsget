from news import NewsSource
import news
from output_utils import promptIntOrPanic, paginatedPrompt
import subprocess

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
    cbc = NewsSource(name="Canadian Broadcasting Corporation", alias="CBC", url="https://www.cbc.ca/news", scrape=news.scrapeCBC)

    # Create dictionary of news sources
    sources = {
        1: cbc
    }

    news_source = sources[source_option]
    article_snippets = news_source.fetch()
    
    snippetOptionMapper = lambda snippet : { "text": snippet["headline"], "value": snippet }
    options = list(map(snippetOptionMapper, article_snippets))
    result = paginatedPrompt(options)

    news_source.read(result)

    subprocess.run(
        ["less"], 
        input=bytes(news_source.read(result), 'utf-8')
    )

if __name__ == "__main__":
    main()

