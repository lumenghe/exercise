import random


def quick_sort(alist: list, first: int, last: int) -> None:
    """quick sort"""
    if first < last:
        split = partition(alist, first, last)
        quick_sort(alist, first, split - 1)
        quick_sort(alist, split + 1, last)


def partition(alist: list, first: int, last: int) -> int:
    done = False
    left = first + 1
    while not done:
        while left <= last and alist[left] <= alist[first]:
            left += 1

        while left <= last and alist[first] <= alist[last]:
            last -= 1

        if left > last:
            done = True
            alist[first], alist[last] = alist[last], alist[first]
        else:
            alist[left], alist[last] = alist[last], alist[left]

    return last


if __name__ == "__main__":
    my_list = list(range(10))
    random.shuffle(my_list)
    print(my_list)
    quick_sort(my_list, 0, len(my_list) - 1)
    print(my_list)
