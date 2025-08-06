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
    uv sync
    ```
    
    Or with pip:
    ```bash
    # Create virtual environment
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    
    # Install dependencies
    pip install -r requirements.txt
    ```

3. **Run the Complete Application**
    
    With uv:
    ```bash
    uv run python main.py
    ```
    
    Or with activated virtual environment:
    ```bash
    # If using pip, make sure virtual environment is activated
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
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
# With uv
uv run python main.py --mode backend

# With virtual environment
source .venv/bin/activate
python main.py --mode backend
```

**Frontend Only (requires backend running):**
```bash
# With uv
uv run python main.py --mode frontend

# With virtual environment
source .venv/bin/activate
python main.py --mode frontend
```

**Manual Setup:**
```bash
# Terminal 1 - Backend
cd backend
# With uv
uv run uvicorn api:app --reload --port 8000
# Or with venv: source ../.venv/bin/activate && uvicorn api:app --reload --port 8000

# Terminal 2 - Frontend
cd frontend
# With uv
uv run streamlit run app.py
# Or with venv: source ../.venv/bin/activate && streamlit run app.py
```

## 📝 Technologies Used

- Python 3.12+
- FastAPI
- Streamlit
- Transformers (Hugging Face)
- PyTorch
- Feedparser
- Plotly
- Pandas
- Requests
- uv (package manager)

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
- **Single Command Run**: Use `uv run python main.py` or `python main.py` (with activated venv) to run everything at once
- **Development Mode**: Use `--mode backend` or `--mode frontend` flags for isolated development
- **Package Management**: Use `uv` for ultra-fast dependency management during development
- **Virtual Environment**: Project uses `.venv` directory for isolated dependencies
- **API Testing**: Visit http://localhost:8000/docs for interactive API documentation
- **Hot Reload**: Both backend (uvicorn) and frontend (streamlit) support hot reloading during development
- **Dependencies**: Optimized to include only essential packages (removed unused httpx, mangum, python-dotenv)

## 🔧 Troubleshooting

**Module Not Found Errors:**
- Make sure you're running commands with `uv run` or have activated the virtual environment
- Verify dependencies are installed: `uv sync` or `pip install -r requirements.txt`

**Port Already in Use:**
- Backend runs on port 8000, frontend on port 8501
- Kill existing processes: `pkill -f uvicorn` or `pkill -f streamlit`

**Model Download Issues:**
- First run downloads Hugging Face models (~268MB)
- Ensure stable internet connection for initial setup

**Virtual Environment Issues:**
- For uv: Run `uv sync` to recreate environment
- For pip: Delete `.venv` folder and recreate with `python3 -m venv .venv`

## 📝 License

MIT License
