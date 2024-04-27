"""
Reverse Integer
Medium
Topics
Companies

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1

"""


def wrong_reverse(x: int) -> int:
    flag = x >= 0
    mylist = []
    abs_x = abs(x)
    while abs_x // 10 > 0:
        mylist.append(abs_x % 10)
        abs_x //= 10

    mylist.append(abs_x % 10)
    ret = 0
    for index, v in enumerate(mylist[::-1]):
        ret += 10**index * v

    ret = ret * (-1) if flag is False else ret

    return 0 if x >= (2**31) or x < -(2**31) else ret


def right_reverse(x: int) -> int:
    ans = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
    return ans if -(2**31) <= ans < 2**31 else 0


if __name__ == "__main__":
    print(wrong_reverse(1534236469))
    print(right_reverse(1534236469))
