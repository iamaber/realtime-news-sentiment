import feedparser

def fetch_headlines(url="https://feedparser.readthedocs.io/en/latest/examples/atom10.xml"):
    feed = feedparser.parse(url)
    headlines = [entry['title'] for entry in feed['entries']]
    return headlines

print(fetch_headlines())