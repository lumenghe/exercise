"""
Path Sum II
Medium
Topics
Companies

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000


"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count(node: TreeNode) -> list[list[int]]:
    if node is None:
        return []

    if node.left is None and node.right is None:
        return [[node.val]]

    all_count = []
    for solution in count(node.left):
        all_count.append([node.val] + solution)

    for solution in count(node.right):
        all_count.append([node.val] + solution)

    return all_count


def path_sum(self, root: Optional[TreeNode], target_sum: int) -> list[list[int]]:
    result = []
    for solution in count(root):
        if sum(solution) == target_sum:
            result.append(solution)
    return result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionWrong:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ret = []

        if root is None:
            return []

        def dfs(node, path, path_sum):
            if node is None:
                if path_sum == targetSum and path not in self.ret:
                    self.ret.append(path)
                return

            dfs(node.left, path + [node.val], path_sum + node.val)
            dfs(node.right, path + [node.val], path_sum + node.val)

        dfs(root, [], 0)

        return self.ret
# this solution is wrong as
# root = [1,2], targetSum=1
#my solution is [[1]]. expected is []
