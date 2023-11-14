import bank_account,atm

account = bank_account.BankAccount(50)
account.__get_balance_from_db()

#print(account.get_balance())
my_atm = atm.ATM(account)

menu.run_menu(my_atm)

#print(account.get_balance())

#my_atm.make_deposit()
#my_atm.display_balance()

#my_atm.make_withdraw()
#my_atm.display_balance
