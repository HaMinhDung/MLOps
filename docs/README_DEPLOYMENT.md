# Iris ML API với MLflow Tracking và Docker

## 📋 Mô tả Project
Project này bao gồm:
- 2 mô hình ML (Random Forest & SVM) để phân loại hoa Iris
- MLflow để tracking experiments
- FastAPI để tạo REST API endpoints
- Docker để containerization
- Postman collection để testing

## 🚀 Hướng dẫn Setup và Deployment

### Bước 1: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 2: Train models với MLflow tracking
```bash
python train_models_mlflow.py
```
Lệnh này sẽ:
- Train 2 models (Random Forest & SVM)
- Log experiments vào MLflow
- Lưu models (.pkl files)
- Tạo test data

### Bước 3: Khởi động MLflow UI (optional)
```bash
mlflow ui
```
Truy cập: http://localhost:5000 để xem experiments

### Bước 4: Chạy FastAPI locally
```bash
# Cách 1: Chạy trực tiếp
python app.py

# Cách 2: Dùng uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
API sẽ chạy tại: http://localhost:8000

### Bước 5: Test API
```bash
# Test bằng script Python
python test_api.py

# Hoặc truy cập Swagger UI
# http://localhost:8000/docs
```

## 🐳 Docker Deployment

### Build và run với Docker
```bash
# Build image
docker build -t iris-api .

# Run container
docker run -p 8000:8000 iris-api
```

### Sử dụng Docker Compose (Recommended)
```bash
# Khởi động cả API và MLflow
docker-compose up -d

# Xem logs
docker-compose logs -f

# Dừng services
docker-compose down
```

Services:
- **Iris API**: http://localhost:8000
- **MLflow UI**: http://localhost:5000

## 📮 Testing với Postman

### Cách 1: Import collection
1. Mở Postman
2. Import file: `Iris_API.postman_collection.json`
3. Set environment variable: `BASE_URL = http://localhost:8000`

### Cách 2: Manual testing
```bash
# Health check
GET http://localhost:8000/

# Models info
GET http://localhost:8000/models/info

# Predict with Random Forest
POST http://localhost:8000/predict/random_forest
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

# Predict with SVM
POST http://localhost:8000/predict/svm
{
  "sepal_length": 6.3,
  "sepal_width": 3.3,
  "petal_length": 6.0,
  "petal_width": 2.5
}

# Predict with both models
POST http://localhost:8000/predict/both
{
  "sepal_length": 5.9,
  "sepal_width": 3.0,
  "petal_length": 5.1,
  "petal_width": 1.8
}
```

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/models/info` | Get models information |
| POST | `/predict/random_forest` | Predict with Random Forest |
| POST | `/predict/svm` | Predict with SVM |
| POST | `/predict/both` | Predict with both models |

## 📁 Cấu trúc Project
```
├── app.py                          # FastAPI application
├── train_models_mlflow.py          # Training với MLflow
├── test_api.py                     # Test script
├── Dockerfile                      # Docker configuration
├── docker-compose.yml              # Docker Compose
├── requirements.txt                # Dependencies
├── Iris_API.postman_collection.json # Postman collection
├── mlruns/                         # MLflow experiments
├── *.pkl                          # Trained models
└── README_DEPLOYMENT.md            # Hướng dẫn này
```

## 🔧 Troubleshooting

### Lỗi phổ biến:
1. **Models not found**: Chạy `python train_models_mlflow.py` trước
2. **Port đã sử dụng**: Thay đổi port trong docker-compose.yml
3. **Permission denied**: Chạy với admin/sudo

### Logs:
```bash
# Docker logs
docker-compose logs iris-api
docker-compose logs mlflow

# API logs
tail -f app.log
```

## 🚀 Next Steps
- Thêm authentication/authorization
- Implement model versioning
- Add monitoring và alerting
- Scale với Kubernetes
