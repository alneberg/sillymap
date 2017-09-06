import numpy as np
import warnings

class Rank():
    """Rank table corresponding to http://alexbowe.com/fm-index/ except 0-indexed.

    The rank(i,c) is the number of occurencies of c within text[0:(i+1)]

    public methods:
    add_text(text) -- initialize the rank for text.
    rank(i,c) -- returns rank of character c in intercal [0:i] 

    ex:

    rank = Rank()
    rank.add_text("ipssm$pissii")
    rank.rank(-1,i) = 0
    rank.rank("ipssm$pissii")[0,i] = 1
    rank.rank("ipssm$pissii")[11,s] = 4
    """

    def __init__(self):
        self.rank_dict = {}
        self.zero_ix = None
        self.constructed = False

    def add_text(self, text):
        # Zero is a special case, only has one occurrence
        self.zero_ix = np.where(text == 0)[0]
       
        text_len = len(text)
        if text_len > 2**32:
            dtype_for_array = 'uint64'
        else:
            dtype_for_array = 'uint32'

        # Store rank in array 
        self.rank_dict = np.zeros((len(text),5), dtype=dtype_for_array)
        for char in [0,1,2,3,4]:
            tmp_array = np.zeros_like(text, dtype=dtype_for_array)
            tmp_array[np.where(text == char)] = 1
            self.rank_dict[:,char] = np.cumsum(tmp_array)
        
        self.constructed = True

    def rank(self, i, c):
        """Should only be called if self.constructed is True.
        For speed reasons, this is not checked at every call."""
        if i != -1:
            return self.rank_dict[i,c]
        else:
            return 0

