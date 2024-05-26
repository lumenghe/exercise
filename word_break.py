"""
Word Break
Solved
Medium
Topics
Companies

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

 

Constraints:

    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.

"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def construct(current, word_dict, memo={}):
            if current == "":
                return True

            if current in memo:
                return memo[current]

            for word in word_dict:
                if current.startswith(word):
                    new_current = current[len(word) :]
                    if construct(new_current, word_dict, memo):
                        memo[current] = True

                        return True
            print(memo)
            memo[current] = False
            return False

        return construct(s, wordDict)


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]


class SolutionMySolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[i - len(word) : i] == word:
                    if i - len(word) <= 0:
                        dp[i] = True
                    else:
                        dp[i] = dp[i - len(word)]
                if dp[i]:
                    break
        return dp[len(s)]
