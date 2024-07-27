"""

Subtree of Another Tree
Solved
Easy
Topics
Companies
Hint

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

 

Constraints:

    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_sub_tree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None and node2 is not None:
                return False
            if node1 is not None and node2 is None:
                return False
            left = check_sub_tree(node1.left, node2.left)
            right = check_sub_tree(node1.right, node2.right)
            return left and right and (node1.val == node2.val)

        def dfs(node):
            if self.subRoot is None:
                return True
            if node is None:
                return False
            if check_sub_tree(node, self.subRoot):
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right

        self.subRoot = subRoot
        return dfs(root)
