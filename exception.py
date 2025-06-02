class MyError(Exception):
    pass
choice = input("Press 1 to raise error: ")
try:
    if choice == "1":
        raise MyError("Error: You pressed 1")
except MyError as e:
    print(e)