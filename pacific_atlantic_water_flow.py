"""
Pacific Atlantic Water Flow
Solved
Medium
Topics
Companies

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

 

Constraints:

    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 105

"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < m
                    and 0 <= new_y < n
                    and (new_x, new_y) not in visited
                    and heights[new_x][new_y] >= heights[x][y]
                ):
                    dfs(visited, new_x, new_y)

        # iterate from left border and right border
        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n - 1)
        # iterate from up border and bottom border
        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m - 1, j)
        # The intersections of two sets are coordinates where water can flow to both P and A
        return list(p_visited.intersection(a_visited))


class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()

        def dfs(i, j, visited):

            visited.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and heights[x][y] >= heights[i][j]:
                    dfs(x, y, visited)

        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n - 1, a_visited)

        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m - 1, j, a_visited)

        print(p_visited)
        print(a_visited)

        return list(p_visited & a_visited)


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        alt = []
        pac = []
        ret = []

        def dfs(r, c, prevheight, visited):
            if r in [-1, m] or c in [-1, n] or (r, c) in visited or heights[r][c] < prevheight:
                return
            visited.append((r, c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)

        for i in range(m):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, n - 1, heights[i][n - 1], alt)

        for j in range(n):
            dfs(0, j, heights[0][j], pac)
            dfs(m - 1, j, heights[m - 1][j], alt)

        for i in range(m):
            for j in range(n):
                if (i, j) in alt and (i, j) in pac:
                    ret.append((i, j))

        return ret
