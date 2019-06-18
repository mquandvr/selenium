def firstReverseTry(arr):
    if len(arr) > 1:
        return arr[-1:] + arr[1:-1] + arr[:1]
    else:
        return arr[::-1]
