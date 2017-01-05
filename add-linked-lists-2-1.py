class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.
        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    # Create reversed strings of the two linked lists
    l1_rev = l1.as_rev_string()
    l2_rev = l2.as_rev_string()

    # Assuming the lengths of l1_rev and l2_rev are equal
    out = []
    for i in range(len(l1_rev)):
        # each char in l1_rev and l2_rev must first be turned into integers
        # so they may be added
        out.append(str(int(l1_rev[i]) + int(l2_rev[i])))
        i += 1

    return "".join(out)
