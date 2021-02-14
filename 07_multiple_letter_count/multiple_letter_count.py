def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    word_counter = {}

    for ltr in phrase:
        word_counter[ltr] = word_counter.get(ltr, 0) + 1

        return word_counter


# print(multiple_letter_count("Yay")) #>>>>>>> This is a bit tricky, I do not get the same result when I print, as when I run the function with the argument in the terminal

# In[12]: % run multiple_letter_count.py
# {'Y': 1}

# In[8]: multiple_letter_count('Yay') >>>>>>>>>>>  This is the result I get when I run stray in the terminal
# Out[8]: {'Y': 1, 'a': 1, 'y': 1}
