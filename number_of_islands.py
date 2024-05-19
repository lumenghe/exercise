"""
Number of Islands
Medium
Topics
Companies

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.count = 0

        def dfs(i, j):
            if 0 <= i < self.m and 0 <= j < self.n and self.grid[i][j] == "1":

                self.grid[i][j] = "0"
                dfs(i, j - 1)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i + 1, j)

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1":
                    self.count += 1
                    dfs(i, j)

        return self.count
