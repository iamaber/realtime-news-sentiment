from fastapi import FastAPI
from news_fetcher import fetch_headlines
from sentiment import analyze_sentiment

app = FastAPI()

@app.get("/news-sentiment")
def get_news_sentiment():
    headlines = fetch_headlines()
    sentiments = analyze_sentiment(headlines)
    results = [{"headline": h, "sentiment": s} for h, s in zip(headlines, sentiments)]
    return results
