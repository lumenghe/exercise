"""
Binary Tree Right Side View
Solved
Medium
Topics
Companies

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, level):
            if node is None:
                return
            self.result.setdefault(level, [])
            self.result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        self.result = {}
        dfs(root, 0)
        res = []
        length = len(self.result)
        for index in range(length):
            res.append(self.result[index][-1])

        return res


class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, level):
            if node is None:
                return
            if level not in self.level_list:
                self.result.append(node.val)
                self.level_list.append(level)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        self.level_list = []
        self.result = []
        dfs(root, 0)
        return self.result
