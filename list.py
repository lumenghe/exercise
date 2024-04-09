class SingleList(object):
    def __init__(self, value: int):
        self.value = value
        self.next = None


class DoubleList(object):
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


list_example = [5,1,2,3,4,9,7,7,4,5,6,6,3,1,0,1,4,5,6,7,8,1,6,9,7,1,2,3]


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
    
print(len(list_example))
print(length_single(single_example))


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
    

print(length_double(double_example))


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
    
    
print(max_single(single_example))

def max_double(head):
    """
    Get maximum of a double-linked list
    """
    current = head
    max = head.value
    while current:
        if max<current.value:
            max = current.value
        current = current.next
        
    return max
print ('max double=', max_double(double_example) == max(list_example))

    
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

print_single(single_example)
print_single(revert_single(single_example))
    
