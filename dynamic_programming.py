def longest_common_subsequence(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[0] == Y[0]:
        return longest_common_subsequence(X[1:], Y[1:], m - 1, n - 1) + 1
    else:
        return max(
            longest_common_subsequence(X, Y[1:], m, n - 1),
            longest_common_subsequence(X[1:], Y, m - 1, n),
        )


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("LCS length is ", longest_common_subsequence(X, Y, len(X), len(Y)))
