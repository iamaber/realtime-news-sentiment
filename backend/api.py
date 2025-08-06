from fastapi import FastAPI
from services.news_fetcher import fetch_headlines
from services.sentiment import analyze_sentiment

app = FastAPI(title="News Sentiment Analysis API", version="1.0.0")

@app.get("/")
def get_news_sentiment():
    """Fetch latest news headlines and analyze their sentiment"""
    headlines = fetch_headlines()
    sentiments = analyze_sentiment(headlines)
    results = [{"headline": h, "sentiment": s} for h, s in zip(headlines, sentiments)]
    return results

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
