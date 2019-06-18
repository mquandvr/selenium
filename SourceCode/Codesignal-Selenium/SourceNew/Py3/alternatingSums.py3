def alternatingSums(a):
    return sum(a[i] for i in range(0, len(a), 2)), sum(a[i] for i in range(1, len(a), 2))
