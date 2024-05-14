"""
Find Leaves of Binary Tree
Leetcode Link

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.

Example 1:
Example 1

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

Example 2:

Input: root = [1] Output: [[1]]

Constraints:

    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


leaves = []


def solution(root):
    result = {}

    def dfs(node):
        if node is None:
            return 0
        left_level = dfs(node.left) + 1
        right_level = dfs(node.right) + 1
        level = max(left_level, right_level)
        result.setdefault(level, []).append(node.val)
        return level

    dfs(root)

    return list(result.values())


if __name__ == "__main__":
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
    print(solution(root))
