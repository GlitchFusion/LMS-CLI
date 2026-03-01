# database imports
from database.init_db import init_db
# core imports
from core.auth_manager import AUTH_MANAGER

FIRST_RUN_ACTIONS = [
    "Login",
    "Register",
    "Exit"
]

def initialize_database():
    init_db()

def main():
    initialize_database()
    print("Welcome to the CLI Library Management System!")
    for i in range(len(FIRST_RUN_ACTIONS)):
        print(f"{i+1}. {FIRST_RUN_ACTIONS[i]}")
    
    while True:
        choice = input("Please select an option: ")
        if choice == "1":
            AUTH_MANAGER("login")
        elif choice == "2":
            print("Registration functionality is not implemented yet.")
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            exit(1)

    
main()