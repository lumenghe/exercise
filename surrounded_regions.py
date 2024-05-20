"""
Surrounded Regions
Medium
Topics
Companies

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

 

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.


"""

from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        self.safe = []
        for i in range(m):
            if board[i][0] == "O":
                self.safe.append((i, 0))
            if board[i][n - 1] == "O":
                self.safe.append((i, n - 1))
        for j in range(n):
            if board[0][j] == "O":
                self.safe.append((0, j))
            if board[m - 1][j] == "O":
                self.safe.append((m - 1, j))

        def dfs(i, j, board):
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "#"

            return board

        while self.safe:
            i, j = self.safe.pop(0)
            board[i][j] = "#"
            for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == "O":
                    board[ii][jj] = "#"
                    self.safe.append((ii, jj))
            # board = dfs(i, j+1, board)
            # board = dfs(i, j-1, board)
            # board = dfs(i+1, j, board)
            # board = dfs(i-1, j, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

        return board


s = Solution()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
# print(s.solve(board))
board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
# print(s.solve(board))
board = [
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
]
print(s.solve(board))
