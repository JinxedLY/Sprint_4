import pytest
from main import BooksCollector
from test_data import test_books_data


@pytest.fixture
def collection():
    collection = BooksCollector()
    return collection


@pytest.fixture
def default_book():
    default_book = 'Книга'
    return default_book


@pytest.fixture
def premade_collection_of_5_books(collection):
    for book, genre in test_books_data.items():
        collection.add_new_book(book)
        collection.set_book_genre(book, genre)
    return collection
