T =float(input("Enter the total mark: "))
if(T>90):
    grade="A"
elif(80<T<89):
    grade="B"
elif(70<T<79):
    grade="C"
elif(60<T<69):
    grade="D"
elif(50<T<59):
    grade="E"
else:
    grade="failed"
print("Your grade is:",grade)