#!/bin/bash
# Script to start MLflow UI

echo "Starting MLflow UI..."
echo "Access at: http://localhost:5000"

# Start MLflow UI
mlflow ui --host 0.0.0.0 --port 5000
