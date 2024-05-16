"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):   
        def dfs(prev):
            if prev.left is None and prev.right is None:
                return
            prev.left.val = prev.val * 2 + 1
            prev.right.val = prev.val *2 + 2
            dfs(prev.left)
            dfs(prev.right)
        self.root = dfs(root)
    
        
    
    def find(self, target: int) -> bool:
        
        def find_dfs(node):
            if node is None:
                return False
            if node.val == target:
                return True
            left_found = find_dfs(node.left)
            right_found = find_dfs(node.right)
            return left_found or right_found 
        
        return find_dfs(self.root)


        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def dfs(prev):
            if prev.left is None and prev.right is None:
                return
            if prev.left:
                prev.left.val = prev.val * 2 + 1
                dfs(prev.left)
            if prev.right:
                prev.right.val = prev.val * 2 + 2
                dfs(prev.right)

        root.val = 0
        dfs(root)
        self.root = root

    def find(self, target: int) -> bool:
        def find_dfs(node):
            if node is None:
                return False
            if node.val == target:
                return True
            left_found = find_dfs(node.left)
            right_found = find_dfs(node.right)
            return left_found or right_found

        return find_dfs(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
