class OnePressedError(Exception):
    pass
for i in range(3):
    try:
        print("\nMenu:")
        print("1. Raise custom exception")
        print("2. Just a normal option")
        choice = input("Enter your choice: ")

        if choice == "1":
            raise OnePressedError("You pressed 1, which is not allowed!")
        print("You selected option", choice)
    except OnePressedError as e:
        print("Custom Exception Caught:", e)
