"""
Add Two Numbers
Medium
Topics
Companies

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]



Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.


"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    current1 = l1
    i = j = 0
    num1 = num2 = 0
    while current1:
        num1 += current1.val * (10**i)
        current1 = current1.next
        i += 1

    current2 = l2
    while current2:
        num2 += current2.val * (10**j)
        current2 = current2.next
        j += 1
    sum_list = num1 + num2
    print(num1, num2)
    print(sum_list)
    head = prev = ListNode()
    while sum_list // 10 != 0:
        current = ListNode(val=sum_list % 10)
        sum_list //= 10
        prev.next = current
        prev = current

    prev.next = ListNode(val=sum_list % 10)

    return head.next


def make_linked_list(list1: list):
    head = prev = ListNode()
    for value in list1:
        current = ListNode(val=value)
        prev.next = current
        prev = current
    return head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        new_head = ListNode()
        prev = new_head
        flag = 0

        while current1 and current2:
            current_sum = current1.val + current2.val + flag
            flag = 0
            if current_sum >= 10:
                current_sum %= 10
                flag = 1
            prev.next = ListNode(current_sum)
            prev = prev.next
            current1 = current1.next
            current2 = current2.next

        while current1:
            current_sum = current1.val + flag
            flag = 0
            if current_sum >= 10:
                current_sum %= 10
                flag = 1
            prev.next = ListNode(current_sum)
            prev = prev.next
            current1 = current1.next

        while current2:
            current_sum = current2.val + flag
            flag = 0
            if current_sum >= 10:
                current_sum %= 10
                flag = 1
            prev.next = ListNode(current_sum)
            prev = prev.next
            current2 = current2.next

        if flag:
            prev.next = ListNode(1)
        return new_head.next


if __name__ == "__main__":
    list1 = [2, 4, 3]
    list1 = make_linked_list(list1)

    list2 = [5, 6, 4]
    list2 = make_linked_list(list2)
    sum = add_two_numbers(list1, list2)
    while sum:
        print(sum.val)
        sum = sum.next
    print(10**0)
    print(10**1)
    print(10 ^ 1)
