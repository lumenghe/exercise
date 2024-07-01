"""
Rotate List
Medium
Topics
Companies

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

 

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        length = 0
        current = head
        while current:
            current = current.next
            length += 1

        current = head
        index = 1
        k = k % length
        while current.next:
            if index == (length - k):
                break

            index += 1
            current = current.next

        new_head = current.next
        if new_head is None:
            return head
        current.next = None
        new_current = new_head

        while new_current.next:
            new_current = new_current.next

        new_current.next = head

        return new_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        k = k % length

        last.next = head

        temp = head
        for _ in range(length - k - 1):
            temp = temp.next

        res = temp.next
        temp.next = None
        return res
