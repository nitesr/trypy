# Problem:
#   https://leetcode.com/problems/sqrtx/
#   Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
#       The returned integer should be non-negative as well.
# Note:
#   You must not use any built-in exponent function or operator.
#   For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
# Example1:
#   Input: x = 4
#   Output: 2
#   Explanation: The square root of 4 is 2, so we return 2.
#
# Example2:
#   Input: x = 8
#   Output: 2
#   Explanation: The square root of 8 is 2.82842...,
#       and since we round it down to the nearest integer, 2 is returned.
#
# Constraints:
#   0 <= x <= 2^31 - 1
import math
import unittest


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Solution:
        #   Brute Force: We know sqrt(x) < x for x > 1,
        #       so we iterator from i=2 to i*i < x and find closet sqrt of x
        #       Time Complexity: O(n). Can we do better ?
        #       since i*i is a monotonically increasing function 1*1 < 2*2 < 3*3
        #           we can apply binary search.
        #
        #   Binary Search:
        #       start with range [2, x] and i = 2 + (x-2)/2
        #           if i*i > x, make range [2, i-1] and repeat
        #           else, make range [i, x] and repeat
        #           stop when range is [i, j] and i > j; j is solution
        #       e.g. 10
        #           Iteration1: range=[2, 10] => i=6 => 6*6 > 10
        #           Iteration2: => range=[2, 5] => i=3 => 3*3 !> 10
        #           Iteration3: => range=[4, 5] => i=4 => 4*4 > 10
        #           Iteration4: => range=[4, 3] => i=3 is solution
        #       e.g. 16
        #           Iteration1: range=[2, 16] => i=8 => 9*9 > 16
        #           Iteration2: => range=[2, 8] => i=5 => 5*5 > 16
        #           Iteration3: => range=[2, 4] => i=3 => 3*3 !> 16
        #           Iteration4: => range=[4, 4] => i=4 => 4*4 !> 16
        #           Iteration5: => range=[3, 4] => i=4 is solution
        if x == 0 or x == 1:
            return x

        low = 2
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1

        return high

    def heroSqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Solution:
        #   We can use Hero's iterative approach to find sqrt to certain precision or error tolerance
        #       approach talks about making the sequence of guesses progressively getting closer to answer
        #       Let's say first guess, g
        #           next guess g` should be closer i.e |x - (g*g)| > |x - (g`*g`)|. How do we get closer ?
        #       if we plot g on a line ->
        #           case 1: ..(x/g)..g..x..(g*g)..  (g*g > x => g > x/g) (next guess g` < g and g` > x/g)
        #           case 2: ..g..(x/g)..(g*g)..x..  (g*g < x => g < x/g) (next guess g` > g and g` < x/g)
        #           case 3: ..(x/g)..x..g..(g*g)..  (g*g > x => g > x/g) (next guess g` < g, g` < x and g` > x/g)
        #           in all the cases, in order to choose g` we can increment/decrement by error tolerance
        #               and get closer to sqrt(x) but we can do better my taking a middle point between g & x/g.
        #               Hero claims that this middle point will be always closer and less than sqrt(x)
        #               irrespective the case. i.e. g` < sqrt(x)
        #
        #       So, we repeatedly compute g`=(g*g + x)/2 till next two guess is within the error tolerance
        #
        # Code Here:
        if x == 0 or x == 1:
            return x

        error_tolerance = 0.1
        guess = x
        next_guess = (guess * guess + x) / (2 * guess)
        while abs(next_guess - guess) > error_tolerance:
            guess = next_guess
            next_guess = (guess * guess + x) / (2 * guess)

        return int(next_guess)


class Testcase(unittest.TestCase):
    def test_example1(self):
        x = 4
        expected = 2
        actual = Solution().mySqrt(x)
        hero_actual = Solution().heroSqrt(x)
        self.assertEqual(expected, actual, "example1")
        self.assertEqual(expected, hero_actual, "example1")

    def test_example2(self):
        x = 8
        expected = 2
        actual = Solution().mySqrt(x)
        hero_actual = Solution().heroSqrt(x)
        self.assertEqual(expected, actual, "example2")
        self.assertEqual(expected, hero_actual, "example2")

    def test_zero(self):
        x = 0
        expected = 0
        actual = Solution().mySqrt(x)
        hero_actual = Solution().heroSqrt(x)
        self.assertEqual(expected, actual, "zero")
        self.assertEqual(expected, hero_actual, "zero")

    def test_one(self):
        x = 1
        expected = 1
        actual = Solution().mySqrt(x)
        hero_actual = Solution().heroSqrt(x)
        self.assertEqual(expected, actual, "one")
        self.assertEqual(expected, hero_actual, "one")

    def test_max(self):
        x = 2 ** 31 - 1
        expected = math.isqrt(x)
        actual = Solution().mySqrt(x)
        hero_actual = Solution().heroSqrt(x)
        self.assertEqual(expected, actual, "max")
        self.assertEqual(expected, hero_actual, "max")
