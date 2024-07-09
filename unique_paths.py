"""
Unique Paths
Solved
Medium
Topics
Companies

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

 

Constraints:

    1 <= m, n <= 100

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_step = (m - 1) + (n - 1)
        count = 1
        for i in range(total_step, m - 1, -1):
            count *= i

        product = 1
        for i in range(1, n):
            product *= i
        count /= product

        return int(count)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = (m - 1) + (n - 1)
        b = m - 1

        def productpart(start, count):
            ret = 1
            current = start
            while current > (start - count):
                ret *= current
                current -= 1
            return ret

        def productpart2(number):
            current = number
            ret = 1
            while current > 0:
                ret *= current
                current -= 1

            return ret

        return int(productpart(a, (m - 1)) / productpart2(b))
