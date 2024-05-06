"""
Symmetric Tree
Easy
Topics
Companies

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?
"""

from typling import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left


def is_same(left, right) -> None:
    if left is None and right is None:
        return True
    if left is not None or right is not None:
        return False
    if left.val != right.val:
        return False

    return is_same(left.left, right.right) and is_same(left.right, right.left)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """"""

    if root is None:
        return True
    return is_same(root.left, root.right)
