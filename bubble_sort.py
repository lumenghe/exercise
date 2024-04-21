import random


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        done = True
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                done = False
        if done == True:
            break


arr = list(range(1, 23, 1))
random.shuffle(arr)
print(arr)
bubble_sort(arr)
print(arr)
