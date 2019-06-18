def divisorsSubset(subset, n):

    res = 0

    for i in range(1, n+1):
        correct = True
        for j in range(len(subset)):
            if i % subset[j] != 0:
                correct = False
        if correct:
            res += 1

    return res
