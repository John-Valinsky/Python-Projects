Encapsulation
=============
class Account:
    def __init__(self, balance):
        self.__balance = balance   

        def show_balance(self):
            print(self.__balance)

acc = Account(1000)
acc.show_balance()