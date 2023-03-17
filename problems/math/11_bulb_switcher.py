# Problem:
#   https://leetcode.com/problems/bulb-switcher/
#   There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
#   On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
#       For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
#   Return the number of bulbs that are on after n rounds.
#
# Example1:
#   Input: n = 3
#   Output: 1
#   Explanation:
#       At first, the three bulbs are [off, off, off].
#   After the first round, the three bulbs are [on, on, on].
#   After the second round, the three bulbs are [on, off, on].
#   After the third round, the three bulbs are [on, off, off].
#   So you should return 1 because there is only one bulb is on.
#
# Example2:
#   Input: n = 0
#   Output: 0
#
# Example3:
#   Input: n = 1
#   Output: 1
#
# Constraints:
#   0 <= n <= 10^9
import math
import unittest


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution:
        #   Let say i, is an arbitrary bulb in n
        #       For i=1, it is visited once, rounds = 1. so the bulb is on
        #       For i=2, it is visited twice, rounds = 1, 2. so bulb is off (on, off)
        #       For i=3, it is visited twice, rounds = 1, 3. bulb is off (2 toggles)
        #       For i=4, it is visited thrice, rounds = 1, 2, 4. bulb is on (3 toggles)
        #       For i=i, it is visited based on number of factors (#factors). bulb is on if #factors is odd
        #   any number can be represented as a product of power of primes using
        #       Euclid's fundamental theorem of arithmetics
        #   e.g. 6 = 2^1 x 3^1
        #       => factors are product of subsets we get by choosing the powers
        #       => [ [2^0 x 3^0], [2^1 x 3^0], [2^0 x 3^1], [2^1 x 3^1] ]
        #       => [ 1, 2, 3, 6]
        #       => Number of factors is 4 which is same as (1+1)x(1+1)
        #   e.g. 64 = 2^6
        #       => Number of factors is (6+1) = 7
        #       => factors = [ [2^0], [2^1], [2^2], [2^3], [2^4], [2^5], [2^6] ]
        #       => factors = [1, 2, 4, 8, 16, 32, 64]
        #   so, the number of factors (say #factors) is number ways the powers of prime can be chosen
        #       for n = a^p x b^q x c^r ... where a,b,c,.. are prime and p,q,r,.. > 0
        #       => #factors = (p+1) x (q+1) x (r+1) x ...
        #       => #factors is odd only when the expression on right is odd
        #       =>  p,q,r,.. should be even
        #       =>  number should be a perfect square
        #
        #   We can check for every i > 1 & i <= n, if it's a perfect square to check if bulb is on
        #       and count them.
        #
        # Code:
        if n == 0:
            return 0

        number_of_bulbs_on = 1
        i = 2
        while i * i <= n:
            number_of_bulbs_on = number_of_bulbs_on + 1
            i = i + 1

        return number_of_bulbs_on


class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 3
        expected = 1
        actual = Solution().bulbSwitch(n)
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        n = 0
        expected = 0
        actual = Solution().bulbSwitch(n)
        self.assertEqual(expected, actual, "example2")

    def test_example3(self):
        n = 1
        expected = 1
        actual = Solution().bulbSwitch(n)
        self.assertEqual(expected, actual, "example3")

    def test_number6(self):
        n = 6
        expected = 2
        actual = Solution().bulbSwitch(n)
        self.assertEqual(expected, actual, "number6")

    def test_number10(self):
        n = 10
        expected = 3
        actual = Solution().bulbSwitch(n)
        self.assertEqual(expected, actual, "number10")
