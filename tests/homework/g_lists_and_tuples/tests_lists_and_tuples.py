#

import unittest

from src.homework.g_lists_and_tuples.lists import add_inventory, remove_inventory_widget 

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):

#Write to assert that adding Widget1 with quantity of 10 to the inventory_dictionary inserts the Widget1 with value of 10 for quantity.
#Write another assertion to test that adding Widget1 with quantity of 25 updates the existing Widget1 item quantity to 35.
#Write another assertion to test that adding Widget1 with quantity of -10 updates the existing Widget1 item quantity to 25.

        inventory = {}
        add_inventory(inventory, 'MK1', 10 ) 

        self.assertEqual(inventory['MK1'],10) 

        add_inventory(inventory, 'MK1', 25 ) 

        self.assertEqual(inventory['MK1'],35) 

        add_inventory(inventory, 'MK1', -10 ) 

        self.assertEqual(inventory['MK1'],25) 

#Write a test case add two widgets(widget1 and widget2 with quantities of your choice).
#Remove widget1. Test that the length of dictionary is 1 and that widget2 still exists.

    def test_remove_inventory(self):
        inventory = {'MK1':10, 'mario':10 }
        remove_inventory_widget (inventory, 'mario') 
        self.assertEqual(len(inventory),1)

        self.assertEqual(inventory,{'MK1':10})
        




