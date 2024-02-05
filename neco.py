def add_int(m, n):
    """Returns the sum of two positive integers
    Usage examples:
    >>> add_int(5, 6)
    11

    Function accepts only positive numbers:
    >>> add_int(5, -3)
    Traceback (most recent call last):
    ValueError: m and n needs to be positive integers
    """

    if m < 0 or n < 0:
        raise ValueError("m and n needs to be positive integers")

    return m + n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
