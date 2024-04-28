"""
Climbing Stairs
Easy
Topics
Companies
Hint

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


def climb_staires(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return climb_staires(n - 1) + climb_staires(n - 2)


def climb_staires_fast(n: int) -> int:
    if n == 1 or n == 0:
        return 1

    prev, current = 1, 1
    for i in range(1, n):
        temp = curent
        current = prev + current
        prev = temp

    return current


if __name__ == "__main__":
    print(climb_staires(3))
    print(climb_staires_fast(10))
