"""

Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

Illustration : 

A[] = {10, 20, 35, 50, 75, 80}
X = =70
i = 0
j = 5
A[i] + A[j] = 10 + 80 = 90
Since A[i] + A[j] > X, j--
i = 0
j = 4
A[i] + A[j] = 10 + 75 = 85
Since A[i] + A[j] > X, j--
i = 0
j = 3
A[i] + A[j] = 10 + 50 = 60
Since A[i] + A[j] < X, i++
i = 1
j = 3
m
A[i] + A[j] = 20 + 50 = 70
Thus this signifies that Pair is Found.


"""

# Python Program Illustrating Naive Approach to
# Find if There is a Pair in A[0..N-1] with Given Sum

# Method


def isPairSum(A, N, X):

    for i in range(N):
        for j in range(N):

            # as equal i and j means same element
            if i == j:
                continue

            # pair exists
            if A[i] + A[j] == X:
                return True

            # as the array is sorted
            if A[i] + A[j] > X:
                break

    # No pair found with given sum
    return 0


# Driver code
arr = [2, 3, 5, 8, 9, 10, 11]
val = 17

print(isPairSum(arr, len(arr), val))

# This code is contributed by maheshwaripiyush9
