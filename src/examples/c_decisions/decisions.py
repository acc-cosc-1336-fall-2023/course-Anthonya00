def is_overtime(hours):
    result = False
    result = hours > 40
    return result 


def get_letter_grade(grade): 
    letter_grade = ""

    if(grade >= 90 and grade <= 100) :
        letter_grade = "A"
    elif(grade >= 80 and grade < 90):
        letter_grade = "B"
    elif(grade >= 70 and grade < 80:
        letter_grade = "C"
    elif(grade >= 60 and grade < 70:
        letter_grade = "D"   
    elif(grade >= 0 and grade < 60:
        letter_grade = "F"      
    else:
        letter_grade = "Invalid grade"
        
        return letter_grade


def display_menu():
    print("1-simple if")
    Print("2-if else")
    print("3-if elif")

def run_menu():
    display_menu()  
    option = input("Enter a menu option(1,2, or 3): ")

    handle_menu_option(option)

def handle_menu_option(option):
    if(option == "1" ):
    selected_option_1()
        Print("User selected option 1")
    elif(option == "2" ):
        Print("User selected option 2")
    elif(option == "3" ):
    Print("User selected option 3")   
    else: 
        print("Invalid option")

def selected_option_1():
    print user selected option 1


