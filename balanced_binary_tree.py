"""
Balanced Binary Tree
Easy
Topics
Companies

Given a binary tree, determine if it is
height-balanced
.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104

"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_count(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return max(dfs_count(root.left), dfs_count(root.right)) + 1


def is_balanced(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    if abs(dfs_count(root.left) - dfs_count(root.right)) <= 1:
        return is_balanced(root.left) and is_balanced(root.right)
    return False


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def get_depth(node):
            if node is None:
                return 0
            left = get_depth(node.left)
            right = get_depth(node.right)
            self.is_balanced = (abs(left - right) <= 1) and self.is_balanced
            return max(left, right) + 1

        get_depth(root)
        return self.is_balanced
