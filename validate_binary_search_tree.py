"""
Validate Binary Search Tree
Medium
Topics
Companies

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def calculate(root: Optional[TreeNode], min_value: int, max_value: int) -> bool:
    if root is None:
        return True
    if min_value >= root.val or root.val >= max_value:
        return False
    return calculate(root=root.left, min_value=min_value, max_value=root.val) and calculate(
        root=root.right, min_value=root.val, max_value=max_value
    )


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """is valid bst"""

    if root is None:
        return True

    return calculate(root, float("-inf"), float("inf"))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float("-inf")

        def dfs(node):
            if node is None:
                return True

            if dfs(node.left) is False:
                return False

            if self.prev >= node.val:
                return False
            self.prev = node.val

            return dfs(node.right)

        return dfs(root)
