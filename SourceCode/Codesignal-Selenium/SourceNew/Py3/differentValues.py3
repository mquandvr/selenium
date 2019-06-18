def differentValues(a, d):

    best = -1
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            diff = abs(a[i] - a[j])
            if diff <= d and best < diff:
                best = diff

    return best
