"""
    dado 1 libro el resultado seria 8 euros
    dado 2 libros iguales el resultado seria 16 euros
    dado 2 libros diferentes el resultado seria 8€ * 2librosdiferentes * 0.95descuento = 15.2
dado 2 copias del primer libro y 1 copia del segundo -> 2 * 8 * 0,95 + 1 * 8 = 23.2
"""

from book import Book
from calculator import Calculator


def test_smoke():
    assert True


def test_given_1_book_price_should_be_8():
    book = Book(1, 'name1', 8)
    assert Calculator().calculate(*[book]) == 8


def test_given_2_books_price_should_be_16():
    first_book = Book(1, 'name1', 8)
    assert Calculator().calculate(*[first_book, first_book]) == 16


def test_given_3_books_price_should_be_24():
    first_book = Book(1, 'name1', 8)
    assert Calculator().calculate(*[first_book, first_book, first_book]) == 24


def test_given_2_different_books_should_be_15_2():
    first_book = Book(1, 'name1', 8)
    second_book = Book(2, 'name2', 8)
    assert Calculator().calculate(*[first_book, second_book]) == 15.2


def test_given_2_different_books_and_another_book_should_be_23_2():
    first_book = Book(1, 'name1', 8)
    second_book = Book(2, 'name2', 8)
    assert Calculator().calculate(*[first_book, first_book, second_book]) == 23.2


def test_given_3_different_books_and_another_book_should_be_29_6():
    first_book = Book(1, 'name1', 8)
    second_book = Book(2, 'name2', 8)
    third_book = Book(3, 'name3', 8)
    assert Calculator().calculate(*[first_book, first_book, second_book, third_book]) == 29.6


def test_another_should_be_51_2():
    """
    2 copies of the first book
    2 copies of the second book
    2 copies of the third book
    1 copy of the fourth book
    1 copy of the fifth book
    :return:
    """

    first_book = Book(1, 'name1', 8)
    second_book = Book(2, 'name2', 8)
    third_book = Book(3, 'name3', 8)
    fourth_book = Book(4, 'name4', 8)
    fifth_book = Book(5, 'name5', 8)
    assert Calculator().calculate(*[
        first_book,
        first_book,
        second_book,
        second_book,
        third_book,
        third_book,
        fourth_book,
        fifth_book,
    ]) == 51.2
