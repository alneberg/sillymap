import numpy as np

def burrows_wheeler(text):
    """Calculates the burrows wheeler transform of <text>.

    returns the burrows wheeler string and the suffix array indices
    The text is assumed to not contain the character $"""

    text = np.append(text,0)
    seq_len = len(text)
    # suffix array indices
    sa_i = my_suffix_sort(text, seq_len)

    # burrows wheeler
    bw = text[sa_i - 1]

    return bw, sa_i

def my_suffix_sort(input_dna_array, seq_len):
    """My sort method for suffix arrays of an numpy array consisting of 0,1,2,3,4 :s only"""
    original_index = np.arange(seq_len)
    return _recursive_sort(original_index, input_dna_array, 0)

def _recursive_sort(indices, input_dna_array, iteration):
    output = np.negative(np.ones_like(indices))
    index = 0
    for val in [0,1,2,3,4]:
        new_indices = indices[np.where(input_dna_array[indices + iteration] == val)]
        ind_len = len(new_indices)
        if ind_len > 1:
            output[index:index+ind_len] = _recursive_sort(new_indices, input_dna_array, iteration+1)
            index += ind_len
        elif ind_len == 1:
            output[index] = new_indices
            index += 1
    return output
