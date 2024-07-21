import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_weather(client, monkeypatch):
    def mock_get_coordinates(city):
        return 51.509865, -0.118092  # Example coordinates for London
    monkeypatch.setattr('app.get_coordinates', mock_get_coordinates)

    rv = client.post('/weather', data={'city': 'London'})
    assert rv.status_code == 200
    assert b"Temperature" in rv.data