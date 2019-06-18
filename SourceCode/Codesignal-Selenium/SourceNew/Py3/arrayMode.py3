import collections

def arrayMode(sequence):
    vs = collections.Counter(sequence)
    return vs.most_common(1)[0][0]
