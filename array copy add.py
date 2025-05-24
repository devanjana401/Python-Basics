n=int(input("Enter the size of array:"))
array1 = []
for i in range(n):
    element=int(input(f"enter element {i+1}:"))
    array1.append(element)
array2 = array1.copy()
for j in range(2):
    element=int(input(f"enter element {n+j+1}:"))
    array2.append(element)
print("Array1:",array1)
print("Array2:",array2)