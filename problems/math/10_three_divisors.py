# Problem:
#   https://leetcode.com/problems/three-divisors/
#   Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
#   An integer m is a divisor of n if there exists an integer k such that n = k * m.
#
# Example1:
#   Input: n = 2
#   Output: false
#   Explanation: 2 has only two divisors: 1 and 2.
#
# Example2:
#   Input: n = 4
#   Output: true
#   Explanation: 4 has three divisors: 1, 2, and 4.
#
# Constraints:
#   1 <= n <= 10^4
import unittest


class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Solution:
        #   This is a factorization problem where the number of factors should be 3
        #   For any given n, 1 & n will be its factors, so we need find only one additional factor
        #       which should be multiplied by itself i.e. sqrt(n)
        #       also, sqrt(n) should be prime so its can't be further factored
        #   so n should be a perfect square of a prime number
        #   n < 10000 => sqrt(n) < 100
        #   we can check for all prime numbers under 100 and check if square of it is equal to n
        #
        # Code Here:
        primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                            97]
        for prime in primes_under_100:
            if prime * prime == n:
                return True
        return False


class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 2
        expected = False
        actual = Solution().isThree(n)
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        n = 4
        expected = True
        actual = Solution().isThree(n)
        self.assertEqual(expected, actual, "example2")

    def test_perfect_square_of_prime(self):
        n = 53 * 53
        expected = True
        actual = Solution().isThree(n)
        self.assertEqual(expected, actual, "perfect_square_of_prime")

    def test_perfect_square_of_non_prime(self):
        n = 8 * 8
        expected = False
        actual = Solution().isThree(n)
        self.assertEqual(expected, actual, "perfect_square_of_non_prime")

    def test_composite_number(self):
        n = 90
        expected = False
        actual = Solution().isThree(n)
        self.assertEqual(expected, actual, "composite_number")

    def test_one(self):
        n = 1
        expected = False
        actual = Solution().isThree(n)
        self.assertEqual(expected, actual, "one")
