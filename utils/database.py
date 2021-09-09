from typing import List, Tuple

from utils.db_connect import DatabaseConnection

Book = Tuple[int, str, str, int]


def create_book_table():
    with DatabaseConnection('data.db') as cursor:

        # SQLite automatically makes `integer primary key` row auto-incrementing (see link in further reading)
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books (id integer primary key, name text, author text, read integer default 0)')


def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
    return books


def insert_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as cursor:

        cursor.execute(
            'INSERT INTO books (name, author) VALUES (?, ?)', (name, author))


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('DELETE FROM books WHERE name=?', (name,))
