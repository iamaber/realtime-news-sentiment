import streamlit as st
import requests

st.title("📰 Real-time News Sentiment Dashboard")
        
if st.button("Fetch News Sentiments"):
    response = requests.get("http://localhost:8000/")
    if response.status_code == 200:
        data = response.json()
        for item in data:
            sentiment = item.get('sentiment', {})
            label = sentiment.get('label', 'UNKNOWN')
            score = sentiment.get('score', 0.0)

            st.write(f"**Headline**: {item['headline']}")
            st.write(f"Sentiment: {label} ({score:.2f})")
            st.markdown("---")
    else:
        st.error("Failed to fetch data!")