import feedparser

def fetch_headlines(url="http://rss.cnn.com/rss/cnn_topstories.rss"):
    feed = feedparser.parse(url)
    headlines = [entry['title'] for entry in feed['entries']]
    return headlines