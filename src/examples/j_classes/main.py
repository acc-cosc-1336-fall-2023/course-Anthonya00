import bank_account,atm

list_account = []

account = bank_account.BankAccount(50)

list_account.append(account)

account = bank_account.BankAccount(50)

list_account.append(account)

account = bank_account.BankAccount(50)

list_account.append(account)

for account in list_account:
    print (account)