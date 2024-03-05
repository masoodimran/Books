from fastapi.testclient import TestClient
from api.main import app
from uuid import UUID

client = TestClient(app)

def test_create_read_book():
    # Create a book without specifying an ID
    response = client.post("/books", json={"title": "Test Book", "author": "Test Author", "publication_year": 2021})
    assert response.status_code == 201, response.text  # Adding response.text helps debug the actual error message
    data = response.json()
    assert 'id' in data, "Response JSON does not include 'id' key"
    assert UUID(data["id"], version=4)
    book_id = data["id"]
    # Assuming the response structure matches the expected format
    assert "title" in data and data["title"] == "Test Book"
    assert "author" in data and data["author"] == "Test Author"
    assert "publication_year" in data and data["publication_year"] == 2021

    # Read the book using the UUID
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    read_data = response.json()
    assert read_data == data, "Read data does not match created data"

def test_update_book():
    # Create a book first
    response = client.post("/books", json={"title": "Old Title", "author": "Test Author", "publication_year": 2020})
    book_id = response.json()["id"]

    # Update the book
    response = client.put(f"/books/{book_id}", json={"id": book_id, "title": "New Title", "author": "Test Author", "publication_year": 2020})
    assert response.status_code == 200
    assert response.json() == {"id": book_id, "title": "New Title", "author": "Test Author", "publication_year": 2020}

def test_delete_book():
    # Create a book first
    response = client.post("/books", json={"title": "Book to Delete", "author": "Test Author", "publication_year": 2022})
    book_id = response.json()["id"]

    # Delete the book
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 204

    # Try to read the deleted book
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 404

