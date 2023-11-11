#
import unittest, random
from src.homework.j_classes.class_a import die 

class Test_config(unittest.TestCase):

    def test_die(self):
       dice_roll = die ()

       for _ in range(3): 

            dice_roll.roll()
            self.assertEqual(1 <= dice_roll.get_rolled_value()<= 6, True)

       