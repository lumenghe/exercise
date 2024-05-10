import random


def merge_sort(mylist: list) -> list:
    """merge sort"""
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mylist[k] = left[i]
                i += 1
            else:
                mylist[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            mylist[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1

    return mylist


if __name__ == "__main__":
    mylist = list(range(20))
    print(mylist)

    random.shuffle(mylist)
    print(mylist)
    print(merge_sort(mylist))
