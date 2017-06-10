class SubString(object):
    # Class written by @MSeifert:
    # https://stackoverflow.com/a/41669542
    # slots reduce the memory overhead of the instances
    __slots__ = ('str_', 'idx')

    def __init__(self, str_, idx):
        self.str_ = str_
        self.idx = idx

    # sorted only requires "<" to be implemented so we only need __lt__
    def __lt__(self, other):
        # temporarly create explicit substrings but only temporaries for the comparison
        return self.str_[self.idx:] + self.str_[:self.idx] < other.str_[other.idx:] + other.str_[:other.idx]

    def __repr__(self):
        return self.idx

def burrows_wheeler(text):
    """Calculates the burrows wheeler transform of <text>.

    returns the burrows wheeler string and the suffix array indices
    The text is assumed to not contain the character $"""

    text += "$"

    # suffix arrau indices
    sa_i = list(range(len(text)))
    sa_i.sort(key=lambda i: SubString(text, i))

    # burrows wheeler as list
    bw_l = [text[i-1] for i in sa_i]

    return "".join(bw_l), sa_i
