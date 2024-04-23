"""
Valid Palindrome
Easy
Topics
Companies

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

"""


def is_palindrome_first(s: str) -> bool:

    s = [
        c.lower()
        for c in s
        if (c >= "A" and c <= "Z") or (c >= "a" and c <= "z") or (c >= "0" and c <= "9")
    ]
    return s == s[::-1]


def is_palindrome_second(s: str) -> bool:
    s = [
        c.lower()
        for c in s
        if (c >= "A" and c <= "Z") or (c >= "a" and c <= "z") or (c >= "0" and c <= "9")
    ]

    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False

    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal:123 Panama"
    print(is_palindrome_first(s))
    print(s)
    print(is_palindrome_second(s))

    s = "A man, a plan, a canal:123 Panrama"
    print(is_palindrome_first(s))
    print(s)
    print(is_palindrome_second(s))

    s = "0P"
    print(is_palindrome_first(s))
    print(s)
    print(is_palindrome_second(s))
