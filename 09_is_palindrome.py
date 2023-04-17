def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_no_space = phrase.replace(" ", "")
    phrase_lower = phrase_no_space.lower()
    phrase_list = list(phrase_lower)
    phrase_list.reverse()
    reverse_phrase = "".join(phrase_list)

    return phrase.replace(" ", "").lower() == reverse_phrase
