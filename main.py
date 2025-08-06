import subprocess
import sys
import time
import os
from pathlib import Path
import argparse


def run_backend():
    """Run the FastAPI backend server"""
    backend_dir = Path(__file__).parent / "backend"
    os.chdir(backend_dir)
    
    parent_dir = str(Path(__file__).parent)
    env = os.environ.copy()
    env['PYTHONPATH'] = parent_dir + ':' + env.get('PYTHONPATH', '')
    
    return subprocess.Popen([
        sys.executable, "-m", "uvicorn", "api:app", 
        "--reload", "--host", "0.0.0.0", "--port", "8000"
    ], env=env)


def run_frontend():
    """Run the Streamlit frontend"""
    frontend_dir = Path(__file__).parent / "frontend"
    return subprocess.Popen([
        sys.executable, "-m", "streamlit", "run", "app.py", 
        "--server.port", "8501", "--server.address", "0.0.0.0"
    ], cwd=frontend_dir)


def main():
    parser = argparse.ArgumentParser(description="Real-time News Sentiment Analysis")
    parser.add_argument("--mode", choices=["all", "backend", "frontend"], 
                       default="all", help="Run mode (default: all)")
    args = parser.parse_args()
    
    processes = []
    
    try:
        if args.mode in ["all", "backend"]:
            backend_process = run_backend()
            processes.append(backend_process)
            
            if args.mode == "all":
                time.sleep(3)
        
        if args.mode in ["all", "frontend"]:
            frontend_process = run_frontend()
            processes.append(frontend_process)
        
        for process in processes:
            process.wait()
            
    except KeyboardInterrupt:
        for process in processes:
            try:
                process.terminate()
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()


if __name__ == "__main__":
    main()
