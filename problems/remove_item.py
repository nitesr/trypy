# Problem:
#   Remove all occurrences of a specific item from a list.
#
# Constraints:
#   1 <= length of list1 <= 10^5
#   -1000 <= list1[i] <= 1000
#
# Example:
#   Input: list1 = [5, 20, 15, 20, 25, 50, 20]  item=20
#   Output: [5, 15, 25, 50]

import unittest


def swap(list1, src_pos, dest_pos):
    temp = list1[src_pos]
    list1[src_pos] = list1[dest_pos]
    list1[dest_pos] = temp


def remove_item(list1, item) -> list:
    """
    Args:
     list1(list_int32)
     item(int32)
    Returns:
     list_int32
    """

    non_item_index = -1

    for i in range(0, len(list1)):
        if list1[i] != item:
            non_item_index = non_item_index + 1
            swap(list1, non_item_index, i)

    for i in range(len(list1) - 1, non_item_index, -1):
        list1.pop(i)

    return list1


class Test(unittest.TestCase):
    def test_example1(self):
        result = remove_item([5, 20, 15, 20, 25, 50, 20], 20)
        self.assertEqual([5, 15, 25, 50], result, "Example1")

    def test_example2(self):
        result = remove_item([5], 20)
        self.assertEqual([5], result, "Example 2")

    def test_example3(self):
        result = remove_item([20, 20], 20)
        self.assertEqual([], result, "Example 3")