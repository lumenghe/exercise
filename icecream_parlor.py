"""
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example.
The two flavors that cost and meet the criteria. Using -based indexing, they are at indices and

.

Function Description

Complete the icecreamParlor function in the editor below.

icecreamParlor has the following parameter(s):

    int m: the amount of money they have to spend
    int cost[n]: the cost of each flavor of ice cream

Returns

    int[2]: the indices of the prices of the two flavors they buy, sorted ascending

Input Format

The first line contains an integer,
, the number of trips to the ice cream parlor. The next

sets of lines each describe a visit.

Each trip is described as follows:

    The integer 

, the amount of money they have pooled.
The integer
, the number of flavors offered at the time.
space-separated integers denoting the cost of each flavor:

    .

Note: The index within the cost array represents the flavor of the ice cream purchased.

Constraints

, ∀

    There will always be a unique solution.

Sample Input

STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]

Sample Output

1 4
1 2

Explanation

Sunny and Johnny make the following two trips to the parlor:

    The first time, they pool together 

dollars. Of the five flavors available that day, flavors and have a total cost of
.
The second time, they pool together
dollars. Of the four flavors available that day, flavors and have a total cost of .
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#


def icecreamParlor(m, arr):
    # Write your code here
    other = list(map(lambda x: m - x, arr))
    for index, value in enumerate(arr):
        for index_j, value2 in enumerate(other):
            if index != index_j and value == value2:
                return index + 1, index_j + 1
    raise ValueError("not found")


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")

    fptr.close()
