"""
Balance a Binary Search Tree
Medium
Topics
Companies
Hint

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 105


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.queue = []

        def loop_bst(node):
            if node is None:
                return
            loop_bst(node.left)
            self.queue.append(node)
            loop_bst(node.right)

        def add_new_tree(queue):
            if not queue:
                return
            mid = len(queue) // 2
            left = add_new_tree(queue[:mid])
            right = add_new_tree(queue[mid + 1 :])
            sub_tree = TreeNode(queue[mid].val, left=left, right=right)
            return sub_tree

        loop_bst(root)
        new_root = add_new_tree(self.queue)
        return new_root
