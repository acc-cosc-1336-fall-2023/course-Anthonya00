import bank_account,atm

account = bank_account.BankAccount(50)

print(account.get_balance())
my_atm = atm.ATM(account)

print(account.get_balance())

my_atm.make_deposit()
my_atm.display_balance()

my_atm.make_withdraw()
my_atm.display_balance
