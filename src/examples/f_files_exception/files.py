#

def write_to_file(file_name):
    out_file = open(file_name, 'w')

    #rite to file
    out_file.write('John Locke\n')
    out_file.write('David Hum\n')
    out_file.write('Edmund Burke\n')

    #close the file 
    out_file.close()

def read_from_file(file_name):
    in_file = open(file_name, 'r')

    file_contents = in_file.read()

    #close file
    in_file.close()

    print(file_contents)

def read_each_line_from_file(file_name):
    in_file = open(file_name, 'r')

    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()

    in_file.close();

    print(line1.rstrip('\n'))
    print(line2.rstrip('\n'))
    print(line3.rstrip('\n'))

def write_names_to_file(file_name):
    out_file =  open(file_name, 'w')

    user_choice = 'y'

    while(user_choice == 'y' or user_choice == 'Y')
        name = input("Enter friend: ")
        out_file.write(name + '\n')
        user_choice = input("Type y to continue... ")


    out_file.close()


