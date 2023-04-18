def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newStr = ""
    to_swap_lower = to_swap.lower()
    for c in phrase:
        newStr += c.swapcase() if c.lower() == to_swap_lower else c
    return newStr
