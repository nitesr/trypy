# Problem:
#   Given a list of integers, find the index at which the
#       sum of the left part of the array is equal to the right part.
#   Return the leftmost such index. If no such index exists, return -1.

# Constraints:
#   1 <= length of numbers <= 10^5
#   -1000 <= numbers[i] <= 1000

# Example 1:
#   Input: [1, 5, 3, 6, 3, 6]
#   Output: 3
#   Explanation: sum([1, 5, 3]) == sum([3, 6])

import unittest


def find_equilibrium_index(numbers) -> int:
    """
        Args:
         numbers(list_int32)
        Returns:
         int32
        """
    # Write your code here. _ _ _ _ _

    total_sum = 0
    for i in range(0, len(numbers)):
        total_sum = total_sum + numbers[i]

    equilb_index = 0
    left_sum = 0
    right_sum = total_sum - numbers[equilb_index]
    if left_sum == right_sum:
        return 0

    while equilb_index < len(numbers) - 1:
        left_sum = left_sum + numbers[equilb_index]
        equilb_index = equilb_index + 1
        right_sum = right_sum - numbers[equilb_index]
        if left_sum == right_sum:
            return equilb_index

    return -1


class Test(unittest.TestCase):
    def test_example1(self):
        result = find_equilibrium_index([1, 5, 3, 6, 3, 6])
        self.assertEqual(3, result, "Example 1")

    def test_example2(self):
        result = find_equilibrium_index([3, 7, 1, 7, 2, 4, 1, 5, 8, 6, 6, 8, 3, 4, 2, 1])
        self.assertEqual(8, result, "Example 2")

    def test_example3(self):
        result = find_equilibrium_index([6, -4, -1, -4, 1, 1, 1, 0, 1, 3, -1])
        self.assertEqual(2, result, "Example 3")

    def test_example4(self):
        result = find_equilibrium_index([1, 0, 1])
        self.assertEqual(1, result, "Example 4")

    def test_example5(self):
        result = find_equilibrium_index([1, -1, 1])
        self.assertEqual(0, result, "Example 5")

    def test_example6(self):
        result = find_equilibrium_index([1, 2, 3])
        self.assertEqual(-1, result, "Example 6")
