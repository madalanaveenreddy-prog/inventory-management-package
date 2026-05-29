
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, get_db
from main import app

# Day 5: Test isolation using an in-memory test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_inventory_service.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Day 4: Pytest Fixture for clean state arrangement (Arrange-Act-Assert)
@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    
    def _get_test_db():
        try:
            yield db
        finally:
            db.close()
            
    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as test_client:
        yield test_client
        
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()

# Day 3: Basic Functional Testing & Day 4 Arrange-Act-Assert
def test_create_and_read_item(client):
    # Arrange
    payload = {"name": "Mechanical Keyboard", "price": 89.99, "quantity": 45}
    
    # Act
    response = client.post("/items/", json=payload)
    assert response.status_code == 201
    created_item = response.json()
    
    # Assert
    assert created_item["name"] == "Mechanical Keyboard"
    assert created_item["id"] is not None

    # Act (Read back)
    get_response = client.get(f"/items/{created_item['id']}")
    # Assert
    assert get_response.status_code == 200
    assert get_response.json()["price"] == 89.99

# Day 5: Parametrization & Advanced Validation Error Edge Cases
@pytest.mark.parametrize(
    "invalid_payload, expected_status",
    [
        ({"name": "", "price": 10.0, "quantity": 5}, 422),       # Empty name fails validation
        ({"name": "Item A", "price": -2.5, "quantity": 5}, 422),   # Negative price fails validation
        ({"name": "Item B", "price": 10.0, "quantity": -1}, 422),  # Negative quantity fails validation
    ]
)
def test_validation_errors(client, invalid_payload, expected_status):
    response = client.post("/items/", json=invalid_payload)
    assert response.status_code == expected_status