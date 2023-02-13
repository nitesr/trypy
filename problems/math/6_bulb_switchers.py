# https://leetcode.com/problems/bulb-switcher/
# There are n bulbs that are initially off. You first turn on all the bulbs,
#   then you turn off every second bulb.
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
#   For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
# Return the number of bulbs that are on after n rounds.
#
# Constraints:
# 0 <= n <= 10^9
import math
import unittest


def num_bulbs_on(n) -> int:
    # 1-st bulb is on
    # 2-nd bulb is off (1 for on & 2 for off)
    # i-th bulb is on if it is toggled odd number of times
    #   that should be equal to number of factors (e.g. i=10 will be toggled for 1, 2, 5, 10)
    #   and perfect squares have odd number of factors (e.g i=49 will be toggled for 1, 4, 9, 16, 25, 36, 49)
    #   and number of perfect squares should sqrt(i)
    #       (because till i we have perfect squared for each of integer <= sqrt(i))
    return int(math.sqrt(n))


class Test(unittest.TestCase):

    # Example 1:
    #   Input: n = 3
    #   Output: 1
    def test_example1(self):
        result = num_bulbs_on(3)
        self.assertEqual(1, result, "Example 1")

    # Example 2:
    #   Input: n = 0
    #   Output: 0
    def test_example2(self):
        result = num_bulbs_on(0)
        self.assertEqual(0, result, "Example 2")

    # Example 3:
    #   Input: n = 1
    #   Output: 1
    def test_example3(self):
        result = num_bulbs_on(1)
        self.assertEqual(1, result, "Example 3")

    # Example 4:
    #   Input: n = 5
    #   Output: 2
    def test_example4(self):
        result = num_bulbs_on(5)
        self.assertEqual(2, result, "Example 4")

    # Example 5:
    #   Input: n = 49
    #   Output: 7
    def test_example5(self):
        result = num_bulbs_on(49)
        self.assertEqual(7, result, "Example 5")
