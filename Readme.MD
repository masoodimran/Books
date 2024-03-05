# Books API

This project provides a RESTful API for managing a collection of books. It allows users to create, read, update, and delete book records. The API is built with FastAPI and uses a TestClient for testing purposes.

## Features

- **Create Books**: Add new books to the collection with details like title, author, and publication year.
- **Read Books**: Retrieve details of a specific book using its unique identifier.
- **Update Books**: Modify the details of an existing book.
- **Delete Books**: Remove a book from the collection.

## Installation

To set up the project environment, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python 3.8 or newer installed.
3. Install the required dependencies by running following command in the project directory:
    - `uv venv -p (pyenv which python) .venv`
    - `.\.venv\Scripts\activate`
    - `uv pip install -r .\requirements.in -r .\requirements-test.in`

## Running the Application

To run the application, execute the following command in the project root directory:
`uvicorn api.main:app --reload`

This will start the FastAPI application on `127.0.0.1` with the default port `8000`.

## Testing

The project includes tests for each API endpoint. To run the tests, navigate to the project root directory and execute:
`pytest`

Ensure all tests pass to confirm the API is functioning as expected.

## API Endpoints

The following endpoints are available:

- `POST /books`: Create a new book record.
- `GET /books/{book_id}`: Retrieve a book by its ID.
- `PUT /books/{book_id}`: Update the details of an existing book.
- `DELETE /books/{book_id}`: Delete a book from the collection.

For swagger, please use the link `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.