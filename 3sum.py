"""
3Sum
Medium
Topics
Companies
Hint

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive, negative, zero = [], [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zero.append(num)

        self.ret = []
        if len(zero) >= 3:
            self.ret.append((0, 0, 0))
        if 0 < len(zero) < 3:
            for num in positive:
                if -num in negative:
                    if (-num, 0, num) not in self.ret:
                        self.ret.append((-num, 0, num))

        def search(list1, list2):
            for i in range(len(list1)):
                for j in range(i + 1, len(list1)):
                    if -(list1[i] + list1[j]) in list2:
                        temp = list(sorted((list1[i], list1[j], -(list1[i] + list1[j]))))
                        if temp not in self.ret:
                            self.ret.append(temp)

        search(positive, negative)
        search(negative, positive)
        return self.ret


s = Solution()
nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
ret = s.threeSum(nums)
print(len(ret))
