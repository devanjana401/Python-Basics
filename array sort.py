n = int(input("Enter the size of array: "))
array = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)
for i in range(n):
    for j in range(i + 1,n):
        if array[i]<array[j]:
           array[i],array[j] = array[j],array[i]
print("Sorted array:",array)