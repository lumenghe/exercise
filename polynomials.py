class PolyNomials:
    def __init__(self, coefficient: list) -> None:
        self.coefficient = coefficient
        self.length = len(coefficient)

    def isinstance(self, other) -> bool:
        if isinstance(other, self.__class__):
            return True

        raise TypeError
        return False

    def __str__(self):
        s = ""
        for index, c in enumerate(self.coefficient):
            if c:
                if index == 0:
                    s = str(c)
                elif c == 1:
                    s += " + " + f"X^{index}"
                elif c == -1:
                    s += " - " + f"X^{index}"
                elif c > 0:
                    s += " + " + str(c) + f" * X^{index}"
                else:
                    s += str(c) + f" * X^{index}"
        return s

    def __eq__(self, other):
        if self.isinstance(other):
            return self.coefficient == other.coefficient

        return False

    def __lt__(self, other):
        if self.isinstance(other):
            if self == other:
                return False

            len1 = self.length
            len2 = other.length
            if len1 == len2:
                for index in range(len1 - 1, -1, -1):
                    if self.coefficient[index] > other.coefficient[index]:
                        return False
                return True

            return len1 < len2

    def __gt__(self, other):
        if self.isinstance(other):
            return (self != other) and (not (self < other))

    def __add__(self, other):
        l1 = self.coefficient
        l2 = other.coefficient
        n1, n2 = self.length, other.length
        if n1 < n2:
            l1 += [0 for _ in range(n2 - n1)]
        else:
            l2 += [0 for _ in range(n1 - n2)]

        added_list = [x + y for x, y in zip(l1, l2)]
        return PolyNomials(added_list)

    def opposition(self):
        return PolyNomials(list(map(lambda x: -x, self.coefficient)))

    def __sub___(self, other):
        return self.__add__(other.opposition())


if __name__ == "__main__":
    polynomials_1 = PolyNomials([1, 2, -1, 0, 12])
    polynomials_2 = PolyNomials([2, 4])
    print(polynomials_1)
    print(polynomials_2)
    print("eq=", polynomials_1 == polynomials_2)
    print("lt=", polynomials_1 < polynomials_2)
    print("gt=", polynomials_1 > polynomials_2)
    print("add=", polynomials_1 + polynomials_2)
    print("max=", max(polynomials_1, polynomials_2))
    print("min=", min(polynomials_1, polynomials_2))
