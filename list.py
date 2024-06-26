class SingleList(object):
    def __init__(self, value: int):
        self.value = value
        self.next = None


class DoubleList(object):
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


# fmt: off
list_example = [5,1,2,3,4,9,7,7,4,5,6,6,3,1,0,1,4,5,6,7,8,1,6,9,7,1,2,3]
# fmt: on


def list2single(l):
    """
    Create a single-linked list from a list
    """
    next = None
    for value in l[::-1]:
        current = SingleList(value)
        current.next = next
        next = current

    return current


def list2double(l):
    """
    Create a double-linked list from a list
    """
    next = None
    for value in l[::-1]:
        current = DoubleList(value)
        current.next = next
        if next is not None:
            next.prev = current
        next = current

    return current


def print_single(head):
    """
    Print a single-linked list
    """
    s = str(head.value)
    next = head.next
    while next is not None:
        s += "->" + str(next.value)
        next = next.next

    print(s)


single_example = list2single(list_example)
print_single(single_example)


def print_double(head):
    """
    Print a double-linked list
    """
    s = f"{head.value}"
    prev = head
    current = head.next
    while current.prev and current.next:
        if prev is current.prev:
            s += "<-"
        else:
            s += "--"

        if prev.next is current:
            s += "->"
        else:
            s += "--"

        s += f"{current.value}"

        prev = current
        current = current.next

    if current.prev is prev:
        s += "<-"
    else:
        s += "--"
    if prev.next is current:
        s += "->"
    else:
        s += "--"

    s += f"{current.value}"
    print(s)


double_example = list2double(list_example)
print_double(double_example)


def length_single(head):
    """
    Compute length of a single-linked list
    """
    count = 1
    current = head
    while current.next:
        count += 1
        current = current.next

    return count


# print(len(list_example))
# print(length_single(single_example))


def length_double(head):
    """
    Compute length of a double-linked list
    """
    count = 1
    current = head
    while current.next:
        count += 1
        current = current.next

    return count


# print(length_double(double_example))


def max_single(head):
    """
    Get maximum of a single-linked list
    """
    current = head
    max_value = current.value
    while current.next:
        max_value = max(current.next.value, max_value)
        current = current.next

    return max_value


# print(max_single(single_example))


def max_double(head):
    """
    Get maximum of a double-linked list
    """
    current = head
    max = head.value
    while current:
        if max < current.value:
            max = current.value
        current = current.next

    return max


# print("max double=", max_double(double_example) == max(list_example))


def revert_single(head):
    """
    Revert a single-linked list (return the former last element as head of the new list)
    """
    current = head
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


# print_single(single_example)
# print_single(revert_single(single_example))


def revert_double(head):
    """
    Revert a double-linked list (return the former last element as head of the new list)
    """

    prev = head
    current = head.next

    while prev.next:
        prev.next = prev.prev
        prev.prev = current
        next = current.next
        prev = current
        current = current.next

    prev.next = prev.prev
    prev.prev = None
    return prev


# print_double(double_example)
# print_double(revert_double(double_example))


def get_element_single(head, i):
    """
    Get i-th element in a single-linked list
    """
    index = 0
    current = head
    while index < i:
        current = current.next
        if current is None:
            raise IndexError
        index += 1

    return current


# print(get_element_single(single_example, 5).value)


def get_element_double(head, i):
    """
    Get i-th element in a single-linked list
    """
    index = 0
    current = head
    while index < i:
        current = current.next
        index += 1
        if current is None:
            raise IndexError

    return current


# print(get_element_double(double_example, 5).value)


def delete_element_single(head, i):
    """
    Delete i-th element in a single-linked list
    """
    if i == 0:
        return head.next

    index = 0
    current = head
    while index < i - 1:
        current = current.next
        if current is None:
            raise IndexError
        index += 1

    current.next = current.next.next

    return head


# print_single(delete_element_single(single_example, 1))


def delete_element_double(head, i):

    if i == 0:
        head.next.prev = None
        return head.next

    index = 0
    current = head
    while index < i - 1:
        current = current.next
        if current is None:
            raise IndexError
        index += 1

    current.next = current.next.next
    current.next.prev = current

    return head


# print_double(delete_element_double(double_example, 10))


def insert_element_single(head, i, e):
    """
    Insert element at position i in a single-linked list
    """
    if i == 0:
        e.next = head
        return e

    index = 0
    current = head
    while index < i - 1:
        current = current.next
        if current is None:
            raise IndexError
        index += 1

    e.next = current.next
    current.next = e

    return head


# new_element = SingleList(100)
# print_single(insert_element_single(single_example, 3, new_element))


def insert_element_double(head, i, e):
    """
    Insert element at position i in a double-linked list
    """
    if i == 0:
        e.next = head
        e.prev = None
        head.prev = e
        return e

    index = 0
    current = head
    while index < i - 1:
        current = current.next
        if current is None:
            raise IndexError
        index += 1

    e.next = current.next
    e.prev = current
    current.next = e
    if e.next is not None:
        e.next.prev = e
    return head


# new_element = DoubleList(100)
# print(len(list_example))
# print_double(double_example)
# print_double(insert_element_double(double_example, 28, new_element))


def concatenate_single(head1, head2):
    """
    Concatenate two single-linked lists, head of the new list is head of the first list
    """
    current = head1
    while current.next:
        current = current.next

    current.next = head2

    return head1


def concatenate_double(head1, head2):
    """
    Concatenate two double-linked lists, head of the new list is head of the first list
    """
    current = head1
    while current.next:
        current = current.next

    current.next = head2
    head2.prev = current
    return head1


def split_single(head):
    """
    Splits a single-linked list into two lists by separating even and odd positions, returning heads for both new lists
    """
    prev = head
    head2 = current = head.next
    while current:
        prev.next = current.next
        prev = current
        current = current.next
    prev.next = None

    return head, head2


# (head_1, head_2) = split_single(single_example)
# print_single(head_1)
# print_single(head_2)


def split_double(head):
    """
    Splits a double-linked list into two lists by separating even and odd positions, returning heads for both new lists
    """

    head2 = head.next
    prev = head
    current = head.next

    while current.next:
        prev.next = current.next
        prev = current
        current = current.next

    prev.next = None

    while prev.prev:
        current.prev = prev.prev
        current = prev
        prev = prev.prev

    current.prev = None

    return head, head2


# double_example = list2double(list_example)
# (head_1, head_2) = split_double(double_example)
# print_double(head_1)
# print_double(head_2)


def remove_duplicates_single(head):
    """
    Remove duplicates from a single-linked list, only O(1) extra memory
    """
    label = head
    while label:
        current = label
        while current:
            if current.next and current.next.value == label.value:
                current.next = current.next.next
            current = current.next
        label = label.next
    return head


# single_example = list2single(list_example)
# print_single(remove_duplicates_single(single_example))


def remove_duplicates_double(head):
    """
    Remove duplicates from a double-linked list, only O(1) extra memory
    """
    label = head

    while label:
        current = label
        while current:
            if current.next and current.next.value == label.value:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
            current = current.next
        label = label.next

    return head


# double_example = list2double(list_example)
# print_double(remove_duplicates_double(double_example))


def switch(prev, current, next):
    if prev is not None:
        prev.next = next
    current.next = next.next
    next.next = current
    return next


def sort_single(head):
    """
    Sort a single-linked list, only O(1) extra memory
    """
    done = False
    new_head = head
    while not done:
        prev = None
        current = new_head
        done = True
        while current.next:
            if current.value > current.next.value:
                if current is new_head:
                    new_head = current.next
                prev = switch(prev, current, current.next)
                done = False
            else:
                prev = current
                current = current.next

    return new_head


# print_single(sort_single(single_example))
# print_single(sort_single_switch(list2single(list_example)))


def switch_double(prev, current, next, next_next):
    if prev is not None:
        prev.next = next
    current.prev = next
    current.next = next_next
    next.next = current
    next.prev = prev
    if next_next is not None:
        next_next.prev = current
    return next


def sort_double(head):
    """
    Sort a double-linked list, only O(1) extra memory
    """
    done = False
    new_head = head
    while not done:
        prev = None
        current = new_head
        done = True
        while current.next:
            if current.value > current.next.value:
                done = False
                if current is new_head:
                    new_head = current.next
                prev = switch_double(prev, current, current.next, current.next.next)
            else:
                prev = current
                current = current.next

    return new_head


# print_double(sort_double(single_example))


example_palindrome = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
example_not_palindrome = [1, 2, 3, 4, 5, 6, 6, 7, 5, 4, 3, 2, 1]


def get_last(head):
    current = head
    while current.next:
        current = current.next
    return current


def palindrome_double(head):
    """
    Returns true iff the double link list is a palindrome
    """
    last = get_last(head)

    first_current = head
    second_current = last
    while first_current and second_current:
        if first_current.value == second_current.value:
            first_current = first_current.next
            second_current = second_current.prev
        else:
            return False

    if first_current is None and second_current is None:
        return True

    raise IndexError


print(palindrome_double(list2double(example_palindrome)))
print(palindrome_double(list2double(example_not_palindrome)))


def palindrome_single(head):

    first = head
    last = None
    while first:
        cursor = first
        while cursor.next is not last:
            cursor = cursor.next
        if first.value != cursor.value:
            return False
        first = first.next
        last = cursor
        if first is last or first is last.next:
            break
    return True


print(palindrome_single(list2single(example_palindrome)))
print(palindrome_single(list2single(example_not_palindrome)))
