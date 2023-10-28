#
import lists

inventory = {}

""""
#1-Add or Update Item
#2-Delete Item
#3-Exit
The program runs until the user chooses option 3.
"""

def display():
    print("1 - Add or Update Item ")
    print("2 - Delete Item ")
    print("3 - Exit ")
    print("4 - check inventory ")

def run_menu():
    display()
    option = str(input("select option 1 or option 2 or option 3 or option 4: "))
    while option not in ('1','2','3','4'):
        option = str(input("Invalid, select option 1,2,3, or 4 : "))
    run_option(option)

def run_option(input):
    if input == '1':
        option_1()
    if input == '2':
        option_2()
    if input == '3':
        option_3()
    if input == '4':
        option_4()

def option_1():
    while True: 
        video_games = str(input("Enter a video game: "))
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                break

            except ValueError: 
                print("Not valid!!! ")

        lists.add_inventory(inventory,video_games,quantity)
        while True:
            add = str(input("do you want to pick another game? yes or no? "))
            if add in ('Yes','Y','YES','y','yes'):
                break
            if add in ('No', 'N', 'n', 'no'):
                print (" going back to main menu ")
                break 
            else: 
                print("Invalid option ")
        if add in ('No', 'N', 'n', 'no'):
            run_menu()
            break

def option_2():
    while True: 
        video_games = str(input("Remove a video game "))
        x = lists.remove_inventory_widget(inventory,video_games)
        print (x)
        while True:
            add = str(input("do you want to remove another game? yes or no? "))
            if add in ('Yes','Y','YES','y','yes'):
                break
            if add in ('No', 'N', 'n', 'no'):
                print (" going back to main menu ")
                break 
            else: 
                print("Invalid option ")
        if add in ('No', 'N', 'n', 'no'):
            run_menu()
            break

def option_3():
    print ("exit") 

def option_4():
    for video_games in inventory.items():
        print (video_games)
    
    menu = None 
    menu = input("press enter to go to main menu ")
    if menu != None:
        print("going to main menu ")
        run_menu()  


run_menu()