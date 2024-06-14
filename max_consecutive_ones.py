"""
Max Consecutive Ones III
Solved
Medium
Topics
Companies
Hint

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length

"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            print(l, r)
        return r - l + 1


s = Solution()
nums = [
    1,  # 0
    1,  # 1
    1,  # 2
    1,  # 3
    0,  # 4
    0,  # 5
    0,
    1,
    1,
    1,
    0,  # 10
    0,
    0,
    1,
    1,  # 14
]
print(s.longestOnes(nums, 2))
