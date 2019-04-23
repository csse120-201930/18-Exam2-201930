"""
Exam 2, problem 3.
Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3  function:')
    print('--------------------------------------------------')

    format_string = '    problem3( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [9, 2, 6]
    print_expected_result_of_test([10, [9, 15, 2, 20, 13, 6, 8, 1, 17]],
                                  expected, test_results, format_string)
    actual = problem3(10, [9, 15, 2, 20, 13, 6, 8, 1, 17])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [2, 6, 1]
    print_expected_result_of_test([7, [9, 15, 2, 20, 13, 6, 8, 1, 17]],
                                  expected, test_results, format_string)
    actual = problem3(7, [9, 15, 2, 20, 13, 6, 8, 1, 17])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 'Too few'
    print_expected_result_of_test([5, [9, 15, 2, 20, 13, 6, 8, 1, 17]],
                                  expected, test_results, format_string)
    actual = problem3(5, [9, 15, 2, 20, 13, 6, 8, 1, 17])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [4, 2, 4]
    print_expected_result_of_test([5, [5, 4, 11, 2, 4, 4]],
                                  expected, test_results, format_string)
    actual = problem3(5, [5, 4, 11, 2, 4, 4])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [4, 2, 4]
    print_expected_result_of_test([5, [5, 4, 11, 2, 5, 4]],
                                  expected, test_results, format_string)
    actual = problem3(5, [5, 4, 11, 2, 5, 4])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = [4, 3, 2]
    print_expected_result_of_test([5, [4, 3, 2, 1, 0]],
                                  expected, test_results, format_string)
    actual = problem3(5, [4, 3, 2, 1, 0])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 'Too few'
    print_expected_result_of_test([8, [1, 2]],
                                  expected, test_results, format_string)
    actual = problem3(8, [1, 2])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 'Too few'
    print_expected_result_of_test([8, [1, 2, 100]],
                                  expected, test_results, format_string)
    actual = problem3(8, [1, 2, 100])
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3(n, sequence):
    """
    What comes in:
       -- A number n, and
       -- A sequence of numbers.
    What goes out:
      -- Returns a list containing the first 3 numbers in the sequence that
           are strictly less than the given n, unless the sequence has fewer
           than 3 numbers strictly less than the given n, in which case
           the function returns 'Too few'.
    Side effects:   None.
    Examples:
      -- problem3( 10, [9, 15, 2, 20, 13, 6, 8, 1, 17] )  returns [9, 2, 6].
      -- problem3(  7, [9, 15, 2, 20, 13, 6, 8, 1, 17] )  returns [2, 6, 1].
      -- problem3(  5, [9, 15, 2, 20, 13, 6, 8, 1, 17] )  returns 'Too few'.
      -- problem3(  5, [5, 4, 11, 2, 4, 4] )  returns [4, 2, 4].
      -- problem3(  5, [5, 4, 11, 2, 5, 4] )  returns [4, 2, 4].
      -- problem3(  5, [4, 3, 2, 1, 0] )      returns [4, 3, 2].
      -- problem3(  8, [1, 2] )               returns 'Too few'.
      -- problem3(  8, [1, 2, 100] )          returns 'Too few'.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
