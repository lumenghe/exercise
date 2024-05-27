"""
Partition Equal Subset Sum
Solved
Medium
Topics
Companies

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

 

Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 100


"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp, s = set([0]), sum(nums)
        print(s)
        if s % 2 == 1:
            return False
        for num in nums:
            print(s >> 1)
            print([v + num for v in dp if v + num <= s >> 1])
            dp.update([v + num for v in dp if v + num <= s >> 1])
            print(dp)
        return s >> 1 in dp


class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        dp, s = set([0]), sum(nums)
        if s % 2 == 1:
            return False
        for num in nums:
            dp.update([v + num for v in dp if v + num <= s // 2])
        return s >> 1 in dp


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        for i in nums:
            tmp = dp.copy()
            for v in tmp:
                if v + i <= s // 2:
                    dp.add(v + i)

        return s // 2 in dp
