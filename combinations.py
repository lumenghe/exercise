"""
Combinations
Medium
Topics
Companies

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

 

Constraints:

    1 <= n <= 20
    1 <= k <= n

"""

from typing import List


class SolutionSlow:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(path, res):
            if len(path) == k:
                if set(path) not in res:
                    res.append(set(path))
                return

            for i in range(0, n):
                if not used[i]:
                    used[i] = True
                    dfs(path + [i + 1], res)
                    used[i] = False

        used = [False] * n
        res = []
        dfs([], res)
        return res


class SolutionSlow:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(path):
            if len(path) == k and set(path) not in res:
                res.append(set(path))

            for i in range(1, n + 1):
                if i not in path:
                    path.append(i)
                    dfs(path)
                    path.remove(i)

        dfs([])
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []

        def backtrack(remain, comb, nextt):
            if remain == 0:
                sol.append(comb[:])
                return

            for i in range(nextt, n + 1):
                comb.append(i)
                backtrack(remain - 1, comb, i + 1)
                comb.pop()

        backtrack(k, [], 1)
        return sol


from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        used = []
        res = []
        candidates = sorted(candidates)

        def dfs(idx, path, cur):
            if cur > target:
                return
            if cur == target:
                if Counter(path) not in used:
                    used.append(Counter(path))
                    res.append(path)
                return
            for i in range(idx, len(candidates)):

                if i == idx or candidates[i] != candidates[i - 1]:
                    dfs(i + 1, path + [candidates[i]], cur + candidates[i])

        dfs(0, [], 0)
        return res
