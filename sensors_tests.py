import sensors_main
import unittest
import sys # needed for setting the command line parameters for test cases
from unittest.mock import patch # needed for the integration test case

# Unit tests implemented with Python's built-in unittest need to be classes,
# so here we use TestSensors class for the tests.
class TestSensors(unittest.TestCase):
    ###################
    # Unit test cases #
    ###################

    # Test case test_check_limits1 (UT3) that tests the check_limits
    # with correct inputs (lower limit 16 and higher limit 16) and
    # expects the method to return False, since the limits are
    # incorrect.
    #UT3
    def test_check_limits1(self):
        limits = [16, 16]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, False)
    
    # Test case test_check_limits2 (UT4) that tests the check_limits
    # with incorrect inputs (lower limit 17 and higher limit 20) and
    # expects the method to return True, since the limits are
    # correct.
    #UT4
    def test_check_limits2(self):
        limits = [17, 20]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)

    #UT5
    # Test case test_check_limits1 (UT5) that tests the check_limits
    # with correct inputs (lower limit 20 and higher limit 19) and
    # expects the method to return False, since the limits are
    # incorrect.
    #UT5
    def test_check_limits3(self):
        limits = [20, 19]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, False)

    ##########################
    # System test cases #
    ##########################
    def test_system_main(self):
        sys.argv = ['sensors_main.py', '17', '17']
        expected_output = "Error: Incorrect command line arguments.\n"
        
        sys.stdout = StringIO()
        
        sensors_main.main()
        output = sys.stdout.getvalue()

        sys.stdout = sys._stdout_

        self.assertEqual(output, expected_output)

    ##########################
    # Integration test cases #
    ##########################

    # TODO: Complete test case test_check_limits_integration1 code so
    # that tests the check_limits function from main function.

    # NOTE: Redirect console output to sys.stdout in order to check it
    # from the test cases (here, from the integration test case). Also, use
    # mock_print as a parameter of the test case function.
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        sys.argv = ['sensors_main.py', '20', '17']
        expected_output = "Error: Incorrect command line arguments.\n"
        
        sensors_main.main()
        output = mock_print.call_args[0][0]

        self.assertEqual(output, expected_output)
        # 1. set command line parameters, since they are where main gets the
        # min and max temperature settings

        # 2. call main with the command line parameters set up

        # 3. check that the console output is the expected error message

        # 4. If you want to see what is in mock_print, you can use the following
        # (requires that there is import sys (as this module has) because this
        # test case sets the command line arguments that are in sys.argv)
        #
        sys.stdout.write(str(mock_print.call_args) + "\n")
        sys.stdout.write(str(mock_print.call_args_list) + "\n")

if __name__ == '__main__':
    unittest.main()
