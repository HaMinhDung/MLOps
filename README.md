# 🌸 Iris Classification ML API

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![MLflow](https://img.shields.io/badge/MLflow-2.8+-orange.svg)](https://mlflow.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)

A production-ready Machine Learning API for Iris flower classification using **Random Forest** and **SVM** models with **MLflow tracking** and **Docker deployment**.

## 🚀 Features

- **🧠 Dual ML Models**: Random Forest & SVM classifiers
- **📊 MLflow Integration**: Complete experiment tracking and model registry
- **🚀 FastAPI Backend**: High-performance REST API with automatic documentation
- **🐳 Docker Ready**: Full containerization with Docker Compose
- **📮 Testing Suite**: Comprehensive API testing with Postman collection
- **📚 Documentation**: Complete API documentation with Swagger UI

## 🏗️ Project Structure

```
iris-ml-api/
├── 📁 src/
│   ├── app.py                    # FastAPI application
│   └── train_models_mlflow.py    # Model training with MLflow
├── 📁 tests/
│   └── test_api.py              # API test suite
├── 📁 docs/
│   └── README_DEPLOYMENT.md     # Deployment guide
├── 📁 scripts/
│   └── start_mlflow.sh          # MLflow startup script
├── 🐳 docker-compose.yml        # Multi-service Docker setup
├── 🐳 Dockerfile               # API container definition
├── 📦 requirements.txt          # Python dependencies
├── 📮 Iris_API.postman_collection.json  # Postman test collection
└── 📄 README.md                # This file
```

## 🛠️ Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- Postman (optional, for testing)

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd iris-ml-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Train Models
```bash
python src/train_models_mlflow.py
```

### 3. Run with Docker (Recommended)
```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps
```

### 4. Access Services
- **API Swagger UI**: http://localhost:8000/docs
- **MLflow UI**: http://localhost:5000
- **API Health**: http://localhost:8000/

## 📊 API Endpoints

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| `GET` | `/` | Health check | `{"status": "healthy"}` |
| `GET` | `/models/info` | Model information | Model details & features |
| `POST` | `/predict/random_forest` | Random Forest prediction | Iris classification |
| `POST` | `/predict/svm` | SVM prediction | Iris classification |
| `POST` | `/predict/both` | Both models prediction | Compare results |

### Example Request
```json
POST /predict/random_forest
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Example Response
```json
{
  "model_name": "Random Forest",
  "predicted_class": "setosa",
  "predicted_class_id": 0,
  "confidence": 1.0,
  "probabilities": {
    "setosa": 1.0,
    "versicolor": 0.0,
    "virginica": 0.0
  }
}
```

## 🧪 Testing

### Python Test Suite
```bash
python tests/test_api.py
```

### Postman Testing
1. Import `Iris_API.postman_collection.json` into Postman
2. Set environment variable: `BASE_URL = http://localhost:8000`
3. Run the collection tests

### Manual Testing
- **Swagger UI**: http://localhost:8000/docs
- **cURL**: See examples in `docs/README_DEPLOYMENT.md`

## 📈 MLflow Tracking

The project includes comprehensive experiment tracking:

- **Experiments**: Model training runs with parameters and metrics
- **Model Registry**: Versioned model artifacts
- **Metrics**: Accuracy, precision, recall for both models
- **Artifacts**: Trained models, scalers, and metadata

Access MLflow UI at http://localhost:5000 to explore experiments and compare models.

## 🐳 Docker Deployment

### Production Deployment
```bash
# Build and deploy
docker-compose up -d

# Scale API service
docker-compose up -d --scale iris-api=3

# View logs
docker-compose logs -f iris-api

# Stop services
docker-compose down
```

### Development Mode
```bash
# Run API locally
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000

# Run MLflow UI
mlflow ui --host 0.0.0.0 --port 5000
```

## 📚 Model Information

### Dataset
- **Source**: Iris flower dataset (sklearn.datasets)
- **Features**: 4 numerical features (sepal & petal dimensions)
- **Classes**: 3 species (setosa, versicolor, virginica)
- **Split**: 90% training, 10% testing

### Models
1. **Random Forest**
   - 100 estimators
   - Accuracy: ~93%
   - Fast inference

2. **Support Vector Machine**
   - RBF kernel
   - Probability estimates enabled
   - Accuracy: ~93%

Both models use StandardScaler for feature normalization.

## 🔧 Configuration

### Environment Variables
```bash
PYTHONPATH=/app          # Python module path
MLFLOW_TRACKING_URI=./mlruns  # MLflow storage
```

### Model Files
- Models are saved as `.pkl` files
- Scaler is saved separately
- Test data preserved for validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and test thoroughly
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

**Port already in use**
```bash
# Check what's using the port
netstat -ano | findstr :8000
# Kill the process or change port in docker-compose.yml
```

**Models not found**
```bash
# Retrain models
python src/train_models_mlflow.py
```

**Docker build fails**
```bash
# Clean Docker cache
docker system prune -a
# Rebuild
docker-compose build --no-cache
```

### Getting Help
- Check `docs/README_DEPLOYMENT.md` for detailed deployment guide
- Review API documentation at http://localhost:8000/docs
- Examine logs: `docker-compose logs iris-api`

---

## 🎯 Next Steps

- [ ] Add authentication & authorization
- [ ] Implement model versioning API
- [ ] Add monitoring & alerting
- [ ] Create CI/CD pipeline
- [ ] Add more ML models
- [ ] Implement A/B testing

---

**⭐ Star this repo if it helped you!**
