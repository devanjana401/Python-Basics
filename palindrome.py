string = input("Enter the string: ")
n = len(string)
for i in range(n // 2):
    if string[i] != string[n - i - 1]:
        print("It's not a palindrome")
        break
else:
    print("It's a palindrome")
