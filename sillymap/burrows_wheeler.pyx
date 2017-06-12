class SubString(object):
    # Class written by @MSeifert:
    # https://stackoverflow.com/a/41669542
    # slots reduce the memory overhead of the instances
    __slots__ = ('str_', 'idx', 'str_len')

    def __init__(self, str_, idx, str_len):
        self.str_ = str_
        self.idx = idx
        self.str_len = str_len

    # sorted only requires "<" to be implemented so we only need __lt__
    def __lt__(self, other):
        # temporarly create explicit substrings but only temporaries for the comparison
        #Optimized case to speed things up
        if self.idx + 10 < self.str_len and other.idx + 10 < self.str_len:
            if self.str_[self.idx:self.idx+10] < other.str_[other.idx:other.idx+10]:
                return True
            elif self.str_[self.idx:self.idx+10] > other.str_[other.idx:other.idx+10]:
                return False
        # this is the general case
        return self.str_[self.idx:] + self.str_[:self.idx] < other.str_[other.idx:] + other.str_[:other.idx]

    def __repr__(self):
        return self.idx

def burrows_wheeler(text):
    """Calculates the burrows wheeler transform of <text>.

    returns the burrows wheeler string and the suffix array indices
    The text is assumed to not contain the character $"""

    text += "$"

    text_len = len(text)
    # suffix arrau indices
    sa_i = list(range(text_len))
    sa_i.sort(key=lambda i: SubString(text, i, text_len))

    # burrows wheeler as list
    bw_l = [text[i-1] for i in sa_i]

    return "".join(bw_l), sa_i
