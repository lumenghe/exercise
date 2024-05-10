"""
Insert a node at a specific position in a linked list


This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.

Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its

attribute, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

Example
refers to the first node in the list

Insert a node at position with . The new list is

Function Description Complete the function insertNodeAtPosition in the editor below. It must return a reference to the head node of your finished list.

insertNodeAtPosition has the following parameters:

    head: a SinglyLinkedListNode pointer to the head of the list
    data: an integer value to insert as data in your new node
    position: an integer position to insert the new node, zero based indexing

Returns

    SinglyLinkedListNode pointer: a reference to the head of the revised list

Input Format

The first line contains an integer
, the number of elements in the linked list.
Each of the next lines contains an integer SinglyLinkedListNode[i].data.
The next line contains an integer , the data of the node that is to be inserted.
The last line contains an integer

.

Constraints

, where is the
element of the linked list.

    .

Sample Input

3
16
13
7
1
2

Sample Output

16 13 1 7

Explanation

The initial linked list is
. Insert at the position which currently has in it. The updated linked list is .
"""

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = llist
        return new_node
    current = llist
    for index in range(position - 1):
        current = current.next

    current_next = current.next
    new_node.next = current_next
    current.next = new_node

    return llist
