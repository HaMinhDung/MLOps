"""
Test script for API endpoints
Can be used to test before using Postman
"""
import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_models_info():
    """Test models info endpoint"""
    print("\nTesting models info endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/models/info")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_prediction(model_endpoint, sample_data):
    """Test prediction endpoint"""
    print(f"\nTesting {model_endpoint} endpoint...")
    try:
        response = requests.post(
            f"{BASE_URL}/predict/{model_endpoint}",
            json=sample_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_both_models(sample_data):
    """Test both models endpoint"""
    print(f"\nTesting both models endpoint...")
    try:
        response = requests.post(
            f"{BASE_URL}/predict/both",
            json=sample_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    # Sample test data (typical Iris setosa)
    sample_data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    
    print("="*50)
    print("IRIS API TESTING")
    print("="*50)
    
    # Test all endpoints
    tests = [
        ("Health Check", lambda: test_health()),
        ("Models Info", lambda: test_models_info()),
        ("Random Forest Prediction", lambda: test_prediction("random_forest", sample_data)),
        ("SVM Prediction", lambda: test_prediction("svm", sample_data)),
        ("Both Models Prediction", lambda: test_both_models(sample_data)),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'-'*30}")
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print(f"{'='*50}")
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name}: {status}")

if __name__ == "__main__":
    main()
