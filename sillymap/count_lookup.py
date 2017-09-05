import numpy as np

def count_lookup(text):
    """Returns a lookup table for c, returning the 
    number of characthers in text lexically smaller than c.
    """
    unique, char_count = np.unique(text, return_counts=True)
    lookup = {}

    current_count = 0
    for val, count in zip(unique, char_count):
        lookup[val] = current_count
        current_count += count

    return lookup
