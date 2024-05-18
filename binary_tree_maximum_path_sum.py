"""
Binary Tree Maximum Path Sum
Hard
Topics
Companies

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

 

Constraints:

    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionWrong:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def max_sum(node):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                return node.val
            left = max_sum(node.left)
            right = max_sum(node.right)
            return node.val + max(left, right)

        def dfs(node):
            if node is None:
                return 0
            self.max_result = max(self.max_result, max_sum(node.left) + max_sum(node.right) + node.val)
            dfs(node.left)
            dfs(node.right)

        self.max_result = float("-inf")
        dfs(root)
        return self.max_result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(*self.path_rec(root))

    def path_rec(self, root: Optional[TreeNode]):
        if root is None:
            return (None, None)
        left_t, left_b = self.path_rec(root.left)
        right_t, right_b = self.path_rec(root.right)
        t, b = (
            root.val
            + max(
                0, (0 if left_t is None and right_t is None else max([x for x in [left_t, right_t] if x is not None]))
            ),
            max(
                [
                    x
                    for x in [
                        left_b,
                        right_b,
                        ((left_t if left_t is not None else 0) + root.val + (right_t if right_t is not None else 0)),
                        ((left_t if left_t is not None else 0) + root.val),
                        (root.val + (right_t if right_t is not None else 0)),
                        root.val,
                    ]
                    if x is not None
                ]
            ),
        )
        print(root.val, t, b, left_t, left_b, right_t, right_b)
        return t, b
