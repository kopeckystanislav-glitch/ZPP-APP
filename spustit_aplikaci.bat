@echo off
echo ✅ Spoustím Streamlit aplikaci...
start cmd /k "streamlit run app.py"

timeout /t 5 >nul

echo 🌐 Spoustím ngrok tunel...
start cmd /k "ngrok http 8501"
