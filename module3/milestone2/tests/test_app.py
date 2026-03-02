import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_success(client):
    response = client.post('/predict', json={"features": [1, 2, 3, 4]})
    assert response.status_code == 200
    assert "prediction" in response.get_json()

def test_predict_missing_features(client):
    response = client.post('/predict', json={"wrong_key": [1, 2]})
    assert response.status_code == 400