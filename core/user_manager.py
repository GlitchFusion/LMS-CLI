# managing user data and adding users to db

from storage.file_handler import get_storage
from core.pwd_manager import decode_password

storage = get_storage()
users = storage.get_all_users()

# user credentials account validation
def user_credentials_validation(email, pwd):
    password = decode_password(pwd)
    for user in users:
        if user[2] == email and user[3] == password:
            return True
        elif user[2] == email and user[3] != password:
            print("Incorrect password. Please try again.")
            return False
        else:
            print("Email not found. Please register or try again.")
    return False