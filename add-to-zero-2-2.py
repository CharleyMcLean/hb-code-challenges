# Whiteboard - easier
# Concepts - loops, general


def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.
        >>> add_to_zero([])
        False

        >>> add_to_zero([1])
        False

        >>> add_to_zero([1, 2, 3])
        False

        >>> add_to_zero([1, 2, 3, -2])
        True

        >>> add_to_zero([0, 1, 2])
        True
    """
    if not nums:
        return False

    for num in nums:
        if (num * -1) in nums or num == 0:
            return True

    return False

#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
