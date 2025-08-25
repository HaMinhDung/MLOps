@echo off
REM Script to start MLflow UI

echo Starting MLflow UI...
echo Access at: http://localhost:5000
echo.
echo Press Ctrl+C to stop
echo.

REM Start MLflow UI with Python module (more reliable)
python -m mlflow ui --host 0.0.0.0 --port 5000

pause
