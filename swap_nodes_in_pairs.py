"""
Swap Nodes in Pairs
Medium
Topics
Companies

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

 

Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev, current, ans = None, head, head.next

        while current and current.next:
            adj = current.next
            if prev:
                prev.next = adj
            current.next, adj.next = adj.next, current
            prev, current = current, current.next

        return ans or head


s = Solution()
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4))))
current = s.swapPairs(head)
s = ""
while current:
    s += f" {current.val}"
    current = current.next

print(s)
