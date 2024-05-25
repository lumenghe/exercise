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
        numCoins = len(coins)

        # Values in this array equal the number of coins needed to achieve the cost of the index
        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0
        print(minCoins)
        # Loop through every needed amount
        for i in range(amount + 1):
            # Loop through every coin value
            for coin in coins:
                # Check that the coin is not bigger than the current amount
                if coin <= i:
                    # minCoins[i]: number of coins needed to make amount i
                    # minCoins[i-coin]: number of coins needed to make the amount before adding
                    #                   the current coin to it (+1 to add the current coin)
                    minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

        # Check if any combination of coins was found to create the amount
        if minCoins[amount] == amount + 1:
            return -1

        # Return the optimal number of coins to create the amount
        return minCoins[amount]


coins = [1, 2, 5]
s = Solution()
s.coinChange(coins, 11)
