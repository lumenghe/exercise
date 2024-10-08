"""

Min Cost Climbing Stairs
Easy
Topics
Companies
Hint

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

 

Constraints:

    2 <= cost.length <= 1000
    0 <= cost[i] <= 999


"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        dp = [0] * len(cost)
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])


class SolutionBetter:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) in [0, 1]:
            return 0
        a = cost[0]
        b = cost[1]
        for i in range(2, len(cost)):
            temp = b
            b = min(a, b) + cost[i]
            a = temp
        return min(a, b)


class Solution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost) + 2)]
        dp[1] = cost[0]
        for i in range(2, len(cost) + 2):
            if i == (len(cost) + 1):
                dp[i] = min(dp[i - 2], dp[i - 1])
            else:
                dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i - 1]

        return min(dp[len(cost)], dp[len(cost) + 1])


class SolutionBetterThanSolution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost) + 1)]
        dp[1] = cost[0]
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i - 1]

        return min(dp[len(cost)], dp[len(cost) - 1])
