"""


In this problem, we are given a nestedList consisting of integers that might be wrapped in multiple layers of lists. An integer's depth is determined by how many lists contain it. For instance, in the list [1,[2,2],[[3],2],1], the number 1 is at depth 1 (since it's not within any nested list), the number 2 is at depth 2 (as it is in one nested list), and the number 3 is at depth 3 (as it's in two nested lists).

Our goal is to compute the sum of all integers in nestedList each weighted by its depth. In simple terms, we multiply each integer by the number of lists it is inside and then sum these products together.
"""


def depth_sum(nested_list: list) -> int:

    def element_sum(sub_list, level):
        sub_sum = 0
        for element in sub_list:
            if isinstance(element, list):
                sub_sum += element_sum(element, level + 1)
            else:
                sub_sum += element * level
        return sub_sum

    return element_sum(nested_list, 1)


nested_list = [1, [2, 2], [[3], 2], 1]
print(depth_sum(nested_list=nested_list))
