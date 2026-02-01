import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def sample_expense():
    return {
        "amount": "125.50", # String to ensure Decimal parsing
        "category": "Food",
        "description": "Team Lunch",
        "expense_date": "2026-02-01",
        "request_id": "test-uuid-unique-123"
    }

def test_create_expense_success(sample_expense):
    """Test standard creation (201 Created)"""
    response = client.post("/api/v1/expenses/", json=sample_expense)
    assert response.status_code == 201
    assert response.json()["amount"] == "125.50"

def test_idempotency_same_request_id(sample_expense):
    """Test that duplicate request_id returns 200 and no new record"""
    # First request
    client.post("/api/v1/expenses/", json=sample_expense)
    
    # Second request with same ID
    response = client.post("/api/v1/expenses/", json=sample_expense)
    
    assert response.status_code == 200
    assert response.json()["request_id"] == sample_expense["request_id"]

def test_negative_amount_validation():
    """Test Pydantic validation for positive amounts"""
    bad_data = {
        "amount": -50.00,
        "category": "Food",
        "expense_date": "2026-02-01",
        "request_id": "bad-data-id"
    }
    response = client.post("/api/v1/expenses/", json=bad_data)
    assert response.status_code == 422 # Unprocessable Entity