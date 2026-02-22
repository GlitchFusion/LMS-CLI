# Actions available in the menu

# common actions
COMMON_MENU_OPTIONS = [
    "View available books",
    "Search for a book",
    "View my account details",
    "logout",
]

# for normal members
MEMBER_MENU = [
    "Borrow a book",
    "Return a book",
    "View my borrowed books",
]

# for librarians/admins
LIBRARIAN_MENU = [
    "Add a new book",
    "Remove a book",
    "View all members",
    "View all issues",
]

# for faculty
FACULTY_MENU = [
    "Borrow a book",
    "Return a book",
    "View my borrowed books",
    "Request a book",
]

def Menu(role):
    if role == "member":
        return MEMBER_MENU + COMMON_MENU_OPTIONS
    elif role == "librarian":
        return LIBRARIAN_MENU + COMMON_MENU_OPTIONS
    elif role == "faculty":
        return FACULTY_MENU + COMMON_MENU_OPTIONS
    else:
        return COMMON_MENU_OPTIONS