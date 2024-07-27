"""
Lowest Common Ancestor of a Binary Tree IV
Description

Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
Output: 1
Explanation: The lowest common ancestor of a single node is the node itself.

Example 3:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
Output: 5
Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -109 <= Node.val <= 109
    All Node.val are unique.
    All nodes[i] will exist in the tree.
    All nodes[i] are distinct.
"""


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        def dfs(node, target, node_path):
            if node is None:
                return []
            elif node.val == target.val:
                return node_path + [node]
            left_path = dfs(node.left, target, node_path + [node])
            right_path = dfs(node.right, target, node_path + [node])
            if left_path:
                return left_path
            if right_path:
                return right_path
            return []

        node_map = {}
        for node in nodes:
            node_map[node] = dfs(root, node, [])

        def find_parent(node_map, nodes):
            for key, value in node_map.items():
                print(key.val, [v.val for v in value])
            # print([node.val for node in nodes])
            for index, sub_path in enumerate(node_map[nodes[0]]):
                for key, value in node_map.items():
                    if len(value) <= index:
                        return node_map[nodes[0]][index - 1]
                    if value[index] != sub_path:
                        return node_map[nodes[0]][index - 1]

        res = find_parent(node_map, nodes)
        return res


s = Solution()
node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node2.left = node7
node2.right = node4
node1.left = node0
node1.right = node8


print(s.lowestCommonAncestor(node3, [node0, node1, node5, node6]).val)
print(s.lowestCommonAncestor(node3, [node7, node2, node5, node6]).val)
