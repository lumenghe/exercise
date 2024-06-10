"""
Generate Parentheses
Medium
Topics
Companies

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8

"""

from typing import List


def generate_parenthese(n: int) -> list[str]:
    n -= 1
    result = {"()"}

    while n > 0:
        new_result = set()
        for item in result:
            for i in range(len(item)):
                new_result.add(item[:i] + "()" + item[i:])
        result = new_result
        n -= 1
    return result


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def dfs(first, last, s):
            if len(s) == 2 * n:
                ret.append(s)
            if first < n:
                dfs(first + 1, last, s + "(")
            if last < first:
                dfs(first, last + 1, s + ")")

        dfs(0, 0, "")
        return ret


sol = Solution()
print(sol.generateParenthesis(4))
