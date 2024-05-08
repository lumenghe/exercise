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
