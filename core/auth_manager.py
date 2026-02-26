# FILE: auth_manager.py
# USE: Manages user authentication, including login, registration, and logout processes.

# fetching data from db through storage.filehandler and validating it

from datetime import datetime

from storage.file_handler import get_storage
from utils.validators import user_credentials_validation, password_validation
from core. pwd_manager import encode_password

access_to_acount = False

storage = get_storage()
booklist = storage.get_all_books()

add_user = storage.add_users

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
    email = input("Enter your email: ")
    pwd = input("Enter your password: ")
    if user_credentials_validation(email, pwd):
        login()

def REGISTER_FORM():
    username = input("Enter your username: ")
    email = input("Ener your email: ")
    pwd = input("Enter your password: ")
    confirm_pwd = input("Confirm your password: ")
    if pwd != confirm_pwd:
        print("Passwords do not match. Please try again.")
        return
    if not password_validation(pwd):
        return
    register(pwd)


def login():
    print("Login successful!")
    return True


def register(username, email, pwd):
    password = encode_password(pwd)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_user(username, email, password, current_time)
    print("Registration successful!")
    return True


def logout():
    global access_to_acount
    access_to_acount = False

# give access to account if credentials are valid
def access_account(): 
    global access_to_acount
    if login():
        access_to_acount = True
    if register():
        access_to_acount = True