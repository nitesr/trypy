# Problem:
#   https://leetcode.com/problems/check-if-it-is-a-good-array/
#   Given an array nums of positive integers.
#       Your task is to select some subset of nums, multiply each element by an integer
#       and add all these numbers. The array is said to be good if you can obtain a sum of 1
#       from the array by any possible subset and multiplicand.
#
#   Return True if the array is good otherwise return False.
#
# Example 1:
#   Input: nums = [12,5,7,23]
#   Output: true
#   Explanation: Pick numbers 5 and 7.
#       5*3 + 7*(-2) = 1
# Example 2:
#   Input: nums = [29,6,10]
#   Output: true
#   Explanation: Pick numbers 29, 6 and 10.
#       29*1 + 6*(-3) + 10*(-1) = 1
# Example 3:
#   Input: nums = [3,6]
#   Output: false
#
# Constraints:
#   1 <= nums.length <= 10^5
#   1 <= nums[i] <= 10^9
#
# Solution:
#   if a,b,c, .. are elements of array we need to find if equation
#       ax+by+cz+...= 1 is solvable.
#
#   ax+by=1 is solvable only if a & b are co-prime by Bezout's identity theorem (ax+by=zGCD(a,b)).
#       can we extend to more than one coefficient ?
#       Is ax+by=1 => ax+by+cz=1 true ?
#           ax+by=1 => n(ax+by) = n where n is any integer
#           => a(nx) + b(ny) = n => ax`+by` = n , so I can choose ax`+by` expression to be any integer
#           => if I choose ax+by = (-cz+1) (x` and y` are arbitrary values similar to x and y)
#           => ax+by+cz = (-cz+1)+cz = 1
#       I can extend this argument to any number of coefficients => ax+by+cz+.... = 1
#
#   if there are two numbers in array (a, b, c, ..) which are co-prime then the array is good.
#      We can find all the pairs in the array in order to check it. time complexity - O(log(n^2))
#      Can we do better than that ?
#       if GCD(a, b) = 1 then GCD(a, b, c) should be 1 because 1 is the lowest common factor
#       => if we can find the GCD of the array and if its equal to 1 then the array is good
#               GCD(a, b, c, d, ....) = GCD(GCD(GCD(GCD(a,b), c),d)
#
#   Pseudocode:
#      g = nums[0]
#      for n in nums starting at position 1:
#           g = math.gcd(g, n)
#      if g==1:
#           then array is good
#      else:
#           array is not good.
#
#   Time Complexity:
#       GCD function takes logx(m) where m is max of two numbers
#       T = O(nlogx(m)), where m is max of all the numbers in the array and n is the array length
#   Space Complexity:
#       O(1) - constant
import math
import unittest
from typing import List


class Solution:
    def is_good_array(self, nums: List[int]) -> bool:
        g = nums[0]
        for i in range(1, len(nums)):
            g = math.gcd(nums[i], g)
        if g == 1:
            return True
        else:
            return False


class Testcase(unittest.TestCase):
    def test_example1(self):
        nums = [12, 5, 7, 23]
        expected = True
        actual = Solution().is_good_array(nums)
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        nums = [29, 6, 10]
        expected = True
        actual = Solution().is_good_array(nums)
        self.assertEqual(expected, actual, "example2")

    def test_example3(self):
        nums = [3, 6]
        expected = False
        actual = Solution().is_good_array(nums)
        self.assertEqual(expected, actual, "example3")

    def test_multiples_of_2(self):
        nums = [2, 8, 16, 32]
        expected = False
        actual = Solution().is_good_array(nums)
        self.assertEqual(expected, actual, "multiples_of_2")

    def test_primes(self):
        nums = [2, 5, 7, 11]
        expected = True
        actual = Solution().is_good_array(nums)
        self.assertEqual(expected, actual, "primes")

    def test_sequence(self):
        nums = [5, 6, 7, 8, 9]
        expected = True
        actual = Solution().is_good_array(nums)
        self.assertEqual(expected, actual, "sequence")

    def test_one_pair_of_coprimes_at_extremes(self):
        nums = [5, 15, 20, 9]
        expected = True
        actual = Solution().is_good_array(nums)
        self.assertEqual(expected, actual, "one_pair_of_coprimes_at_extremes")
