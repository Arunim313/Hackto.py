class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Function to find the intersection point of two linked lists using hashing
def findIntersection(first, second):

    nodes = set()

    while first:
        nodes.add(first)
        first = first.next

    while second:
        if second in nodes:
            return second
        second = second.next

    return None


if __name__ == '__main__':

    first = None
    for i in reversed(range(1, 6)):
        first = Node(i, first)

    second = None
    for i in reversed(range(1, 4)):
        second = Node(i, second)

    second.next.next.next = first.next.next.next

    addr = findIntersection(first, second)
    if addr:
        print('The intersection point is', addr.data)
    else:
        print('The lists do not intersect.')
