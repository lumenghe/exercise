"""
Max Area of Island
Medium
Topics
Companies

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.

"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_areas = 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.total = {}
        self.grid = grid

        def dfs(i, j, root_i, root_j):
            if 0 <= i < self.m and 0 <= j < self.n and self.grid[i][j] == 1:
                self.grid[i][j] = 0
                self.total.setdefault((root_i, root_j), 0)
                self.total[(root_i, root_j)] += 1
                dfs(i - 1, j, root_i, root_j)
                dfs(i + 1, j, root_i, root_j)
                dfs(i, j - 1, root_i, root_j)
                dfs(i, j + 1, root_i, root_j)

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    dfs(i, j, i, j)

        if self.total == {}:
            return 0
        return max(self.total.values())
