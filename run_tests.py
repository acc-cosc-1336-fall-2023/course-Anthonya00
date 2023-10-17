import unittest

#from tests.homework.h_strings import tests_strings

from test.examples.g_lists_and_tuples import test_lists_and_tuples

suite = unittest.TestLoader().loadTestsFromModule(test_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)  

