def isMonotonous(a):
    return all(a[i] < a[i-1] for i in range(1, len(a))) or all(a[i] > a[i-1] for i in range(1, len(a)))
