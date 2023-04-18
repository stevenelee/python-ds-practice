from functools import reduce

def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    evens = [n for n in nums if n % 2 == 0]
    return reduce(product, evens, 1)

def product(a, b):
    return a * b