def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    to_swap = to_swap.lower()

    swapping_ltr = [
        (ltr.swapcase() if ltr.lower() == to_swap else ltr)
        for ltr in phrase
    ]

    return ''.join(swapping_ltr)


print(flip_case('Aaaahhh', 'a'))
