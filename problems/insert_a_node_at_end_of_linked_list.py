"""
Problem:
    Given a linked list, insert a given number at the end of the list.
    Return the head of the modified linked list.

Example 1:
    Input:
        "head": [50, 40, 30, 20, 10],
        "num": 60
    Output:
        [50, 40, 30, 20, 10, 60]

Constraints:
    0 <= length of the list <= 10^5
    0 <= value in a linked list node <= 10^5
    0 <= number to be inserted <= 10^5

Solution:
    We need the tail of the list to add a node next to tail.
    traverse the list till the next node is None, which will be the tail.
    and add new node to tail.

    In case the list is empty, the new node will be the new head.

For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
import traceback
import unittest

from problems.utils.tools import build_linked_list, traverse_linked_list as traverse, LinkedListNode


def insert_at_end(head, num):
    """
    Args:
     head(LinkedListNode_int32)
     num(int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    new_node = LinkedListNode(num)

    if head is None:
        return new_node

    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = new_node

    return head


class Testcase(unittest.TestCase):
    def test_example1(self):
        head = build_linked_list([50, 40, 30, 20, 10])
        num = 60
        output = insert_at_end(head, num)
        try:
            self.assertEqual(50, output.value, "example1: head should be 55")
            self.assertEqual(num, traverse(output, 6).value, "example1: tail should be 60")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_single_element(self):
        head = build_linked_list([10])
        num = 11
        output = insert_at_end(head, num)
        try:
            self.assertEqual(10, output.value, "single_element: head should be 10")
            self.assertEqual(11, traverse(output, 2).value, "single_element: tail should be 11")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_empty_list(self):
        head = None
        num = 11
        output = insert_at_end(head, num)
        try:
            self.assertEqual(11, output.value, "empty_list: head should be 11")
            self.assertEqual(None, output.next, "empty_list: next to head should be None")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")