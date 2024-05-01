"""
Binary Tree Inorder Traversal
Easy
Topics
Companies

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traveral(root: TreeNode) -> list[int]:
    current = root
    res = []
    queue = []
    while current or queue:
        while current:
            queue.append(current)
            current = current.left

        current = queue.pop()
        res.append(current.val)
        current = current.right

    return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
res = inorder_traveral(root)
print(res)
