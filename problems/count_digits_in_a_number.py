# Problem:
#   Count the number of digits in a given number.
#
# Example 1:
#   Input: "number": 120
#   Output: 3
# Example 2:
#   Input: "number": -1
#   Output: 1
#
# Constraints:
#   -10^13 < the input number < 10^13
import unittest


def count_digits(number):
    """
    Args:
     number(int64)
    Returns:
     int32
    """
    # Solution:
    #   take absolute of number and divide repeatedly by 10 till the number diminishes to 0
    #       the count of digits is equal to number of divisions
    #       special case: if number is 0 to start with make the count as 1
    # Write your code here.
    pos_number = abs(number)

    digits_number = 0

    if pos_number == 0:
        digits_number = 1

    while pos_number > 0:
        pos_number = pos_number // 10
        digits_number = digits_number + 1

    return digits_number


class Testcase(unittest.TestCase):
    def test_example1(self):
        number = 120
        expected = 3
        actual = count_digits(number)
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        number = -1
        expected = 1
        actual = count_digits(number)
        self.assertEqual(expected, actual, "example1")

    def test_zero(self):
        number = 0
        expected = 1
        actual = count_digits(number)
        self.assertEqual(expected, actual, "zero")
