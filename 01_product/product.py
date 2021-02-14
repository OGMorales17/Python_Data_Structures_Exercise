def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    # if type(a) and type(b) is int:
    if type(a) is int and type(b) is int:
        return a * b


print(product(2, 2))
print(product(2, -2))
