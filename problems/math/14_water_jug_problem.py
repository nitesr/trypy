# Problem:
#   https://leetcode.com/problems/water-and-jug-problem/
#   You are given two jugs with capacities jug1Capacity and jug2Capacity liters.
#       There is an infinite amount of water supply available.
#       Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.
#
#   If targetCapacity liters of water are measurable,
#       you must have targetCapacity liters of water contained within one or both buckets by the end.
#
#   Operations allowed:
#   Fill any of the jugs with water.
#   Empty any of the jugs.
#   Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
#
# Example 1:
#   Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
#   Output: true
#   Explanation: The famous Die Hard example
# Example 2:
#   Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
#   Output: false
# Example 3:
#   Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
#   Output: true
#
# Constraints:
#   1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
#
# Solution:
#   For Example 1,
#       I can take j1=3 pour to j2 and then take another j1=3 pour to j2, so I have j1=(3+3-5)=1
#           and j2=5 which I can throw away. so I have one unit of water between j1 & j2.
#           in order to get to the target=4, I need to repeat this 4x(3+3-5) times.
#
#           How many times I can do like this ? can I do till max capacity = 8 (j1+j2)
#               after 3 times, 3x(3+3-5) leaves 3 units in j1
#               4th: j2=3, take j1=3 and pour to j2, so I have j1=(3+3-5) & j2=5, throw away j2
#                       and transfer j1 to j2 (j2=1 & j1=0). take j1=3, so I have j1+j2=(3+1)=4
#                       summarize: start=3 (j1=3, j2=0) => 3+3-5 (+j1 twice & -j2 once) =>  end=4 (j1=3, j2=1)
#               5th: j2=4, j1=0;  +j1,-j2 => j1=2,j2=0; j1->j2 and +j1 => j2=2,j1=3 (5)
#               6th: j2=5, j1=0;  +j1,-j2 => j1=3,j2=0; j1->j2 and +j1 => j2=3,j1=3 (6)
#               7th: j2=5, j1=1;  +j1,-j2 => j1=3,j2=1; j1->j2 and +j1 => j2=4,j1=3 (7)
#               8th: j2=5, j1=2;  +j1,-j2 => j1=3,j2=2; j1->j2 and +j1 => j2=5,j1=3 (8)
#               It looks like we can do it ? but why ?
#                   what we did effectively add j1 x times and subtract j2 y times to get to the target t
#                   => 3x + 5y = t, where x, y are integers and t >= 0
#                   => 3(2) + 5(-1) = 1
#                   => 3(4) + 5(-2) = 2 => t[3(2) + 5(-1)] = t => we can do t times to get to t
#
#   To generalize,
#       given, ax + by = d where a, b are known and d is derived
#       we can solve the equation ax' + by' = t only when t is multiple of d
#       how do we derive d ? Based on Bezout's identity theorem the d is the greatest common
#           divisor of a and b i.e. ax + by = GCD(a, b) where x,y are integers
#
#    So the solution is to get GCD(a, b) and check if GCD(a, b) divides target
#    Note: edge case where target exceeds max capacity (a+b) then we can't solve it.
import unittest
import math

class Solution:
    def can_measure_water(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity+jug2Capacity < targetCapacity:
            return False

        gcd_of_j1_and_j2 = math.gcd(jug1Capacity, jug2Capacity)
        return targetCapacity % gcd_of_j1_and_j2 == 0


class Testcase(unittest.TestCase):
    def test_example1(self):
        j1 = 3
        j2 = 5
        t = 4
        expected = True
        actual = Solution().can_measure_water(j1, j2, t)
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        j1 = 2
        j2 = 6
        t = 5
        expected = False
        actual = Solution().can_measure_water(j1, j2, t)
        self.assertEqual(expected, actual, "example2")

    def test_example3(self):
        j1 = 1
        j2 = 2
        t = 3
        expected = True
        actual = Solution().can_measure_water(j1, j2, t)
        self.assertEqual(expected, actual, "example3")

    def test_co_prime(self):
        j1 = 10
        j2 = 9
        t = 8
        expected = True
        actual = Solution().can_measure_water(j1, j2, t)
        self.assertEqual(expected, actual, "co_prime")

    def test_multiples_true(self):
        j1 = 20
        j2 = 5
        t = 15
        expected = True
        actual = Solution().can_measure_water(j1, j2, t)
        self.assertEqual(expected, actual, "multiples_true")

    def test_multiples_false(self):
        j1 = 20
        j2 = 5
        t = 16
        expected = False
        actual = Solution().can_measure_water(j1, j2, t)
        self.assertEqual(expected, actual, "multiples_false")

    def test_co_prime_exceeds_max(self):
        j1 = 9
        j2 = 5
        t = 15
        expected = False
        actual = Solution().can_measure_water(j1, j2, t)
        self.assertEqual(expected, actual, "co_prime_exceeds_max")