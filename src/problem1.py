"""
Exam 2, problem 1.
Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # Uncomment the following calls to the testing functions one at a time
    # as you work the problems.
    # -------------------------------------------------------------------------
    print()
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    # run_test_problem1a()
    # run_test_problem1b()
    # run_test_problem1c()


###############################################################################
# TODO: 2.  READ the doc-strings for the  sum_of_digits  and  is_prime
# functions defined below.  They are the same as you have seen before.
# After you UNDERSTAND the doc-string (JUST the doc-string, NOT the code),
# ASKING QUESTIONS AS NEEDED, change the above _TODO_ to DONE.
###############################################################################

def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a  function:')
    print('--------------------------------------------------')

    format_string = '    problem1a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 30 + 5  # which is 35
    print_expected_result_of_test([[30, 1, 22, 8, 5]], expected, test_results,
                                  format_string)
    actual = problem1a([30, 1, 22, 8, 5])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 8 + 8  # which is 16
    print_expected_result_of_test([[8, 30, 40, 50, 1, 3, 66, 8]], expected,
                                  test_results, format_string)
    actual = problem1a([8, 30, 40, 50, 1, 3, 66, 8])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 0
    print_expected_result_of_test([[20, -20]], expected, test_results,
                                  format_string)
    actual = problem1a([20, -20])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 40
    print_expected_result_of_test([[20, 20]], expected, test_results,
                                  format_string)
    actual = problem1a([20, 20])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 30 + 5  # which is 35
    print_expected_result_of_test([(30, 1, 22, 8, 5)], expected, test_results,
                                  format_string)
    actual = problem1a((30, 1, 22, 8, 5))
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem1a(sequence):
    """
    What comes in:  A sequence of numbers.  You may assume that the sequence
      contains at least 2 numbers.
    What goes out:
      -- Returns the sum of the first and last numbers in the sequence.
    Side effects:   None.
    Examples:
      -- problem1a( [30, 1, 22, 8, 5] ) returns 30 + 5 (which is 35).
      -- problem1a( [8, 30, 40, 50, 1, 3, 66, 8] ) returns 8 + 8 (which is 16).
      -- problem1a( [20, -20] ) returns 0.
      -- problem1a( [20, 20] )  returns 40.
      -- problem1a( (30, 1, 22, 8, 5) )  returns 35.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


def run_test_problem1b():
    """ Tests the   problem1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b  function:')
    print('--------------------------------------------------')

    format_string = '    problem1b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 33
    print_expected_result_of_test([[24, 905, 3, 1234]],
                                  expected, test_results, format_string)
    actual = problem1b([24, 905, 3, 1234])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 14
    print_expected_result_of_test([[905]],
                                  expected, test_results, format_string)
    actual = problem1b([905])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 15
    print_expected_result_of_test([[0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0]],
                                  expected, test_results, format_string)
    actual = problem1b([0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 0
    print_expected_result_of_test([[]],
                                  expected, test_results, format_string)
    actual = problem1b([])
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem1b(integers):
    """
    What comes in:  A sequence of positive integers
    What goes out:
      -- Returns the sum of all the digits in all the numbers in the sequence.
    Side effects:   None.
    Examples:
      -- problem1b( [24, 905, 3, 1234] )
              returns  2 + 4 + 9 + 0 + 5 + 3 + 1 + 2 + 3 + 4, which is 33.
      -- See the test cases for more examples, or ASK YOUR INSTRUCTOR
           FOR HELP if this problem's specification is not clear to you.
     """
    ###########################################################################
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    # NOTE that there is a   sum_of_digits   function above that is relevant!
    ###########################################################################


def run_test_problem1c():
    """ Tests the   problem1c   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1c  function:')
    print('--------------------------------------------------')

    format_string = '    problem1c( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 1
    print_expected_result_of_test([[30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2]],
                                  expected, test_results, format_string)
    actual = problem1c([30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 999
    print_expected_result_of_test([[1, 2, 3]],
                                  expected, test_results, format_string)
    actual = problem1c([1, 2, 3])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -100
    print_expected_result_of_test([[-100, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2]],
                                  expected, test_results, format_string)
    actual = problem1c([-100, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 2
    print_expected_result_of_test([[30, 2, 2, 9, 10, 90, 10, 40, 19, 40, 2]],
                                  expected, test_results, format_string)
    actual = problem1c([30, 2, 2, 9, 10, 90, 10, 40, 19, 40, 2])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 999
    print_expected_result_of_test([[]],
                                  expected, test_results, format_string)
    actual = problem1c([])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 999
    print_expected_result_of_test([[0]],
                                  expected, test_results, format_string)
    actual = problem1c([1])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = -1
    print_expected_result_of_test([[-1]],
                                  expected, test_results, format_string)
    actual = problem1c([-1])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:  Same at Test #1, but a tuple
    expected = 1
    print_expected_result_of_test([(30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2)],
                                  expected, test_results, format_string)
    actual = problem1c((30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2))
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem1c(integers):
    """
    What comes in:  A sequence of integers.
    What goes out:
      -- Returns the first integer in the sequence that is less than its index,
           or 999 if there is no such integer in the sequence.
    Side effects:   None.
    Examples:
      -- problem1c( [30, 2, 2, 9, 1, 0, -10, 4, 1, 40, 2] )
              returns 1
           since:  It is NOT true that 30 < 0
                   It is NOT true that 2 < 1
                   It is NOT true that 2 < 2
                   It is NOT true that 9 < 3
                   It IS true that 1 < 4  (and so 1 is returned)
      -- problem1c( [1, 2, 3] )
              returns 999
           since none of the three numbers are less than
           their respective indices (0, 1, and 2, respectively).
     """
    ###########################################################################
    # TODO: 5. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################


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
