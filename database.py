from models import DatabaseManager

def main():
    project_manager = DatabaseManager()

    project_manager.register_user('user1', 'password1')
    project_manager.login_user('user1', 'password1')
    project_manager.add_project('New Project')

if __name__ == "__main__":
    main()