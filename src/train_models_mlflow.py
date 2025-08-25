"""
Train models with MLflow tracking
"""
import os
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import mlflow
import mlflow.sklearn
import mlflow.pyfunc
from datetime import datetime

def train_and_track_models():
    # Set MLflow tracking URI (local)
    mlflow.set_tracking_uri("file:./mlruns")
    
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split data (90% train, 10% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=42, stratify=y
    )
    
    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save test data and scaler
    os.makedirs('models', exist_ok=True)
    np.save('models/X_test.npy', X_test)
    np.save('models/y_test.npy', y_test)
    joblib.dump(scaler, 'models/scaler.pkl')
    
    models_info = []
    
    # 1. Random Forest Model
    with mlflow.start_run(run_name="Random_Forest_Iris"):
        print("Training Random Forest...")
        
        # Log parameters
        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)
        mlflow.log_param("test_size", 0.1)
        
        # Train model
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_model.fit(X_train_scaled, y_train)
        
        # Predict and evaluate
        rf_pred = rf_model.predict(X_test_scaled)
        rf_accuracy = accuracy_score(y_test, rf_pred)
        
        # Log metrics
        mlflow.log_metric("accuracy", rf_accuracy)
        mlflow.log_metric("train_samples", len(X_train))
        mlflow.log_metric("test_samples", len(X_test))
        
        # Log model
        mlflow.sklearn.log_model(
            sk_model=rf_model,
            artifact_path="model",
            registered_model_name="iris_random_forest"
        )
        
        # Save model locally
        joblib.dump(rf_model, 'models/random_forest_model.pkl')
        
        print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
        models_info.append({
            "name": "Random Forest",
            "accuracy": rf_accuracy,
            "run_id": mlflow.active_run().info.run_id
        })
    
    # 2. SVM Model
    with mlflow.start_run(run_name="SVM_Iris"):
        print("Training SVM...")
        
        # Log parameters
        mlflow.log_param("model_type", "SVM")
        mlflow.log_param("kernel", "rbf")
        mlflow.log_param("random_state", 42)
        mlflow.log_param("test_size", 0.1)
        
        # Train model
        svm_model = SVC(kernel='rbf', random_state=42, probability=True)
        svm_model.fit(X_train_scaled, y_train)
        
        # Predict and evaluate
        svm_pred = svm_model.predict(X_test_scaled)
        svm_accuracy = accuracy_score(y_test, svm_pred)
        
        # Log metrics
        mlflow.log_metric("accuracy", svm_accuracy)
        mlflow.log_metric("train_samples", len(X_train))
        mlflow.log_metric("test_samples", len(X_test))
        
        # Log model
        mlflow.sklearn.log_model(
            sk_model=svm_model,
            artifact_path="model",
            registered_model_name="iris_svm"
        )
        
        # Save model locally
        joblib.dump(svm_model, 'models/svm_model.pkl')
        
        print(f"SVM Accuracy: {svm_accuracy:.4f}")
        models_info.append({
            "name": "SVM",
            "accuracy": svm_accuracy,
            "run_id": mlflow.active_run().info.run_id
        })
    
    # Print summary
    print("\n" + "="*50)
    print("MODEL TRAINING SUMMARY")
    print("="*50)
    for model in models_info:
        print(f"{model['name']}: {model['accuracy']:.4f} (Run ID: {model['run_id']})")
    
    print(f"\nFiles saved:")
    print(f"- models/random_forest_model.pkl")
    print(f"- models/svm_model.pkl")
    print(f"- models/scaler.pkl")
    print(f"- models/X_test.npy, models/y_test.npy")
    print(f"\nMLflow UI: Run 'mlflow ui' to view experiments")

if __name__ == "__main__":
    train_and_track_models()
