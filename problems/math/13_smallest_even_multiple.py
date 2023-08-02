# Problem:
#   Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
#
# Example 1:
#   Input: n = 5
#   Output: 10
#   Explanation: The smallest multiple of both 5 and 2 is 10.
# Example 2:
#   Input: n = 6
#   Output: 6
#   Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
#
# Constraints:
#   1 <= n <= 150
import unittest


class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution:
        #   if n is even, its already multiple of 2 otherwise we can multiply by 2 to get lowest
        #
        #   Generic:
        #   say GCD(m, n) = g => m/g and n/g are co-prime. (GCD is
        #   greatest common divisor between m & n when it divides them
        #   there is no common factor other than 1 e.g. GCD(10, 8) = 2
        #   and 10/2=5 and 8/2=4 doesn't have any common factor other
        #   than 1. 5 & 4 are co-prime). Refer to below section "Find
        #   GCD"

        #   => LCM(m/g, n/g) = m/g * n/g
        #   => LCM(m, n) = g * LCM(m/g, n/g)
        #       (it becomes multiple of m & n i.e. m * (n/g) or n * (m/g) )
        #   => LCM(m, n) = (m * n)/g

        #   Another way to put it,
        #   m = p * g and n = q * g (where g is GCD(m, n)
        #   => LCM(m, n) =   m * n * g (take out duplicate factors)
        #   => LCM(m, n) * g = g * p * q * g
        #   => LCM(m, n) * g = (g * p) * (q * g) = m * n
        #   => LCM(m, n) = (m * n)/g

        #   so the solution is to find (m * n) / GCD(m, n)
        #   GCD(2, n) = 2 (n is even) or 1 (n is odd)
        #   => LCM(2, n) = 2n/2 (n is even) or 2n (n is odd)
        #   => LCM(2, n) = n (n is even) or 2n (n is odd)
        #
        # Code here:
        if n % 2 == 0:
            return n
        else:
            return n * 2


class Testcase(unittest.TestCase):
    def test_example(self):
        n = 5
        expected = 10
        actual = Solution().smallestEvenMultiple(n)
        self.assertEqual(expected, actual, "example1")

    def test_example(self):
        n = 6
        expected = 6
        actual = Solution().smallestEvenMultiple(n)
        self.assertEqual(expected, actual, "example2")
