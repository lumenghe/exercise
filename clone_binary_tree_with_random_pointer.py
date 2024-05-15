"""
Clone Binary Tree With Random Pointer
MediumTreeDepth-First SearchBreadth-First SearchHash TableBinary Tree
Leetcode Link
Problem Description

In this LeetCode problem, we are given a binary tree where each node has an additional feature. Along with the usual left and right child pointers, each node also contains a random pointer. The random pointer can point to any node in the tree or be null.

The task is to create a deep copy of this binary tree. A deep copy means that we need to create a new binary tree that looks exactly like the original tree, but is completely independent of the original. Changes to the new tree should not affect the old one and vice versa. The new nodes' random pointers should point to the corresponding nodes in the copied tree, not the original tree.

Each node in the tree is represented as a pair [val, random_index] where:

    val represents the value of the node.
    random_index is the index of the node to which the random pointer points, or null if the random pointer does not point to any node.

Lastly, the output should be provided using the NodeCopy class, which is essentially a clone of the Node class with identical attributes and constructors.
"""


class Node:

    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


def solution(root):
    clone_map = {}

    def clone_binary_tree(node):
        if node is None:
            return
        if node in clone_map:
            return clone_map[node]
        left = clone_binary_tree(node.left)
        right = clone_binary_tree(node.right)
        random = clone_binary_tree(node.random)
        sub_root = Node(node.val, left=left, right=right, random=random)
        clone_map[node] = sub_root
        return sub_root

    clone_binary_tree(root)
