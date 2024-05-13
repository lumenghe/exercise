"""
Count Nodes Equal to Average of Subtree
Medium
Topics
Companies
Hint

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

    The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
    A subtree of root is a tree consisting of root and all of its descendants.

 

Example 1:

Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Example 2:

Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 1000


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_and_number(node):
    if node is None:
        return 0, 0
    return (
        sum_and_number(node.left)[0] + sum_and_number(node.right)[0] + node.val,
        sum_and_number(node.left)[1] + sum_and_number(node.right)[1] + 1,
    )


def averageOfSubtree(root: TreeNode) -> int:
    queue = [(root, sum_and_number(root))]
    res = 0
    while len(queue):
        node, (sumvalue, numbers) = queue.pop(0)
        if node is None:
            continue
        if numbers and node.val == sumvalue // numbers:
            res += 1
        queue.append((node.left, sum_and_number(node.left)))
        queue.append((node.right, sum_and_number(node.right)))

    return res


def better_averageOfSubtree(root: TreeNode) -> int:
    res = 0

    def traverse(node):
        nonlocal res
        if node is None:
            return 0, 0
        left_sum, left_nb = traverse(node.left)
        right_sum, right_nb = traverse(node.right)

        s = left_sum + right_sum + node.val
        nb = left_nb + right_nb + 1
        if s // nb == node.val:
            res += 1
        return s, nb

    traverse(root)
    return res


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(6)
    print(averageOfSubtree(root))
    print(better_averageOfSubtree(root))
