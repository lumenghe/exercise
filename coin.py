import math

from scipy.special import comb

if __name__ == "__main__":
    print(math.factorial(6))
    print(comb(3, 3, exact=True))

    sum = 0
    for n in range(41):
        sum += comb(100, n, exact=True)

    print(sum)
    print(sum / (2**100))
