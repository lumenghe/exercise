"""
First Unique Character in a String
Easy
Topics
Companies

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.


"""


def first_unique_char(s: str) -> int:
    unique = []
    non_unique = []
    for char in s:
        if char in non_unique:
            continue
        if char not in unique:
            unique.append(char)
            continue
        unique.remove(char)
        non_unique.append(char)
    if len(unique) == 0:
        return -1

    first = unique[0]
    i = 0
    for char in s:
        if char == first:
            return i
        i += 1

    raise ValueError
