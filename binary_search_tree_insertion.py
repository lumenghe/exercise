"""
You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree. You just have to complete the function.

Input Format

You are given a function,

Node * insert (Node * root ,int data) {

}

Constraints

    No. of nodes in the tree 

    500

Output Format

Return the root of the binary search tree after inserting the value into the tree.

Sample Input

        4
       / \
      2   7
     / \
    1   3

The value to be inserted is 6.

Sample Output

         4
       /   \
      2     7
     / \   /
    1   3 6
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        # Enter you code here.
        if self.root is None:
            self.root = Node(val)
            return
        prev = None
        current = self.root
        while current:
            prev = current
            if current.info > val:
                current = current.left
            else:
                current = current.right

        if prev.info > val:
            prev.left = Node(val)
        else:
            prev.right = Node(val)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
