# Problem:
#   Check if any element occurs more than once in a given list of numbers.
#
# Example:
#   Input: [10, 30, 10, 20]
#   Output: 1
#   Explanation: 10 is repeated more than once in the array
#
# Constraints:
#   1 <= size of the input list <= 10^5
#   0 <= any element of the input list <= 10^5
import unittest


def check_if_array_contains_duplicate(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     bool
    """
    # Solution:
    #   add the elements to the set and check if already exists to return the result

    # Write your code here.
    nums_set = set()
    for n in nums:
        if n in nums_set:
            return True
        else:
            nums_set.add(n)

    return False


class Testcase(unittest.TestCase):
    def test_example(self):
        nums = [10, 30, 10, 20]
        actual = check_if_array_contains_duplicate(nums)
        expected = True
        self.assertEqual(expected, actual, "example")

    def test_single_element(self):
        nums = [10]
        actual = check_if_array_contains_duplicate(nums)
        expected = False
        self.assertEqual(expected, actual, "single_element")

    def test_single_element_repeated(self):
        nums = [10, 10]
        actual = check_if_array_contains_duplicate(nums)
        expected = True
        self.assertEqual(expected, actual, "single_element_repeated")

    def test_multi_element_no_duplicates(self):
        nums = [10, 20, 30, 40, 50]
        actual = check_if_array_contains_duplicate(nums)
        expected = False
        self.assertEqual(expected, actual, "multi_element_no_duplicates")
