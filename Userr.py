import sqlite3
class Client(User):
    def register(self, username, password):
        query = 'INSERT INTO Users (username, password, role_id) VALUES (?, ?, ?)'
        params = (username, password, 1)  # ID роли клиента
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Вы успешно зарегистрировались как клиент!")
        except sqlite3.IntegrityError:
            print("Пользователь с таким именем уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при регистрации: {str(e)}")

    def login(self, username, password):
        query = 'SELECT * FROM Users WHERE username=? AND password=? AND role_id=?'
        params = (username, password, 1)  # ID роли клиента
        result = self._conn.execute(query, params).fetchone()
        if result:
            print("Добро пожаловать, клиент!")
        else:
            print("Неверные учетные данные. Пожалуйста, попробуйте снова.")

class Employee(User):
    def register(self, username, password):
        query = 'INSERT INTO Users (username, password, role_id) VALUES (?, ?, ?)'
        params = (username, password, 2)  # ID роли сотрудника
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Вы успешно зарегистрировались как сотрудник!")
        except sqlite3.IntegrityError:
            print("Пользователь с таким именем уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при регистрации: {str(e)}")

    def login(self, username, password):
        query = 'SELECT * FROM Users WHERE username=? AND password=? AND role_id=?'
        params = (username, password, 2)  # ID роли сотрудника
        result = self._conn.execute(query, params).fetchone()
        if result:
            print("Добро пожаловать, сотрудник!")
        else:
            print("Неверные учетные данные. Пожалуйста, попробуйте снова.")

class Administrator(User):
    def register(self, username, password):
        query = 'INSERT INTO Users (username, password, role_id) VALUES (?, ?, ?)'
        params = (username, password, 3)  # ID роли администратора
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Вы успешно зарегистрировались как администратор!")
        except sqlite3.IntegrityError:
            print("Пользователь с таким именем уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при регистрации: {str(e)}")

    def login(self, username, password):
        query = 'SELECT * FROM Users WHERE username=? AND password=? AND role_id=?'
        params = (username, password, 3)  # ID роли администратора
        result = self._conn.execute(query, params).fetchone()
        if result:
            print("Добро пожаловать, администратор!")
        else:
            print("Неверные учетные данные. Пожалуйста, попробуйте снова.")

