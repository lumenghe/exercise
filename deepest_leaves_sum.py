"""
Deepest Leaves Sum
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the sum of values of its deepest leaves.

 

Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 100


"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    ans = 0
    current_level = 0
    q = [(root, 0)]
    while len(q) != 0:
        current, max_level = q.pop(0)
        if max_level > current_level:
            current_level = max_level
            ans = 0
        ans += current.val
        if current.left is not None:
            q.append((current.left, max_level + 1))
        if current.right is not None:
            q.append((current.right, max_level + 1))
    return ans


class Solution:
    def sum_and_level(self, node, level):
        if node.left is None and node.right is None:
            return node.val, level

        if node.left and node.right is None:
            left_sum, left_level = self.sum_and_level(node.left, level + 1)
            return left_sum, left_level
        if node.right and node.left is None:
            right_sum, right_level = self.sum_and_level(node.right, level + 1)
            return right_sum, right_level
        left_sum, left_level = self.sum_and_level(node.left, level + 1)
        right_sum, right_level = self.sum_and_level(node.right, level + 1)
        if left_level == right_level:
            return left_sum + right_sum, left_level
        if left_level > right_level:
            return left_sum, left_level
        else:
            return right_sum, right_level

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        res, level = self.sum_and_level(root, 1)
        return res
