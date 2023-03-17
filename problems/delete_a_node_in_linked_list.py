"""
Problem:
    Delete the node from a given position of a given linked list.
    Return the head of the updated linked list.
Example:
    Input: "head": [10, 20, 30, 40, 50], "position": 2
    Output: [10, 30, 40, 50]
Constraints:
    1 <= length of the list <= 10^5
    -10^5 <= value in a linked list node <= 10^5
    1 <= value of given position <= length of the list
Solution:
    Inorder to delete the node, we need handle to previous node so we can point it to the next node of deleted node
    To get previous node, iterate the linke list till we reach the position with keeping track of previous node visited.
    Handle edge case where head needs to be deleted, in which case we don't have prev node.

For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
import traceback
import unittest


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node_from_given_position(head, position):
    """
    Args:
     head(LinkedListNode_int32)
     position(int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if position == 1:
        return head.next

    position_prev_node = head
    current_node = head
    node_index = 1
    while node_index < position:
        position_prev_node = current_node
        current_node = current_node.next
        node_index = node_index + 1

    position_prev_node.next = current_node.next

    return head


def build_linked_list(numbers):
    if not numbers:
        return None

    head = LinkedListNode(-1)
    node = head
    for n in numbers:
        node.next = LinkedListNode(n)
        node = node.next
    return head.next


class Testcase(unittest.TestCase):

    def test_example1(self):
        head = build_linked_list([10, 20, 30, 40, 50])
        position = 2
        output = delete_node_from_given_position(head, position)
        try:
            self.assertEqual(10, output.value, "example1: head should be 10")
            self.assertEqual(30, output.next.value, "example1: pos 2 should be 30")
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_beginning(self):
        head = build_linked_list([10, 20, 30, 40, 50])
        position = 1
        output = delete_node_from_given_position(head, position)
        try:
            self.assertEqual(20, output.value, "beginning: head should be 20")
            self.assertEqual(30, output.next.value, "beginning: pos 2 should be 30")
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")

    def test_end(self):
        head = build_linked_list([10, 20, 30, 40, 50])
        position = 5
        output = delete_node_from_given_position(head, position)
        try:
            self.assertEqual(10, output.value, "end: head should be 20")
            self.assertEqual(40, output.next.next.next.value, "end: pos 4 should be 40")
            self.assertEqual(None, output.next.next.next.next, "end: pos 5 should be None")
        except Exception as e:
            traceback.print_exception(e)
            self.assertTrue(False, "not expected!")
