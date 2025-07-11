import pytest

@pytest.fixture
def mock_data():
    return {
        "title": "Test Book",
        "author": "Test Author",
        "ISBN": "1234567890",
        "year": 2022
    }

def test_create_book_success(client, mock_data):
    response = client.post("/books", json=mock_data)
    assert response.status_code == 201
    assert response.json()["title"] == mock_data["title"]

def test_get_all_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_book(client, mock_data):
    response = client.put("/books/1", json=mock_data)
    assert response.status_code == 200
    assert response.json()["author"] == mock_data["author"]

def test_delete_book(client):
    response = client.delete("/books/1")
    assert response.status_code == 204

def test_create_book_invalid_input(client):
    response = client.post("/books", json={})
    assert response.status_code == 422

def test_get_book_not_found(client):
    response = client.get("/books/999")
    assert response.status_code == 404