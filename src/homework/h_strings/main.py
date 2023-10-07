from strings import get_dna_complement, get_hamming_distance


def display_menu():
    print("1 - Hamming Distance")
    print("2 - DNA Reverse Complement")
    print("3 - Exit")

def run_menu():
    display_menu()
    option = str(input("select option 1,2, or 3:"))
    while (option != '1'and option != '2' and option != '3'):
        option = str(input("option Invalid. select 1,2,or 3:"))
    select_option(option)

def select_option(option):
    if option =='1':
        option_1()
    if option == '2':
        option_2()
    if option == '3':
        option_3()

def option_1():
    print("\nyou selected option 1, Enter 2 strings of equal length to find the hamming Distance ")
    y = hamming_parameter ()
    while y== "Invalid, both strings are not of equal length":
        print("These 2 strings aren't of equal length,try again.")
        y = hamming_parameter()
    print(f"\nTheHamming Distance between these two strings is {y}.\n")
    try_agin_option_1()

def option_2():
    print("\nYou selected option 2, Enter a valid DNA strand to find the reverse complement")
    DNA_STRAND = str(input("Enter your DNA strand: "))
    y= get_dna_complement(DNA_STRAND)
    while y == "This sequence is not a DNA strand.":
        print("This strand is NOT a valid DNA strand")
        DNA_STRAND = str(input("Please Enter a Valid DNA strand: "))
        y= get_dna_complement(DNA_STRAND) 
    print (y)


def option_3():
    while True:
        exit = input("Are you sure you want to exit y/n: ")
        if exit == "yes" or exit == "y" or exit == 'Y' or exit == 'YES' :
            print("\nExiting program\n")
            break
        elif exit == "no" or exit == "n" or exit == 'N' or exit == 'NO' :
            run_menu
            break
        else:
            print("please enter yes or no")

def hamming_parameter():
    dna1 = str(input("Enter your 1st String: "))
    dna2 = str(input("Enter your 2nd string: "))
    y= get_hamming_distance(dna1, dna2)
    return y 

def try_agin_option_1():
    while True:
        x= str(input("press 'y if would like to try again, press 'n to return to main menu, press 3 to exit:"))
        if x == "yes" or x == 'Y' or x == 'YES':
            option_1()
            break
        if x == "no" or x == "n" or x == 'N' or x == 'NO':
            print("Returning to Main Menu\n")
            run_menu()
            break 
        if x== "3":
            option_3()
            break
        else:
            print("please enter 'y' or 'n' or '3' ")

def try_agin_option_2():
    while True:
        x= str(input("press 'y' if would like to try again, press 'n' to return to main menu, press 3 to exit: "))
        if x == "no" or x== "n" or x == 'N' or x == 'NO':
            print ("Returning to main menu\n")
            run_menu()
            break
        if x == "3":
            option_3()
            break
        else:
            print("please enter 'y' or 'n' or '3' ")

run_menu()