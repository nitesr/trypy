# Problem:
#   Given an array of numbers, find a non-empty subarray that adds to a given target sum.
#   if exists return the indices of first & last element of the subarray otherwise return [-1]
# Examples:
#   Example1:
#   Input: nums = [1, 4, 20, 3, 10] target_sum = 6
#   Output: [-1]
#   Explanation: no sub-array exists with target_sum
#
#   Example2:
#   Input: nums = [1, 2, 3] target_sum = 3
#   Output: [0, 1]
#   Explanation: no sub-array exists with target_sum
#
# Contraints:
#   1 <= size of the input array <= 10^5
#   1 <= any element of the input array <= 10^4
#   1 <= target sum <= 10^9
import unittest


def find_subarray_with_sum(nums, target_sum):
    """
    Args:
     nums(list_int32)
     target_sum(int32)
    Returns:
     list_int32
    """
    # Solution:
    #   use sliding window to compute the sum and compare with target_sum
    #   if window sum > target_sum, reduce the window to min size (i.e. 1)
    #   if window sum == target_sum, return the left and right pointers
    #   if no window exists return [-1]
    #
    # Write your code here.
    left_ptr = 0
    window_sum = 0
    right_ptr = 0

    while right_ptr < len(nums):
        window_sum = window_sum + nums[right_ptr]

        while window_sum > target_sum and left_ptr < right_ptr:
            window_sum = window_sum - nums[left_ptr]
            left_ptr = left_ptr + 1

        if window_sum == target_sum:
            return [left_ptr, right_ptr]

        right_ptr = right_ptr + 1

    return [-1]


class TestCase(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3]
        target_sum = 3
        actual = find_subarray_with_sum(nums, target_sum)
        expected = [0, 1]
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        nums = [1, 4, 20, 3, 10]
        target_sum = 6
        actual = find_subarray_with_sum(nums, target_sum)
        expected = [-1]
        self.assertEqual(expected, actual, "example2")

    def test_size_1_first_window_match(self):
        nums = [1, 4, 20, 3, 10]
        target_sum = 1
        actual = find_subarray_with_sum(nums, target_sum)
        expected = [0, 0]
        self.assertEqual(expected, actual, "size_1_first_window_match")

    def test_size_3_first_window_match(self):
        nums = [1, 4, 20, 3, 10]
        target_sum = 25
        actual = find_subarray_with_sum(nums, target_sum)
        expected = [0, 2]
        self.assertEqual(expected, actual, "size_3_first_window_match")

    def test_size_1_mid_window_match(self):
        nums = [1, 4, 20, 3, 10]
        target_sum = 20
        actual = find_subarray_with_sum(nums, target_sum)
        expected = [2, 2]
        self.assertEqual(expected, actual, "size_1_mid_window_match")

    def test_size_3_mid_window_match(self):
        nums = [1, 4, 20, 3, 10]
        target_sum = 23
        actual = find_subarray_with_sum(nums, target_sum)
        expected = [2, 3]
        self.assertEqual(expected, actual, "size_3_mid_window_match")

    def test_size_1_last_window_match(self):
        nums = [1, 4, 20, 3, 10]
        target_sum = 10
        actual = find_subarray_with_sum(nums, target_sum)
        expected = [4, 4]
        self.assertEqual(expected, actual, "size_1_last_window_match")

    def test_size_3_last_window_match(self):
        nums = [1, 4, 20, 3, 10]
        target_sum = 13
        actual = find_subarray_with_sum(nums, target_sum)
        expected = [3, 4]
        self.assertEqual(expected, actual, "size_3_last_window_match")
