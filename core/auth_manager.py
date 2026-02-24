# FILE: auth_manager.py
# USE: Manages user authentication, including login, registration, and logout processes.

# fetching data from db through storage.filehandler and validating it

from storage.file_handler import get_storage
from utils.validators import user_credentials_validation, password_validation

access_to_acount = False

storage = get_storage()
booklist = storage.get_all_books()

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

# FORM: Gets user details
def LOGIN_FORM():
    username = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if user_credentials_validation(username, pwd):
        print("Login successful!")
        return True

def REGISTER_FORM():
    username = input("Choose a username: ")
    pwd = input("Choose a password: ")
    return username, pwd

def login():
    print("Login functionality is not implemented yet.")


def register():
    print("Registration functionality is not implemented yet.")


def logout():
    print("Logout functionality is not implemented yet.")

# give access to account if credentials are valid
def access_account():
    global access_to_acount
    if LOGIN_FORM():
        access_to_acount = True