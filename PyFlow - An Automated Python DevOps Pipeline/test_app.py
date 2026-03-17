import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the homepage returns 200 OK and correct JSON"""
    response = client.get('/')
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['status'] == "online"
