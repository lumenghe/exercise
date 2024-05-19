"""
Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""

from itertools import product


def solutionWrong(grid):
    """"""
    print(grid)
    m = len(grid)
    n = len(grid[0])

    def dfs(i, j, count, visited):
        if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
            visited.append((i, j))
            if grid[i][j] == 0:
                return count
            elif grid[i][j] > 0:
                a = dfs(i - 1, j, count + 1, visited)
                b = dfs(i, j - 1, count + 1, visited)
                c = dfs(i + 1, j, count + 1, visited)
                d = dfs(i, j + 1, count + 1, visited)
                return min(a, b, c, d)
        return -1

    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:
                grid[i][j] = dfs(i, j, 0, [])
    return grid


INF = 2**31 - 1
grid = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF],
]


def solution(grid):
    print(grid)
    m = len(grid)
    n = len(grid[0])

    doors = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0]
    print(doors)

    def dfs(i, j, count, visited):
        """"""
        nonlocal doors
        if 0 <= i < m and 0 <= j < n and grid[i][j] not in (0, -1) and (i, j) not in visited:
            grid[i][j] = min(count, grid[i][j])
            visited.append((i, j))
            dfs(i - 1, j, count + 1, visited)
            dfs(i + 1, j, count + 1, visited)
            dfs(i, j + 1, count + 1, visited)
            dfs(i, j - 1, count + 1, visited)

    for i, j in doors:
        dfs(i - 1, j, 1, [])
        dfs(i, j - 1, 1, [])
        dfs(i + 1, j, 1, [])
        dfs(i, j + 1, 1, [])
    print(grid)


print(solution(grid))

from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        """
        This method modifies the 'rooms' matrix in-place by filling each empty room with the distance to its nearest gate.
        An empty room is represented by the integer 2**31 - 1, a gate is represented by 0, and a wall is represented by -1.
        :type rooms: List[List[int]]
        """
        # Dimensions of the rooms matrix
        num_rows, num_cols = len(rooms), len(rooms[0])
        # Define the representation of an infinite distance (empty room)
        INF = 2**31 - 1
        # Initialize a queue and populate it with the coordinates of all gates
        queue = deque([(row, col) for row in range(num_rows) for col in range(num_cols) if rooms[row][col] == 0])

        # Initialize distance from gates
        distance = 0
        # Perform a breadth-first search (BFS) from the gates
        while queue:
            print(queue)
            # Increase the distance with each level of BFS
            distance += 1
            # Process nodes in the current level
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # Explore the four possible directions from the current cell
                for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = i + delta_row, j + delta_col
                    # Check if the new position is within bounds and is an empty room
                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols and rooms[new_row][new_col] == INF:
                        # Update the distance for the room
                        rooms[new_row][new_col] = distance
                        # Add the new position to the queue to process its neighbors
                        queue.append((new_row, new_col))

        print(rooms)


INF = 2**31 - 1
grid = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF],
]
s = Solution()
s.wallsAndGates(grid)
