#

import class_a 

user_choice = str(input("Press Y to roll a die ")).lower()

while user_choice == "y":
    dice_roll = class_a.die()
    dice_roll.roll()

    print(dice_roll)

    user_choice = str(input("Press Y to roll a die again ")).lower()

    

