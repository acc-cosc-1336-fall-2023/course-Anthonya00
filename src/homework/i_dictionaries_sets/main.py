#
import dictionary

def display():
    print("1 -Get Distance Matrix")
    print("2 - exit")

def run_menu():
    display()
    option = str(input("select option 1 or option 2: "))
    while option not in ('1','2'):
        option = str(input("Invalid, select option 1 or 2: "))
    run_option(option)

def run_option(input):
    if input == '1':
        option_1()
    if input == '2':
        option_2()


def option_1():
    print("\n you selected option 1: ")
    y = create_list() 
    while True:
        try:
            x = dictionary.get_p_distance_matrix(y)
            break
        except ValueError:
            print("strings not of equal length" )
            y = create_list()
    print ("your matrix distance is: ")
    for i in range(len(x)):
        print(x[i])
    run_menu()

def create_list():
    data = []
    while True:
        try:
            n = int(input("Enter # of lists: "))
            if n >=1:
                break
            else:
                print("Input at least 1 lists")
        except ValueError:
            print("This is not a whole number")
    print(f'Enter {n} lists')
    for i in range (n):
        list_input = input(f"number {i+1}:").strip()
        data.append(list(list_input))
    return data

def option_2():
    print("\n you're exiting the program: ")


run_menu()