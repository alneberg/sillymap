
def burrows_wheeler(text):
    """Returns the burrows wheeler transform of <text>.

    The text is assumed to not contain the character $"""

    text += "$"
    all_permutations = []
    for i in range(len(text)):
        all_permutations.append(text[i:] + text[:i])

    all_permutations.sort()
    return "".join([w[-1] for w in all_permutations])
