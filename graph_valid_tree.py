"""
Problem Description

In this problem, we're given a graph that is composed of 'n' nodes which are labeled from 0 to n - 1. The graph also has a set of edges given in a list where each edge is represented by a pair of nodes like [a, b] that signifies a bidirectional (undirected) connection between node a and node b. Our main objective is to determine if the given graph constitutes a valid tree.

To understand what makes a valid tree, we should recall two essential properties of trees:

    A tree must be connected, which means there should be some path between every pair of nodes.
    A tree cannot have any cycles, meaning no path should loop back on itself within the graph.

Therefore, our task is to check for these properties in the given graph. We need to verify if there's exactly one path between any two nodes (confirming a lack of cycles) and that all the nodes are reachable from one another (confirming connectivity). If both conditions are met, we return true; otherwise, we return false.
"""

from typing import List


class Solution:

    def validTree(self, num_nodes: int, edges: List[List[int]]) -> bool:
        # Helper function to find the root of a node 'x'.
        # Uses path compression to flatten the structure for faster future lookups.
        def find_root(node):
            print("parent", parent[node], node)
            if parent[node] != node:
                parent[node] = find_root(parent[node])  # Path compression
            return parent[node]

        # Initialize the parent list where each node is initially its own parent.

        parent = list(range(num_nodes))
        # Iterate over all the edges in the graph.
        for node_1, node_2 in edges:
            # Find the root of the two nodes.
            print("-----1")
            root_1 = find_root(node_1)
            print("------------2")
            root_2 = find_root(node_2)
            # print(root_1, root_2)
            # If the roots are the same, it means we encountered a cycle.
            if root_1 == root_2:
                return False
            # Union the sets - attach the root of one component to the other.
            parent[root_1] = root_2
            # Each time we connect two components, reduce the total number of components by one.
            num_nodes -= 1
            print(parent, num_nodes)
        # A tree should have exactly one more node than it has edges.
        # After union operations, we should have exactly one component left.
        return num_nodes == 1


s = Solution()
print(s.validTree(num_nodes=5, edges=[[2, 0], [1, 2], [2, 3], [3, 4]]))
