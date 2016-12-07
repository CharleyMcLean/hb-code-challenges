# Whiteboard Easier
# Concepts Lists


def concat_lists(list1, list2):
    """Combine lists.
        >>> concat_lists([1, 2], [3, 4])
        [1, 2, 3, 4]

        >>> concat_lists([], [1, 2])
        [1, 2]

        >>> concat_lists([1, 2], [])
        [1, 2]

        >>> concat_lists([], [])
        []

    """

    # If we didn't put these on sep lines, (just returned list1.extend(list2)),
    # the function would have returned None.
    # Also, if we'd used append instead, for test1, we would have gotten:
    # [1, 2, [3, 4]]
    list1.extend(list2)
    return list1

#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
