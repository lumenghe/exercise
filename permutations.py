"""
Permutations
Solved
Medium
Topics
Companies

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = 0

        def sub_permute(sub_nums):
            result = []
            for num in sub_nums:
                tmp = sub_nums.copy()
                tmp.remove(num)

                hi = sub_permute(tmp)
                if hi == []:
                    return [[num]]
                for subsub in hi:
                    result.append([num] + subsub)
                    result.append(subsub + [num])
            return result

        good = sub_permute(nums)
        ret = []
        for i in good:
            if i not in ret:
                ret.append(i)
        return ret


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                print("append", nums[:])
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                print("start=", start, "i=", i, nums)
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used, res):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i, letter in enumerate(nums):
                if i not in used:
                    path.append(letter)
                    used.append(i)
                    dfs(path, used, res)
                    path.pop()
                    used.remove(i)

        res = []
        dfs([], [], res)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used, res):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i, letter in enumerate(nums):
                if not used[i]:
                    path.append(letter)
                    used[i] = True
                    dfs(path, used, res)
                    path.pop()
                    used[i] = False

        res = []
        dfs([], [False] * len(nums), res)
        return res
