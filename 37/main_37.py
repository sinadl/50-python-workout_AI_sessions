from menu import menu


def add():
    return 5 + 3


def greet():
    return "Hello!"


def quit_program():
    return "Goodbye"


result = menu(
    add=add,
    greet=greet,
    quit=quit_program
)

print(result)