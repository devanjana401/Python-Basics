from abc import ABC, abstractmethod
class calculator(ABC):
    def _init_(self, id, name):
        self.id = id
        self.name = name
    @abstractmethod
    def addition(self, a, b):
        pass
    @abstractmethod
    def subtraction(self, a, b):
        pass
    @abstractmethod
    def multiplication(self, a, b):
        pass
    @abstractmethod
    def division(self, a, b):
        pass
class MyCalculator(calculator):
    def _init_(self):
        super()._init_(1, "Basic Calculator")
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b
def main():
    print("Choose an operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    n=int(input("The operation choosed:"))
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    calc = MyCalculator()
    if n == 1:
        result = calc.addition(num1, num2)
        print("Result:", result)
    elif n == 2:
        result = calc.subtraction(num1, num2)
        print("Result:", result)
    elif n == 3:
        result = calc.multiplication(num1, num2)
        print("Result:", result)
    elif n == 4:
        result = calc.division(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice!")
main()