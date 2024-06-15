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
                    if (0, num, -num) not in self.ret:
                        self.ret.append((0, num, -num))

        def search(list1, list2):
            for i in range(len(list1)):
                for j in range(i + 1, len(list1)):
                    if -(list1[i] + list1[j]) in list2:
                        if (list1[i], list1[j], -(list1[i] + list1[j])) not in self.ret:
                            self.ret.append((list1[i], list1[j], -(list1[i] + list1[j])))

        search(positive, negative)
        search(negative, positive)
        return self.ret


s = Solution()
nums = [
    34,
    55,
    79,
    28,
    46,
    33,
    2,
    48,
    31,
    -3,
    84,
    71,
    52,
    -3,
    93,
    15,
    21,
    -43,
    57,
    -6,
    86,
    56,
    94,
    74,
    83,
    -14,
    28,
    -66,
    46,
    -49,
    62,
    -11,
    43,
    65,
    77,
    12,
    47,
    61,
    26,
    1,
    13,
    29,
    55,
    -82,
    76,
    26,
    15,
    -29,
    36,
    -29,
    10,
    -70,
    69,
    17,
    49,
]
ret = s.threeSum(nums)
print(len(ret))

trueret = [
    [-82, -11, 93],
    [-82, 13, 69],
    [-82, 17, 65],
    [-82, 21, 61],
    [-82, 26, 56],
    [-82, 33, 49],
    [-82, 34, 48],
    [-82, 36, 46],
    [-70, -14, 84],
    [-70, -6, 76],
    [-70, 1, 69],
    [-70, 13, 57],
    [-70, 15, 55],
    [-70, 21, 49],
    [-70, 34, 36],
    [-66, -11, 77],
    [-66, -3, 69],
    [-66, 1, 65],
    [-66, 10, 56],
    [-66, 17, 49],
    [-49, -6, 55],
    [-49, -3, 52],
    [-49, 1, 48],
    [-49, 2, 47],
    [-49, 13, 36],
    [-49, 15, 34],
    [-49, 21, 28],
    [-43, -14, 57],
    [-43, -6, 49],
    [-43, -3, 46],
    [-43, 10, 33],
    [-43, 12, 31],
    [-43, 15, 28],
    [-43, 17, 26],
    [-29, -14, 43],
    [-29, 1, 28],
    [-29, 12, 17],
    [-14, -3, 17],
    [-14, 1, 13],
    [-14, 2, 12],
    [-11, -6, 17],
    [-11, 1, 10],
    [-3, 1, 2],
]
print(len(trueret))
