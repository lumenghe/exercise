"""
Sliding Window Median
Hard
Topics
Companies
Hint

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

    For examples, if arr = [2,3,4], the median is 3.
    For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.

You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

 

Constraints:

    1 <= k <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1

"""

from typing import List


class SolutionSlow:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        min_list = []
        max_list = []
        length = len(nums)
        ret = []
        prev = nums[:k]
        for i in range(length - k + 1):
            sub = nums[i : i + k]
            subb = sorted(sub)
            ret.append((subb[k // 2] + subb[-1 - k // 2]) / 2)

        return ret


from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        window = SortedList(nums[:k])

        for i in range(k, len(nums)):
            if k % 2 == 1:
                median = window[k // 2]
            else:
                median = (window[k // 2] + window[k // 2 - 1]) / 2

            res.append(float(median))

            window.discard(nums[i - k])
            window.add(nums[i])

        # Process the last window
        if k % 2 == 1:
            median = window[k // 2]
        else:
            median = (window[k // 2] + window[k // 2 - 1]) / 2

        res.append(float(median))

        return res


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor
