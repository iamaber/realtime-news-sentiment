from transformers import pipeline
from news_fetcher import fetch_headlines
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(texts):
    return sentiment_model(texts)


list_news = fetch_headlines()
print(list_news[1])
print(analyze_sentiment(list_news[1]))