a=int(input("Enter the row:"))
b=int(input("Enter the column:"))
array1 = []
array2 = []
result = []
print("Enter elements for Array1:")
for i in range(a):
    row = []
    for j in range(b):
        element = int(input(f"[{i}][{j}]:"))
        row.append(element)
    array1.append(row)
print("Array1:")
for row in array1:
    print(row)
print("Enter elements for Array2:")
for i in range(a):
    row = []
    for j in range(b):
        element = int(input(f"[{i}][{j}]:"))
        row.append(element)
    array2.append(row)
print("Array2:")
for row in array2:
    print(row)
for i in range(a):
    row = []
    for j in range(b):
        row.append(array1[i][j] + array2[i][j])
    result.append(row)
print("Sum of Array1 and Array2:")
for row in result:
    print(row)