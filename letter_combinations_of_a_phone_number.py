"""
Letter Combinations of a Phone Number
Medium
Topics
Companies

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

 

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def sub_string(digits):

            length = len(digits)
            if length == 0:
                return []
            if length == 1:
                return [x for x in self.phone_map[digits]]

            sub_result = sub_string(digits[:-1])
            lastvalues = self.phone_map[digits[-1]]
            result = []

            for value in sub_result:
                for index in range(len(lastvalues)):
                    result.append(value + lastvalues[index])
            return result

        return sub_string(digits)
