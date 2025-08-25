"""
FastAPI application for Iris prediction models
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import mlflow
import mlflow.sklearn
from typing import List, Dict, Any
import os

# Initialize FastAPI app
app = FastAPI(
    title="Iris Classification API",
    description="API for predicting Iris flower species using Random Forest and SVM models",
    version="1.0.0"
)

# Pydantic models for request/response
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    model_name: str
    predicted_class: str
    predicted_class_id: int
    confidence: float
    probabilities: Dict[str, float]

class HealthResponse(BaseModel):
    status: str
    models_loaded: List[str]

# Global variables for models
models = {}
scaler = None
class_names = ['setosa', 'versicolor', 'virginica']

def load_models():
    """Load trained models and scaler"""
    global models, scaler
    
    try:
        # Load scaler
        if os.path.exists('models/scaler.pkl'):
            scaler = joblib.load('models/scaler.pkl')
            print("✓ Scaler loaded successfully")
        
        # Load Random Forest model
        if os.path.exists('models/random_forest_model.pkl'):
            models['random_forest'] = joblib.load('models/random_forest_model.pkl')
            print("✓ Random Forest model loaded successfully")
        
        # Load SVM model
        if os.path.exists('models/svm_model.pkl'):
            models['svm'] = joblib.load('models/svm_model.pkl')
            print("✓ SVM model loaded successfully")
            
        if not models:
            raise Exception("No models found! Please train models first.")
            
    except Exception as e:
        print(f"Error loading models: {e}")
        raise e

# Load models on startup
@app.on_event("startup")
async def startup_event():
    load_models()

@app.get("/", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        models_loaded=list(models.keys())
    )

@app.post("/predict/random_forest", response_model=PredictionResponse)
async def predict_random_forest(features: IrisFeatures):
    """Predict using Random Forest model"""
    if 'random_forest' not in models:
        raise HTTPException(status_code=503, detail="Random Forest model not loaded")
    
    return make_prediction(features, 'random_forest', "Random Forest")

@app.post("/predict/svm", response_model=PredictionResponse)
async def predict_svm(features: IrisFeatures):
    """Predict using SVM model"""
    if 'svm' not in models:
        raise HTTPException(status_code=503, detail="SVM model not loaded")
    
    return make_prediction(features, 'svm', "SVM")

@app.post("/predict/both", response_model=List[PredictionResponse])
async def predict_both_models(features: IrisFeatures):
    """Predict using both models"""
    results = []
    
    if 'random_forest' in models:
        results.append(make_prediction(features, 'random_forest', "Random Forest"))
    
    if 'svm' in models:
        results.append(make_prediction(features, 'svm', "SVM"))
    
    if not results:
        raise HTTPException(status_code=503, detail="No models loaded")
    
    return results

def make_prediction(features: IrisFeatures, model_key: str, model_name: str) -> PredictionResponse:
    """Make prediction using specified model"""
    try:
        # Prepare input data
        input_data = np.array([[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]])
        
        # Scale features
        if scaler is not None:
            input_data = scaler.transform(input_data)
        
        # Get model
        model = models[model_key]
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        
        # Prepare response
        prob_dict = {class_names[i]: float(prob) for i, prob in enumerate(probabilities)}
        confidence = float(max(probabilities))
        
        return PredictionResponse(
            model_name=model_name,
            predicted_class=class_names[prediction],
            predicted_class_id=int(prediction),
            confidence=confidence,
            probabilities=prob_dict
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/models/info")
async def get_models_info():
    """Get information about loaded models"""
    if not models:
        raise HTTPException(status_code=503, detail="No models loaded")
    
    info = {
        "available_models": list(models.keys()),
        "class_names": class_names,
        "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
        "scaler_loaded": scaler is not None
    }
    return info

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
