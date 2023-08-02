class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_linked_list(numbers):
    if not numbers:
        return None

    head = LinkedListNode(-1)
    node = head
    for n in numbers:
        node.next = LinkedListNode(n)
        node = node.next
    return head.next


def traverse_linked_list(head: LinkedListNode, position: int) -> LinkedListNode:
    curr_node = head
    for i in range(1, position):
        if curr_node is not None:
            curr_node = curr_node.next
    return curr_node
