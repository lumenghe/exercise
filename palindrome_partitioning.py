"""
Palindrome Partitioning
Solved
Medium
Topics
Companies

Given a string s, partition s such that every
substring
of the partition is a
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

 

Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.

"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path)
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])

        return result


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path)
                return

            for end in range(start, len(s)):
                if is_palindrome(s[start : end + 1]):
                    backtrack(end + 1, path + [s[start : end + 1]])

        result = []
        backtrack(0, [])
        return result
