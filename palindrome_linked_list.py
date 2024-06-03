"""
Palindrome Linked List
Solved
Easy
Topics
Companies

Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.

 

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

 

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        nextt = None
        current = head

        while current:
            new_current = ListNode(val=current.val, next=nextt)
            nextt = new_current
            current = current.next
        current = head
        while current and nextt:
            if current.val != nextt.val:
                return False

            current = current.next
            nextt = nextt.next

        if current is None and nextt is None:
            return True
        return False
