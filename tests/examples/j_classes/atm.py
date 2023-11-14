
from examples.j_classes.bank_account import bank_account


class ATM:
    __bank__account = None

    def _init_self(self, bank_account):
        self.__bank__account = bank_account

    def make_deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.__bank__account.deposit(amount)

    def make_deposit(self):
        amount = int(input("Enter withdraw amount: "))
        self.__bank__account.deposit(amount)

    def display_balance(self):
        print(self.__bank__account.get_balance())
