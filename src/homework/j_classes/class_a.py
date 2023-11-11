import random

class die:
    __roll_value = None 

    def roll(self): 
        die_roll = random.randint(1 , 6)
        self.__roll_value = die_roll 

    def get_rolled_value(self): 
        return self.__roll_value
    
    def __str__(self): 
        return f"the roll value is , {self.__roll_value} "

