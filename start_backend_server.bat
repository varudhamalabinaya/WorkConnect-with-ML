@echo off
echo Starting WorkConnect Backend Server...
echo =====================================

cd backend
echo Current directory: %cd%
echo.

echo Checking Python version...
python --version
echo.

echo Installing/checking dependencies...
pip install -r requirements.txt
echo.

echo Starting Flask server...
echo Backend will be available at: http://localhost:5000
echo Health check: http://localhost:5000/health
echo API endpoints: http://localhost:5000/api/
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py