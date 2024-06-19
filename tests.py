import pytest
from test_data import test_books_data

class TestBooksCollector:
    def test_add_new_book_two_entries_add_two_books(self, collection):
        collection.add_new_book('Книга 1')
        collection.add_new_book('Книга 2')
        assert len(collection.get_books_genre()) == 2

    @pytest.mark.parametrize('book', ['1' * 0, '1' * 41])
    def test_add_new_book_zero_or_more_than_40_length_not_added(self, book, collection):
        collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 0

    def test_add_new_book_valid_entry_has_no_genre(self, collection, default_book):
        book_value = default_book
        collection.add_new_book(book_value)
        assert collection.get_book_genre(book_value) == ''

    def test_add_new_book_duplicate_books_one_book_added(self, collection, default_book):
        collection.add_new_book(default_book)
        collection.add_new_book(default_book)
        assert len(collection.get_books_genre()) == 1

    def test_set_book_genre_valid_data_genre_applied(self, collection, default_book):
        collection.add_new_book(default_book)
        collection.set_book_genre(default_book, 'Фантастика')
        assert collection.get_book_genre(default_book) == 'Фантастика'

    def test_set_book_genre_invalid_book_not_applied(self, collection, default_book):
        collection.set_book_genre(default_book, 'Фантастика')
        assert collection.get_book_genre(default_book) is None

    def test_set_book_genre_invalid_genre_not_applied(self, collection, default_book):
        collection.add_new_book(default_book)
        collection.set_book_genre(default_book, 'Жанр')
        assert collection.get_book_genre(default_book) == ''

    def test_get_books_with_specific_genre_valid_genre_returns_books_in_genre(self, premade_collection_of_5_books):
        assert premade_collection_of_5_books.get_books_with_specific_genre('Фантастика') == ['Книга 1']

    def test_get_books_genre_no_input_returns_empty(self, collection):
        assert collection.get_books_genre() == {}

    def test_get_books_genre_five_books_returns_dict_of_five(self, premade_collection_of_5_books):
        assert premade_collection_of_5_books.get_books_genre() == test_books_data

    def test_get_books_for_children_five_books_returns_no_spookies_or_detectives(self, premade_collection_of_5_books):
        assert premade_collection_of_5_books.get_books_for_children() == ['Книга 1', 'Книга 4', 'Книга 5']

    def test_add_book_in_favorites_single_book_added_successfully(self, collection, default_book):
        collection.add_new_book(default_book)
        collection.add_book_in_favorites(default_book)
        assert len(collection.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_single_book_deleted_successfully(self, collection, default_book):
        collection.add_new_book(default_book)
        collection.add_book_in_favorites(default_book)
        collection.delete_book_from_favorites(default_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_single_book_returns_list_with_single_book(self, collection, default_book):
        collection.add_new_book(default_book)
        collection.add_book_in_favorites(default_book)
        assert len(collection.get_list_of_favorites_books()) == 1
