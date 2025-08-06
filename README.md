# Real-time News Sentiment Analysis Dashboard

This project is a real-time News Sentiment Analysis dashboard built with **FastAPI** (backend) and **Streamlit** (frontend). It fetches live news headlines, analyzes sentiment using Hugging Face Transformers, and visualizes sentiment distribution interactively.

## 🚀 Features

- 🔍 Real-time news headline fetching (RSS-based)
- 🤖 Sentiment analysis with Hugging Face pre-trained models
- 📊 Interactive sentiment pie chart (Positive/Negative)
- 🖥️ FastAPI-powered backend APIs
- 📈 Streamlit interactive dashboard frontend
- ⚡ Uses `uv` for ultra-fast dependency management (optional for local dev)
- 🏗️ Modular project structure with separate backend and frontend

## 📂 Project Structure

```
realtime-news-sentiment/
├── main.py                    # Main entry point - runs both backend and frontend
├── backend/                   # Backend API (FastAPI)
│   ├── __init__.py
│   ├── api.py                # FastAPI application
│   └── services/             # Business logic services
│       ├── __init__.py
│       ├── news_fetcher.py   # News headline fetching logic
│       └── sentiment.py     # Sentiment analysis logic
├── frontend/                 # Frontend dashboard (Streamlit)
│   ├── __init__.py
│   └── app.py               # Streamlit dashboard application
├── requirements.txt         # Python dependencies
├── pyproject.toml          # uv's dependency file
├── uv.lock                 # uv lock file
└── README.md               # Project documentation
```

## ⚙️ Installation & Running

### Quick Start (Run Everything)

1. **Clone the Repository**
    ```bash
    git clone https://github.com/iamaber/realtime-news-sentiment.git
    cd realtime-news-sentiment
    ```

2. **Install Dependencies**
    
    With uv (recommended):
    ```bash
    # Install uv if not installed
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Sync dependencies
    uv pip sync
    ```
    
    Or with pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Complete Application**
    ```bash
    python main.py
    ```
    This will start both backend and frontend automatically!
    
    - 📊 **Frontend Dashboard**: http://localhost:8501
    - 🔧 **Backend API**: http://localhost:8000
    - 📖 **API Documentation**: http://localhost:8000/docs

### Advanced Usage

Run components separately:

**Backend Only:**
```bash
python main.py --mode backend
```

**Frontend Only (requires backend running):**
```bash
python main.py --mode frontend
```

**Manual Setup:**
```bash
# Terminal 1 - Backend
cd backend
uvicorn api:app --reload --port 8000

# Terminal 2 - Frontend
cd frontend
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

- **Backend (FastAPI)**: 
  - Located in `/backend/` directory
  - Serves API endpoints to fetch live headlines and perform sentiment analysis
  - Modular services architecture with separate news fetching and sentiment analysis
  - Auto-generated API documentation at `/docs`

- **Frontend (Streamlit)**: 
  - Located in `/frontend/` directory
  - Visualizes data in an interactive dashboard with sentiment charts
  - Connects to backend API for real-time data

- **Sentiment Analysis**: Uses Hugging Face pre-trained models (e.g., `distilbert-base-uncased-finetuned-sst-2-english`)

- **Main Runner**: Single `main.py` file orchestrates both backend and frontend services

## 🧑‍💻 Development Tips

- **Project Structure**: Modular design with separate backend and frontend directories
- **Single Command Run**: Use `python main.py` to run everything at once
- **Development Mode**: Use `python main.py --mode backend` or `--mode frontend` for isolated development
- **Fast Dependencies**: Use `uv` for ultra-fast dependency management during development
- **API Testing**: Visit http://localhost:8000/docs for interactive API documentation
- **Hot Reload**: Both backend (uvicorn) and frontend (streamlit) support hot reloading during development

## 📝 License

MIT License
