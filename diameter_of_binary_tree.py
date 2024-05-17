"""
Diameter of Binary Tree
Attempted
Easy
Topics
Companies

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def get_level(node):
            if node is None:
                return 0
            left = get_level(node.left)
            right = get_level(node.right)
            return max(left, right) + 1

        left = get_level(root.left)
        right = get_level(root.right)
        print(left, right)
        return left + right


root = TreeNode(
    4,
    left=TreeNode(-7),
    right=TreeNode(
        -3,
        left=TreeNode(-9, right=TreeNode(9, left=TreeNode(6, left=TreeNode(6, left=TreeNode(-1, left=TreeNode(-2)))))),
        right=TreeNode(-3),
    ),
)

c = Solution()
print(c.diameterOfBinaryTree(root))
