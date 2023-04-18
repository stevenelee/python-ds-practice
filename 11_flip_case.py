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
    to_swap_upper = to_swap.upper()
    for c in phrase:
        if c == to_swap_lower:
            newStr += to_swap_upper
        elif c == to_swap_upper:
            newStr += to_swap_lower
        else:
            newStr += c
    return newStr
