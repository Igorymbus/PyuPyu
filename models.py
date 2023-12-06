import sqlite3

class DatabaseManager:
    def __init__(self, db_name="bookstore.db"):
        self._conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self):
        with self._conn:
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')

            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Books (
                    book_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    publication_year INTEGER,
                    genre TEXT,
                    FOREIGN KEY (author) REFERENCES Authors(author),
                    FOREIGN KEY (genre) REFERENCES Genres(genre)
                )
            ''')

            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Authors (
                    author_id INTEGER PRIMARY KEY,
                    author TEXT NOT NULL UNIQUE
                )
            ''')

            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Genres (
                    genre_id INTEGER PRIMARY KEY,
                    genre TEXT NOT NULL UNIQUE
                )
            ''')

            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Roles (
                    role_id INTEGER PRIMARY KEY,
                    role_name TEXT NOT NULL UNIQUE
                )
            ''')
    def register_user(self, username, password):
        query = 'INSERT INTO Users (username, password) VALUES (?, ?)'
        params = (username, password)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Пользователь успешно зарегистрирован!")
        except sqlite3.IntegrityError:
            print("Пользователь с таким именем уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при регистрации: {str(e)}")
            pass

    def login_user(self, username, password):
        query = 'SELECT * FROM Users WHERE username=? AND password=?'
        params = (username, password)
        result = self._conn.execute(query, params).fetchone()
        if result:
            print(f"Добро пожаловать, {username}!")
        else:
            print("Неверные учетные данные. Пожалуйста, попробуйте снова.")
        pass

    def add_book(self, title, author, publication_year, genre):
        query = 'INSERT INTO Books (title, author, publication_year, genre) VALUES (?, ?, ?, ?)'
        params = (title, author, publication_year, genre)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Книга успешно добавлена!")
        except sqlite3.IntegrityError:
            print("Книга с таким названием уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении книги: {str(e)}")
        pass

    def delete_book(self, book_id):
        query = 'DELETE FROM Books WHERE book_id = ?'
        params = (book_id,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Книга успешно удалена!")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении книги: {str(e)}")

        pass

    def update_book_info(self, book_id, title, author, publication_year, genre):
        query = 'UPDATE Books SET title=?, author=?, publication_year=?, genre=? WHERE book_id=?'
        params = (title, author, publication_year, genre, book_id)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Информация о книге успешно обновлена!")
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении информации о книге: {str(e)}")
        pass

    def get_all_books(self):
        query = 'SELECT * FROM Books'
        return self._conn.execute(query).fetchall()
        pass

    def filter_books_by_genre(self, genre):
        query = 'SELECT * FROM Books WHERE genre = ?'
        params = (genre,)
        return self._conn.execute(query, params).fetchall()
        pass

    def add_author(self, author_name):
        query = 'INSERT INTO Authors (author) VALUES (?)'
        params = (author_name,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Автор успешно добавлен!")
        except sqlite3.IntegrityError:
            print("Автор с таким именем уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении автора: {str(e)}")
        pass

    def add_genre(self, genre_name):
        query = 'INSERT INTO Genres (genre) VALUES (?)'
        params = (genre_name,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Жанр успешно добавлен!")
        except sqlite3.IntegrityError:
            print("Жанр с таким названием уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении жанра: {str(e)}")
        pass

    def delete_user(self, user_id):
        query = 'DELETE FROM Users WHERE user_id = ?'
        params = (user_id,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Пользователь успешно удален!")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении пользователя: {str(e)}")
        pass
class DatabaseManager:
    def save_user(self, user):
        query = 'INSERT INTO Users (username, password) VALUES (?, ?)'
        params = (user.username, user.password)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Пользователь успешно сохранен в базе данных!")
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении пользователя: {str(e)}")

    def save_book(self, book):
        query = 'INSERT INTO Books (title, author, publication_year, genre) VALUES (?, ?, ?, ?)'
        params = (book.title, book.author, book.publication_year, book.genre)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Книга успешно сохранена в базе данных!")
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении книги: {str(e)}")

    def save_author(self, author):
        query = 'INSERT INTO Authors (author) VALUES (?)'
        params = (author.name,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Автор успешно сохранен в базе данных!")
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении автора: {str(e)}")

    def save_genre(self, genre):
        query = 'INSERT INTO Genres (genre) VALUES (?)'
        params = (genre.name,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Жанр успешно сохранен в базе данных!")
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении жанра: {str(e)}")

    def save_user(self, user):
        query = 'INSERT INTO Users (username, password) VALUES (?, ?)'
        params = (user.username, user.password)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Пользователь успешно сохранен в базе данных!")
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении пользователя: {str(e)}")
            print("Ошибка при сохранении пользователя. Пожалуйста, попробуйте снова.")