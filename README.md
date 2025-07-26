# Real-time News Sentiment Analysis Dashboard

This project is a real-time News Sentiment Analysis dashboard built with **FastAPI** (backend) and **Streamlit** (frontend). It fetches live news headlines, analyzes sentiment using Hugging Face Transformers, and visualizes sentiment distribution interactively.

## 🚀 Features

- 🔍 Real-time news headline fetching (RSS-based)
- 🤖 Sentiment analysis with Hugging Face pre-trained models
- 📊 Interactive sentiment pie chart (Positive/Negative)
- 🖥️ FastAPI-powered backend APIs
- 📈 Streamlit interactive dashboard frontend
- ⚡ Uses `uv` for ultra-fast dependency management (optional for local dev)

## 📂 Project Structure

```
.
├── app.py             # Streamlit frontend dashboard
├── main.py            # FastAPI backend API
├── news_fetcher.py    # News headline fetching logic
├── sentiment.py       # Sentiment analysis logic
├── requirements.txt   # Python dependencies
├── pyproject.toml     # uv's dependency file
└── README.md          # Project documentation
```

## ⚙️ Installation & Running (Locally with uv)

1. **Clone the Repository**
    ```bash
    git clone https://github.com/iamaber/realtime-news-sentiment.git
    cd realtime-news-sentiment
    ```

2. **Install uv (if not installed)**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

3. **Sync Dependencies**
    ```bash
    uv pip sync
    ```

4. **Run FastAPI (Backend)**
    ```bash
    uvicorn main:app --reload --port 8000
    ```
    Backend API: [http://localhost:8000](http://localhost:8000)

5. **Run Streamlit (Frontend)**
    Open a new terminal and run:
    ```bash
    streamlit run app.py
    ```

## 📝 Technologies Used

- Python 3.12
- FastAPI
- Streamlit
- Transformers (Hugging Face)
- PyTorch
- Feedparser
- Plotly
- uv

## 🛠 How It Works

- **FastAPI Backend**: Serves API endpoints to fetch live headlines and perform sentiment analysis.
- **Streamlit Frontend**: Visualizes data in an interactive dashboard with sentiment charts.
- **Sentiment Analysis**: Uses Hugging Face pre-trained models (e.g., `distilbert-base-uncased-finetuned-sst-2-english`).
- **Dashboard**: Displays sentiment distribution (pie chart) and color-coded sentiment labels for each headline.

## 🧑‍💻 Development Tips

- Use `uv` for fast dependency management during development.
- Run `uv pip compile > requirements.txt` to update dependencies.
- For production Docker builds, dependencies are installed via pip using `requirements.txt`.

## 📝 License

MIT License
