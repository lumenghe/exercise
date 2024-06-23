"""
Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint

Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""
class SolutionWrong:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def largestlength(s, word):
            max_length = 0
            tmp = 0
            for l in s:
                if l!=word:
                    tmp += 1
                else:
                    max_length = max(max_length, tmp+1)
                    tmp = 0
            return max_length
        ret = 0
        for letter in set(s):
            print(letter, largestlength(s, letter))
            ret = max(largestlength(s, letter), ret)

        return ret


        
