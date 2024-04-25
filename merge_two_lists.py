"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_linked_list(list1: list):
    head = prev = ListNode()
    for value in list1:
        current = ListNode(val=value)
        prev.next = current
        prev = current

    return head.next


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    head = prev = ListNode()
    i = j = 0

    while list1 and list2:
        if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    while list1:
        prev.next = list1
        list1 = list1.next
    while list2:
        prev.next = list2
        list2 = list2.next

    return head.next


if __name__ == "__main__":
    list1 = [-9, 3]

    list2 = [5, 7]
    current = merge_two_lists(list1, list2)
    while current:
        print(current.val)
        current = current.next
