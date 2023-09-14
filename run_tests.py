import unittest
from tests.homework.b_in_proc_out import tests_in_proc_out 

suite = unittest.TestLoader().loadTestsFromModule(test_decisions)
unittest.TextTestRunner(verbosity=2).run(suite)

from test.examples.c_decisions import test_decisions 