from collections import Counter

def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = Counter(nums)

    max = 0
    most_common_num = 0
    for k in counter.keys():
        freq = counter[k]
        if (freq > max):
            max = freq
            most_common_num = k

    return most_common_num