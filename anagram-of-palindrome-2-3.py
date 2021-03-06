# Whiteboard Medium
# Challenge Easier
# Concepts Dictionaries, General


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

        >>> is_anagram_of_palindrome("a")
        True

        >>> is_anagram_of_palindrome("ab")
        False

        >>> is_anagram_of_palindrome("aab")
        True

        >>> is_anagram_of_palindrome("arceace")
        True

        >>> is_anagram_of_palindrome("arceaceb")
        False
    """
    if not word:
        return False

    # Create an empty dictionary to store the letters and their counts.
    letters = {}
    for letter in word:
        letters[letter] = letters.get(letter, 0) + 1

    # If either all letter counts are even, or all are even except one that has
    # a value of one, then return True.
    # Create a counter for letters with the value of 1, skip the letters with
    # value 2, and counter for all others.
    one_count = 0
    other_odd_count = 0

    for num in letters.values():
        if num == 1:
            one_count += 1
        elif num % 2 == 0:
            continue
        else:
            other_odd_count += 1

    if (one_count == 1 and not other_odd_count) or (not one_count and not other_odd_count):
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
