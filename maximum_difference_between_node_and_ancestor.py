"""
Maximum Difference Between Node and Ancestor
Medium
Topics
Companies
Hint

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:

Input: root = [1,null,2,null,0,3]
Output: 3

 

Constraints:

    The number of nodes in the tree is in the range [2, 5000].
    0 <= Node.val <= 105


"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ret = 0

        def dfs(node, max_value, min_value):
            if node is None:
                return float("-inf"), float("inf")

            left_max, left_min = dfs(node.left, max_value, min_value)
            right_max, right_min = dfs(node.right, max_value, min_value)
            min_val = min(node.val, left_min, right_min)
            max_val = max(node.val, left_max, right_max)
            self.ret = max(self.ret, max(node.val - min_val, max_val - node.val))
            return max_val, min_val

        _, _ = dfs(root, float("-inf"), float("inf"))

        return self.ret


class SolutionOther:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        m = [0]
        self.dfs(root, m)
        return m[0]

    def dfs(self, root, m):
        if not root:
            return float("inf"), float("-inf")

        left = self.dfs(root.left, m)
        right = self.dfs(root.right, m)

        min_val = min(root.val, min(left[0], right[0]))
        max_val = max(root.val, max(left[1], right[1]))

        m[0] = max(m[0], max(abs(min_val - root.val), abs(max_val - root.val)))

        return min_val, max_val


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.all_path = []

        def get_path(node, prev):
            if node is None:
                self.all_path.append(prev)
                return
            get_path(node.left, prev + [node.val])
            get_path(node.right, prev + [node.val])

        get_path(root, [])
        result = 0
        for sub_path in self.all_path:
            if sub_path:
                result = max(abs(max(sub_path) - min(sub_path)), result)

        return result


s = Solution()
root = TreeNode(2)
print(s.maxAncestorDiff(root))
