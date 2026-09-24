# Phase 7 – Project Documentation

## VS Code Setup

1. Install Python 3.10 or newer.
2. Open the `LegalEase_Complete` folder in VS Code.
3. Open the integrated terminal.
4. Move into `05_Project_Development`.
5. Create a virtual environment.
6. Activate it.
7. Install requirements.
8. Copy `.env.example` to `.env`.
9. Add `GEMINI_API_KEY` if available.
10. Run FastAPI.
11. Open a second terminal and run Streamlit.

## Commands

```powershell
cd "05_Project_Development"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Terminal 1:
```powershell
cd backend
python -m uvicorn main:app --reload --port 8000
```

Terminal 2:
```powershell
cd frontend
python -m streamlit run app.py
```

Frontend: `http://localhost:8501`
Backend: `http://127.0.0.1:8000`
Swagger: `http://127.0.0.1:8000/docs`

## Troubleshooting

### PowerShell blocks activation
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then activate again.

### Backend not running
Make sure Terminal 1 shows Uvicorn running on port 8000.

### Gemini error
Check `GEMINI_API_KEY`, `.env` location, and `GEMINI_MODEL`. The local fallback still works without a key.

### Port conflict
Change `BACKEND_URL` in `.env` and run Uvicorn on the matching port.
