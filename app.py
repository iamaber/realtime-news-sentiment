import streamlit as st
import requests

st.title("📰 Real-time News Sentiment Dashboard")

if st.button("Fetch News Sentiments"):
    response = requests.get("http://localhost:8000/")
    if response.status_code == 200:
        data = response.json()
        for item in data:
            st.write(f"**Headline**: {item['headline']}")
            st.write(f"Sentiment: {item['sentiment']}")
            st.markdown("---")
    else:
        st.error("Failed to fetch data!")