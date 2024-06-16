import pytest
from main import BooksCollector


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
    premade_dict = {
        'Книга 1': 'Фантастика',
        'Книга 2': 'Ужасы',
        'Книга 3': 'Детективы',
        'Книга 4': 'Мультфильмы',
        'Книга 5': 'Комедии'
    }
    for book, genre in premade_dict.items():
        collection.add_new_book(book)
        collection.set_book_genre(book, genre)
    return collection
