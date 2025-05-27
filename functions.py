array = []
def getArray():
    global array 
    n = int(input("Enter number of elements in the array: "))
    array = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        array.append(element)
def displayArray():
    print("Array elements are:")
    for element in array:
        print(element, end=' ')
    print()
def main():
    getArray()
    displayArray()
main()
