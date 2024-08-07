"""
Recover Binary Search Tree
Medium
Topics
Companies

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

 

Constraints:

    The number of nodes in the tree is in the range [2, 1000].
    -231 <= Node.val <= 231 - 1

 
Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recover_tree(root: Optional[TreeNode]) -> None:
    """"""
    visited = []
    cur = root
    stack = []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        node = stack.pop()
        visited.append(node)
        cur = node.right

    left = 0
    n = len(visited)
    while visited[left].val < visited[left + 1].val:
        left += 1

    right = n - 1
    while visited[right].val > visited[right - 1].val:
        right -= 1

    visited[left].val, visited[right].val = visited[right].val, visited[left].val


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.path = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            self.path += [node]
            dfs(node.right)

        dfs(root)
        current_value = self.path[0].val
        left = 0
        right = len(self.path) - 1
        while left < (len(self.path) - 1) and self.path[left].val < self.path[left + 1].val:
            left += 1

        while right > 0 and self.path[right].val > self.path[right - 1].val:
            right -= 1

        self.path[left].val, self.path[right].val = self.path[right].val, self.path[left].val
