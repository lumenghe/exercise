"""
In this problem, we are given all the nodes of an N-ary tree in the form of an array of Node objects. Each Node has a unique value, and the goal is to determine the root node of the given N-ary tree.

An N-ary tree is a tree in which a node can have any number of children (0 or more). The array provided does not directly show the structure of the tree or the parent-child relationships. Instead, we need to infer which one of these nodes is the root based on the details given.

To aid in this, we have a way to serialize the tree through its level order traversal: each group of children is followed by a null value to indicate the end of that particular level of children. The given example uses serialization to show the structure of an N-ary tree.

Our task is to implement a function, findRoot, which will receive an unsorted array of Node objects and must return the root of the N-ary tree. A key aspect of the problem is that the underlying tree structure is not provided explicitly, and we have to determine the root node without reconstructing the tree.


Given an N-ary tree as a list of nodes Node[] tree. Each node has a unique value, the task is to find the root of the tree.

N-ary tree

Examples:

    Input:          1                   
                    /   |   \              
                  2   3   4           
                  \                    
                  5

    Output: Root value is 1
     

    Input:                5      
                         /     |    \
                       3      6   7
                      /  \    /  \
                     9 2   1 8

    Output: Root value is 5
"""

# The given code is already written in Python 3 syntax, but I will revise it to

# include clearer variable names and add comments to enhance readability.


# Definition for a Node in a tree.


class Node:
    def __init__(self, value=None, children=None):

        self.value = value  # The value contained in the node

        self.children = children if children is not None else []  # Child nodes


# Class to encapsulate the solution methods.


class Solution:

    # Method to find the root of a tree where all nodes are present in an array.

    # The tree has no cycles and each child has exactly one parent, so the root

    # has no parent.

    def findRoot(self, all_nodes: list["Node"]) -> "Node":

        head_list = all_nodes
        for node in all_nodes:
            for child in node.children:
                if child is not None and child in head_list:
                    head_list.remove(child)
        return head_list[0]


# Class to encapsulate the solution methods.


class Solution1:

    # Method to find the root of a tree where all nodes are present in an array.

    # The tree has no cycles and each child has exactly one parent, so the root

    # has no parent.

    def findRoot(self, all_nodes: list["Node"]) -> "Node":

        # Initialize an integer to use it for XOR operation.

        # XOR is used because it cancels out when applied to a pair of the same numbers.

        xor_sum = 0

        # Loop over each node and its children in the list of all nodes.
        for node in all_nodes:

            # XOR the node's value with the xor_sum. If it's the root's value,

            # it will appear only once and stay in the xor_sum as all other non-root

            # nodes will be cancelled out with their children counterpart.

            xor_sum ^= node.value

            # Loop over the children of the current node.

            for child in node.children:
                # XOR each child's value as well, cancelling out their values.

                xor_sum ^= child.value

        # After the above operation, the xor_sum will contain the value of the root node only.

        # Loop over the nodes once more to find the node with the same value as the xor_sum.

        return next(node for node in all_nodes if node.value == xor_sum)


if __name__ == "__main__":
    # Create the nodes for the
    # given example tree
    node1 = Node(5)
    node2 = Node(3)
    node3 = Node(6)
    node4 = Node(7)
    node5 = Node(9)
    node6 = Node(2)
    node7 = Node(1)
    node8 = Node(8)

    # Define the relationships
    # between the nodes
    node1.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node4.children = [node7, node8]

    # Create the list of nodes
    # representing the tree
    tree = [node1, node2, node3, node4, node5, node6, node7, node8]

    c = Solution()
    c1 = Solution1()
    # Find the root of the tree
    root = c.findRoot(tree)
    print(root.value)
    print(c1.findRoot(tree).value)
    tree = [
        Node(1, [Node(3, [Node(2, [Node(4)])]), Node(5), Node(6)]),
        Node(3, [Node(2, [Node(4)])]),
        Node(5),
        Node(6),
        Node(2, [Node(4)]),
        Node(4),
    ]

    # Find the root of the tree
    root = c.findRoot(tree)
    print(root.value)
    print(c1.findRoot(tree).value)
