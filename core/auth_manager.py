# FILE: auth_manager.py
# USE: Manages user authentication, including login, registration, and logout processes.

# fetching data from db through storage.filehandler and validating it

from storage.file_handler import get_storage

storage = get_storage()
booklist = storage.get_books()

# login
# register
# logout

def AUTH_MANAGER(action):

    if action == "login":
        print(booklist)
    elif action == "register":
        register()
    elif action == "logout":
        logout()
    else:
        print("Invalid action. Please choose from 'login', 'register', or 'logout'.")

# getting user data from db and validating it for login
def validate_user_credentials(username, password):
    
    return False

def login():
    print("Login functionality is not implemented yet.")


def register():
    print("Registration functionality is not implemented yet.")


def logout():
    print("Logout functionality is not implemented yet.")