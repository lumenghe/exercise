"""
Binary Tree Zigzag Level Order Traversal
Medium
Topics
Companies

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionWrong:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ret = {}

        def zigzag(level, node):
            if node is None:
                return

            self.ret.setdefault(level, [])
            self.ret[level].append(node.val)
            if level % 2:
                zigzag(level + 1, node.left)
                zigzag(level + 1, node.right)
            else:
                zigzag(level + 1, node.right)
                zigzag(level + 1, node.left)

        zigzag(0, root)

        print(self.ret)
        return self.ret.values()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ret = {}

        def dfs(level, node):
            if node is None:
                return

            self.ret.setdefault(level, [])
            self.ret[level].append(node.val)

            dfs(level + 1, node.left)
            dfs(level + 1, node.right)

        dfs(0, root)
        for level, value in self.ret.items():
            if level % 2:
                self.ret[level] = value[::-1]
        return self.ret.values()
