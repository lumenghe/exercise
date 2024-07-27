"""
Clone N-ary Tree
MediumTreeDepth-First SearchBreadth-First SearchHash Table
Leetcode Link
Problem Description

In this problem, we are given the root of an N-ary tree and asked to create a deep copy of it. A deep copy means that we should create an entirely new tree, where each node is a new instance with the same values as the corresponding nodes in the original tree. In other words, modifying the new tree should not affect the original tree.

An N-ary tree is a tree in which a node can have zero or more children. This differs from a binary tree where each node has at most two children. Each node in an N-ary tree holds a value and a list of nodes that represent its children.

The tree is represented using a custom Node class. The Node class consists of two attributes:

    val: an integer representing the value of the node.
    children: a list of child nodes.

We are to perform the deep copy without altering the structure or values of the original tree
"""


class Node:
    def __init__(self, value=None, children=None):
        """

        Node structure for N-ary tree with optional value and children list arguments.

        :param value: value of the node, defaulted to None

        :param children: list of child nodes, defaulted to empty list if None

        """

        self.value = value

        self.children = [] if children is None else children

    def __str__(self):
        s = str(self.value)
        for child in self.children:
            s += " " + child.__str__()
        return s


def clone_n_ary_tree(node):
    if node is None:
        return None
    if node.children == []:
        return Node(value=node.value)
    new_node = Node(value=node.value, children=[])
    for child in node.children:
        new_child = clone_n_ary_tree(child)
        new_node.children.append(new_child)
    return new_node


if __name__ == "__main__":
    original = Node(value=1, children=[Node(value=2, children=[Node(value=4)]), Node(value=3)])
    new = clone_n_ary_tree(original)
    print(new)
