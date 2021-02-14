import functools
import operator


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

    return functools.reduce(operator.mul, [i for i in nums if i % 2 == 0], 1)


# https: // realpython.com/python-reduce-function/
# https: // docs.python.org/3/library/operator.html
# https://stackoverflow.com/questions/48802297/sum-a-list-with-different-operator-in-python/48802430
