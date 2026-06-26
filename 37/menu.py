def menu(**options):

    while True:
        print("Options:")

        for option in options:
            print(f"- {option}")

        choice = input("> ")

        if choice in options:
            return options[choice]()

        print("Please enter a valid choice.\n")