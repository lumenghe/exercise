import numpy as np
import hashlib
from typing import Optional


def length_hash(s: str) -> int:
    return len(s)


def hashli_hash(s: str) -> int:
    return int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16)


class MyDict:
    def __init__(self, size: int, hash_fun: "func") -> None:
        self.size = size
        self.hash_fun = hash_fun
        self.data = [[] for i in range(size)]

    def get(self, key: str, value: Optional[int]) -> int:
        slot = self.data[self.hash_fun(key) % self.size]
        for k, v in slot:
            if k == key:
                return v

        return value

    def modify(self, key: str, value: int) -> None:
        slot = self.data[self.hash_fun(key) % self.size]
        for index, (k, v) in enumerate(slot):
            if k == key:
                slot[index] = (key, value)
                return

        slot.append((key, value))

    def get_longest(self) -> int:
        return max(list(map(lambda x: len(x), self.data)))

    def get_average(self) -> int:
        return np.mean(list(map(lambda x: len(x), self.data)))

    def get_percentage_used(self) -> float:
        return sum(len(x) != 0 for x in self.data) / len(self.data)


def pass_hash_func(hash_func: "hash_func") -> None:
    my_dict = MyDict(101, hash_func)

    with open("notre_dame.txt", "r") as f:
        for line in f:
            for word in line.strip().split():
                my_dict.modify(word, my_dict.get(word, 0) + 1)

    print("longest: ", my_dict.get_longest())
    print("average: ", my_dict.get_average())
    print("percentage used:", my_dict.get_percentage_used())


if __name__ == "__main__":
    pass_hash_func(length_hash)
    pass_hash_func(hashli_hash)
