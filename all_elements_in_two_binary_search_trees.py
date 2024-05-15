"""
All Elements in Two Binary Search Trees
Medium
Topics
Companies
Hint

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

 

Constraints:

    The number of nodes in each tree is in the range [0, 5000].
    -105 <= Node.val <= 105

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        self.result = []

        def loop_tree(node):
            if node is None:
                return
            loop_tree(node.left)
            self.result.append(node.val)
            loop_tree(node.right)

        loop_tree(root1)
        first_result = self.result
        self.result = []
        loop_tree(root2)
        second_result = self.result
        print(first_result, second_result)
        final_result = []
        i = j = 0
        while i < len(first_result) and j < len(second_result):
            if first_result[i] <= second_result[j]:
                final_result.append(first_result[i])
                i += 1
            else:
                final_result.append(second_result[j])
                j += 1

        while i < len(first_result):
            final_result.append(first_result[i])
            i += 1
        while j < len(second_result):
            final_result.append(second_result[j])
            j += 1

        return final_result


root1 = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=4))

root2 = TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=3))

s = Solution()
print(s.getAllElements(root1, root2))
