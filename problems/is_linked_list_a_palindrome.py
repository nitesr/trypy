"""
Problem:
    Given a singly linked list, check whether it is a palindrome or not.
    A palindrome is a sequence that reads the same backward as forward.

Example 1:
   Input: [0, 2, 4, 4, 2, 0]
   Output: True

Example 2:
    Input: [12, 2, 1]
    Output: False

Constraints:
    1 <= length of the list <= 10^5
    -10^9 <= node values <= 10^9

Solution:
    A palindrome is a sequence that reads the same backward as forward.
    => We need a way to read the list in both directions.

    As the linked list can be read only in one direction,
    => we need to build another list in reverse direction.

    As we compare two halves,
    => we only need to build half the list in reverse direction.

    scan the list to get the size, say n
    scan half the list again and build the list (either arraylist or linked-list in reverse)
    scan the list again from middle out using the two lists, to check for palindrome.

    Make sure for odd size list, we are ignoring the middle element.

For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
import unittest

from problems.utils.tools import build_linked_list


def is_palindrome(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    tail = head
    size = 1
    while tail.next is not None:
        tail = tail.next
        size = size + 1

    half_size = size // 2
    tail = head
    first_half_arr = []
    for i in range(0, half_size):
        first_half_arr.append(tail.value)
        tail = tail.next

    if size % 2 == 1:
        tail = tail.next

    forward = tail
    for i in range(half_size - 1, -1, -1):
        if forward.value != first_half_arr[i]:
            return False
        forward = forward.next

    return True


class Testcase(unittest.TestCase):
    def test_example1(self):
        head = build_linked_list([0, 2, 4, 4, 2, 0])
        expected = True
        actual = is_palindrome(head)
        self.assertEqual(expected, actual, "example1")

    def test_example2(self):
        head = build_linked_list([12, 2, 1])
        expected = False
        actual = is_palindrome(head)
        self.assertEqual(expected, actual, "example2")

    def test_single_element(self):
        head = build_linked_list([12])
        expected = True
        actual = is_palindrome(head)
        self.assertEqual(expected, actual, "single_element")

    def test_two_elements(self):
        head = build_linked_list([12, 12])
        expected = True
        actual = is_palindrome(head)
        self.assertEqual(expected, actual, "two_elements")

    def test_three_elements(self):
        head = build_linked_list([12, 13, 12])
        expected = True
        actual = is_palindrome(head)
        self.assertEqual(expected, actual, "three_elements")