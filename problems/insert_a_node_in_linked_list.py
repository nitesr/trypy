"""
Problem:
    Given a linked list, insert a given number at a given position in the list.
    Return the head of the modified linked list.

Example 1:
    Input:
        "head": [55, 67, 32, 78, 97, 34],
        "num": 9,
        "position": 7
    Output: [55, 67, 32, 78, 97, 34, 9]

Example 2:
    Input:
        "head": [10, 12, 15, 14, 13],
        "num": 11,
        "position": 3
    Output: [10, 12, 11, 15, 14, 13]

Constraints:
    0 <= length of the list <= 10^5
    0 <= value in a linked list node <= 10^5
    0 <= number to be inserted <= 10^5
    1 <= position <= length of the list + 1

Solution:
    inorder to insert we need previous node to the insert position
    we can iterate and keep track of the previous node to current node.
    Once you find the previous node, say prev_pos_node for position node, say pos_node
    you can insert the node, new_node by changing pointers
        prev_pos_node.next = new_node
        new_node.next = pos_node

    look out for edge cases - insert at head or tail, insert in empty list
    at head: new_node.next = head and new_node is new head
    at tail: as pos_node is None, new_node.next will be None.
    in empty list: same as insert at head edge case.

For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
import traceback
import unittest

from utils.tools import LinkedListNode, build_linked_list, traverse_linked_list as traverse


def insert_at_given_position(head, num, position):
    """
    Args:
     head(LinkedListNode_int32)
     num(int32)
     position(int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    new_node = LinkedListNode(num)
    if position == 1:
        new_node.next = head
        return new_node

    prev_pos_node = None
    pos_node = head
    i = 1
    while i < position and pos_node is not None:
        prev_pos_node = pos_node
        pos_node = pos_node.next
        i = i + 1

    prev_pos_node.next = new_node
    new_node.next = pos_node

    return head


class Testcase(unittest.TestCase):
    def test_example1(self):
        head = build_linked_list([55, 67, 32, 78, 97, 34])
        num = 9
        position = 5
        output = insert_at_given_position(head, num, position)
        try:
            self.assertEqual(55, output.value, "example1: head should be 55")
            self.assertEqual(num, traverse(output, 5).value, "example1: Pos 5 should be 9")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_example2(self):
        head = build_linked_list([10, 12, 15, 14, 13])
        num = 11
        position = 3
        output = insert_at_given_position(head, num, position)
        try:
            self.assertEqual(10, output.value, "example2: head should be 10")
            self.assertEqual(num, traverse(output, 3).value, "example2: Pos 3 should be 11")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_insert_at_head(self):
        head = build_linked_list([10, 12, 15, 14, 13])
        num = 11
        position = 1
        output = insert_at_given_position(head, num, position)
        try:
            self.assertEqual(11, output.value, "insert_at_head: head should be 11")
            self.assertEqual(10, traverse(output, 2).value, "insert_at_head: Pos 1 should be 10")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_empty_list(self):
        head = None
        num = 11
        position = 1
        output = insert_at_given_position(head, num, position)
        try:
            self.assertEqual(11, output.value, "empty_list: head should be 11")
            self.assertEqual(None, traverse(output, 2), "empty_list: next to head should be None")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_insert_at_tail(self):
        head = build_linked_list([10, 12, 15, 14, 13])
        num = 11
        position = 6
        output = insert_at_given_position(head, num, position)
        try:
            self.assertEqual(10, output.value, "insert_at_tail: head should be 11")
            self.assertEqual(num, traverse(output, 6).value, "insert_at_tail: tail should be 11")
        except AssertionError as e:
            raise e
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")