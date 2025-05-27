n = int(input("Enter number of rows: "))
count = n * (n + 1) // 2
for i in range(n):
    for j in range(n - i):
        print(count - (n - i - 1 - j), end=" ")
    count -= (n - i)
    print()
