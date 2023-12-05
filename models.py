import sqlite3

class ProjectManager:
    def __init__(self, db_name="projects.db"):
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
                CREATE TABLE IF NOT EXISTS Projects (
                    project_id INTEGER PRIMARY KEY,
                    project_name TEXT NOT NULL UNIQUE
                )
            ''')
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Tasks (
                    task_id INTEGER PRIMARY KEY,
                    project_id INTEGER,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT,
                    deadline TEXT,
                    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
                )
            ''')
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS Teams (
                    team_id INTEGER PRIMARY KEY,
                    team_name TEXT NOT NULL UNIQUE
                )
            ''')
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS TeamMembers (
                    team_member_id INTEGER PRIMARY KEY,
                    team_id INTEGER,
                    user_id INTEGER,
                    FOREIGN KEY (team_id) REFERENCES Teams(team_id),
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
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

    def login_user(self, username, password):
        query = 'SELECT * FROM Users WHERE username=? AND password=?'
        params = (username, password)
        result = self._conn.execute(query, params).fetchone()
        if result:
            print(f"Добро пожаловать, {username}!")
        else:
            print("Неверные учетные данные. Пожалуйста, попробуйте снова.")

    def add_project(self, project_name):
        query = 'INSERT INTO Projects (project_name) VALUES (?)'
        params = (project_name,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Проект успешно добавлен!")
        except sqlite3.IntegrityError:
            print("Проект с таким именем уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении проекта: {str(e)}")

    def delete_project(self, project_id):
        query = 'DELETE FROM Projects WHERE project_id = ?'
        params = (project_id,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Проект успешно удален!")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении проекта: {str(e)}")

    def get_project_tasks(self, project_id):
        query = 'SELECT * FROM Tasks WHERE project_id=?'
        params = (project_id,)
        return self._conn.execute(query, params).fetchall()

    def create_team(self, team_name):
        query = 'INSERT INTO Teams (team_name) VALUES (?)'
        params = (team_name,)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Команда успешно создана!")
        except sqlite3.IntegrityError:
            print("Команда с таким именем уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при создании команды: {str(e)}")

    def add_team_member(self, team_id, user_id):
        query = 'INSERT INTO TeamMembers (team_id, user_id) VALUES (?, ?)'
        params = (team_id, user_id)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Участник успешно добавлен в команду!")
        except sqlite3.IntegrityError:
            print("Этот участник уже в этой команде.")
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении участника в команду: {str(e)}")

    def remove_team_member(self, team_id, user_id):
        query = 'DELETE FROM TeamMembers WHERE team_id = ? AND user_id = ?'
        params = (team_id, user_id)
        try:
            with self._conn:
                self._conn.execute(query, params)
            print("Участник успешно удален из команды!")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении участника из команды: {str(e)}")
