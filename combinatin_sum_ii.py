"""
Combination Sum II
Medium
Topics
Companies

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

 

Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

"""

from collections import Counter


class SolutionSlow:
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
                dfs(i + 1, path + [candidates[i]], cur + candidates[i])

        dfs(0, [], 0)
        return res
