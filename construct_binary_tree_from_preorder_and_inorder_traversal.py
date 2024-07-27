"""
Construct Binary Tree from Preorder and Inorder Traversal
Medium
Topics
Companies

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

 

Constraints:

    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def set_sub_tree(sub_preoder, sub_inorder):
            if sub_preoder == []:
                return None
            if len(sub_preoder) == 1:
                return TreeNode(sub_preoder[0])
            root = TreeNode(sub_preoder[0])

            index = sub_inorder.index(sub_preoder[0])
            root.left = set_sub_tree(sub_preoder[1 : index + 1], sub_inorder[:index])
            root.right = set_sub_tree(sub_preoder[index + 1 :], sub_inorder[index + 1 :])
            return root

        return set_sub_tree(preorder, inorder)
