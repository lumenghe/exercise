"""
House Robber II
Solved
Medium
Topics
Companies
Hint

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 1000

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def house(nums):
            new_length = len(nums)

            a = nums[0]
            b = max(nums[:2])
            c = max(a + nums[2], nums[1])
            for i in range(3, new_length):
                tmp = c
                c = max(max(a, b) + nums[i], c)
                a = b
                b = tmp

            return max(b, c)

        length = len(nums)
        if length == 0:
            return 0
        if length in [1, 2, 3]:
            return max(nums)
        return max(house(nums[:-1]), house(nums[1:]))


class Solution2:
    def rob(self, nums: List[int]) -> int:
        def house(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[:2])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        length = len(nums)
        if length == 0:
            return 0
        if length in [1, 2]:
            return max(nums)
        return max(house(nums[:-1]), house(nums[1:]))


s = Solution()
# s.rob([200,3,140,20,10])
s.rob([2, 7, 9, 3, 1])
