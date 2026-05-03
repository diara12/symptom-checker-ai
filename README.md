# symptom-checker-ai
This project aims to develop an AI-based symptom checker that takes user-reported symptoms as input and predicts the most likely medical condition. The system is intended for preliminary health assessment only, helping users decide whether they should seek professional medical attention.

## Run With Anaconda

1. Open Anaconda Prompt and go to the project folder.

```powershell
cd "d:\ML COURSE - SKYREK\Final Project\symptom-checker-ai"
```

2. Create and activate a new environment.

```powershell
conda create -n symptom-checker python=3.10 -y
conda activate symptom-checker
```

3. Install the backend dependencies.

```powershell
pip install -r backend\requirements.txt
```

4. Start the Flask API.

```powershell
python backend\app.py
```

5. Open `frontend\index.html` in your browser after the API is running.

If you want to serve the frontend locally instead of opening the file directly, you can use any simple static server, but the page will work as long as the backend is running on `http://127.0.0.1:5000`.
