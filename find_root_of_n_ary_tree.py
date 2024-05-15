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
