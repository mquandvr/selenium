def fixedPointsPermutation(permutation):
    return sum([1 if i + 1 == permutation[i] else 0 for i in range(len(permutation))])
