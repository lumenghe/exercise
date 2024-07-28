"""
David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

    Each container contains only balls of the same type.
    No two balls of the same type are located in different containers.

Example

David has containers and different types of balls, both of which are numbered from to

. The distribution of ball types per container are shown in the following diagram.

image

In a single operation, David can swap two balls located in different containers.

The diagram below depicts a single swap operation:

image

In this case, there is no way to have all green balls in one container and all red in the other using only swap operations. Return Impossible.

You must perform
queries where each query is in the form of a matrix,

. For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.

Function Description

Complete the organizingContainers function in the editor below.

organizingContainers has the following parameter(s):

    int containter[n][m]: a two dimensional array of integers that represent the number of balls of each color in each container

Returns

    string: either Possible or Impossible

Input Format

The first line contains an integer

, the number of queries.

Each of the next

sets of lines is as follows:

    The first line contains an integer 

, the number of containers (rows) and ball types (columns).
Each of the next
lines contains space-separated integers describing row

    .

Constraints

Scoring

    For 

of score,
.
For
of score,

    .

Output Format

For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.

"""


def organizingContainers(container):
    count = [0] * len(container[0])
    for i in container:
        temp = 0
        for j in i:
            count[temp] += j
            temp += 1
    temp = 0
    for i in count:
        flag = False
        for j in container:
            color = i - j[temp]
            left = sum(j) - j[temp]
            if color == left:
                flag = True
        if flag == False:
            return "Impossible"
    return "Possible"


print(organizingContainers([[1, 1], [1, 1]]))
