import feedparser

def fetch_headlines(urls=None):
    urls = [
        "https://news.google.com/rss",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://www.bbc.co.uk/feeds/rss/news/world/rss.xml"
        "https://moxie.foxnews.com/google-publisher/latest.xml",
        "https://www.cnbc.com/id/100003114/device/rss/rss.html",
        "https://www.aljazeera.com/xml/rss/all.xml", 
        "https://news.yahoo.com/rss/mostviewed",
        "http://rss.cnn.com/rss/edition.rss"
    ]
    all_headlines = []
    for url in urls:
        feed = feedparser.parse(url)
        headlines = [entry['title'] for entry in feed.get('entries', [])]
        all_headlines.extend(headlines)
        all_headlines = list(set(all_headlines))  # Remove duplicates
    
    return all_headlines