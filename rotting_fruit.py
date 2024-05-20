"""
You are given a 2-D matrix grid. Each cell can have one of three possible values:

    0 representing an empty cell
    1 representing a fresh fruit
    2 representing a rotten fruit

Every second, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of seconds that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:

Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4

Example 2:

Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1

Constraints:

    1 <= grid.length, grid[i].length <= 10

"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        fresh_cnt = 0
        rotten = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        minutes_passed = 0
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                        fresh_cnt -= 1
                        grid[xx][yy] = 2
                        rotten.append((xx, yy))

        return minutes_passed if fresh_cnt == 0 else -1
