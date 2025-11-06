@echo off
echo Starting WorkConnect Backend...
cd backend

echo Testing MongoDB connection...
python test_mongo.py

if %ERRORLEVEL% EQU 0 (
    echo MongoDB connection successful, starting full backend...
    python start.py
) else (
    echo MongoDB connection failed, starting simple backend...
    python simple_app.py
)

pause