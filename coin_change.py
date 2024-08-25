"""
 Coin Change
Medium
Topics
Companies

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

 

Constraints:

    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104


"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [amount + 1] * amount
        for index in range(1, amount + 1):
            for coin in coins:
                if index >= coin:
                    dp[index] = min(dp[index], dp[index - coin] + 1)

        dp = [-1 if dp[index] == (amount + 1) else dp[index] for index in range(amount + 1)]

        return dp[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for index in range(1, amount + 1):
                if index >= coin:
                    dp[index] = min(dp[index], dp[index - coin] + 1)

        dp = [-1 if dp[index] == (amount + 1) else dp[index] for index in range(amount + 1)]

        return dp[amount]


coins = [1, 2, 5]
s = Solution()
s.coinChange(coins, 11)
