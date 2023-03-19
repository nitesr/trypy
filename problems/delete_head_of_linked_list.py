"""
Problem:
   Delete the first node of a given linked list.
   Return the head of the updated linked list.

Example 1:
    Input: "head": [1, 2, 3, 4]
    Output: [2, 3, 4]

Constratints:
    0 <= length of the list <= 10^5
    -10^5 <= value in a linked list node <= 10^5

Solution:
    Pass the next of given head.
    Edgecase - If head is None return same.

For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
import traceback
import unittest
from utils.tools import build_linked_list


def delete_first_node(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    return head.next if head is not None else None


class Testcase(unittest.TestCase):
    def test_example1(self):
        head = build_linked_list([1, 2, 3, 4])
        output = delete_first_node(head)
        try:
            self.assertEqual(2, output.value, "example1: head should be 2")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_empty_list(self):
        head = None
        output = delete_first_node(head)
        try:
            self.assertEqual(None, output, "empty_list: head should be None")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_single_element_list(self):
        head = build_linked_list([1])
        output = delete_first_node(head)
        try:
            self.assertEqual(None, output, "single_element_list: head should be None")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")
