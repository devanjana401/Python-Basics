class BankAccount:
    def __init__(self, name, account_number):
        self.__name = name
        self.__account_number = account_number
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def account_number(self):
        return self.__account_number
    @account_number.setter
    def account_number(self, value):
        self.__account_number = value
acc = BankAccount("Anjana", "1234567890")
print("Name:", acc.name)
print("Account Number:", acc.account_number)
acc.name = "Akash"
acc.account_number = "0987654321"
print("After update:")
print("Name:", acc.name)
print("Account Number:", acc.account_number)
