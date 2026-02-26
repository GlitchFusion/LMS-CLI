from storage.file_handler import get_storage

storage = get_storage()
users = storage.get_all_users()

# password validation
def password_validation(pwd):
    # checking for minimum length
    if len(pwd) < 8:
        print("Password must be at least 8 characters long.")
        return False
    # checking for at least one digit
    if not any(char.isdigit() for char in pwd):
        print("Password must contain at least one digit.")
        return False    
    # checking for at least one letter
    if not any(char.isalpha() for char in pwd):
        print("Password must contain at least one letter.")
        return False
    # checking for at least one special character
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in pwd):
        print("Password must contain at least one special character.")
        return False
    # checking for unneccesary characters
    if any(char in pwd for char in [' ', '\t', '\n']):
        print("Password cannot contain spaces or whitespace characters.")
        return False
    
    return True

# user credentials account validation
def user_credentials_validation(email, pwd):
    for user in users:
        if user[2] == email and user[3] == pwd:
            return True
    return False