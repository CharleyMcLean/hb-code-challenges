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
    letters = {}
    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
        # alternatively?
        # letters.get() syntax?

    for letter in letters... 
    # check for even number of letters


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
