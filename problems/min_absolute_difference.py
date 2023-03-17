# Problem:
#   Given a list of distinct numbers, find all pairs having the minimum absolute difference.
#   return a list of pairs in any order(with respect to pairs), each pair must be sorted in ascending order.
#
# Example1:
#   Input: [2, -2, 4]
#   Output: [[2, 4]]
#
# Example2:
#   Input: [5, 2, 1, 3, 6]
#   Output: [ [1, 2], [2, 3], [5, 6] ]
#
# Constraints:
#   2 <= size of the input list <= 10^5
#   -10^5 <= any element of the input list <= 10^5
import unittest


def get_minimum_abs_difference_pairs(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_list_int32
    """
    # Solution:
    #   Brute force:
    #       Find all the pairs using two nested loops
    #       scan them to find the minimum abs difference, say min_diff
    #       filter the pairs for the min_diff and return
    #       T = O(n^2) S = O(n^2)
    #   Sorting:
    #       on a sorted list of nums
    #           we can find min_diff in a single scan
    #           find pairs with min_diff in single scan
    #       T = O(nlogn+n) S = O(n)
    #
    # Write your code here.

    nums_sorted = nums[:]
    nums_sorted.sort()

    min_diff = 0
    for n in nums:
        min_diff = min_diff + abs(n)

    for i in range(0, len(nums) - 1):
        diff = abs(nums_sorted[i + 1] - nums_sorted[i])
        min_diff = min(diff, min_diff)

    min_diff_pairs = []
    i = 0
    while i < len(nums) - 1:
        diff = abs(nums_sorted[i + 1] - nums_sorted[i])
        if diff == min_diff:
            min_diff_pairs.append([nums_sorted[i], nums_sorted[i + 1]])

        if nums_sorted[i] == nums_sorted[i + 1]:
            while nums_sorted[i] == nums_sorted[i + 1]:
                i = i + 1
        else:
            i = i + 1

    return min_diff_pairs


class Testcase(unittest.TestCase):
    def test_example1(self):
        numbers = [2, -2, 4]
        expected = [[2, 4]]
        actual = get_minimum_abs_difference_pairs(numbers)
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        numbers = [5, 2, 1, 3, 6]
        expected = [[1, 2], [2, 3], [5, 6]]
        actual = get_minimum_abs_difference_pairs(numbers)
        self.assertEqual(expected, actual, "example2")

    def test_only_one_pair(self):
        numbers = [-1000, 1000]
        expected = [[-1000, 1000]]
        actual = get_minimum_abs_difference_pairs(numbers)
        self.assertEqual(expected, actual, "only_one_pair")

    def test_all_negative_pairs(self):
        numbers = [-1, -2, -3, -4, -5]
        expected = [[-5, -4], [-4, -3], [-3, -2], [-2, -1]]
        actual = get_minimum_abs_difference_pairs(numbers)
        self.assertEqual(expected, actual, "all_negative_pairs")
