def diplay_menu():
    print('COSC BANK')
    print('1- deposit')
    print('2- withdraw')
    print('3- display Balance')
    print ('4- Exit')

def run_menu(atm):

    menu_choice = 0

    while(menu_choice != '4'):
        display_menu()
        menu_choice = input("Enter Choice: ")

def handle_menu(menu_choice,atm ):

    if (menu_choice == '1'):
        atm.make_deposit()
    elif(menu_choice == '2'):
        atm.make_withdraw()
    elif(menu_choice == '3'):
        atm.display_balance()
    elif(menu_choice  == '4'):
        print('Exiting...')
    else:
        print("invalid choice")
