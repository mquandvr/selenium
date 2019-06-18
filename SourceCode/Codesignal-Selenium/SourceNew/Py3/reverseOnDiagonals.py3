def reverseOnDiagonals(matrix):
    left = [matrix[i][i] for i in range(len(matrix))]
    print(left)
    right = [matrix[i][-(i+1)] for i in range(len(matrix))]
    print(right)

    for i in range(len(matrix)):
        matrix[i][i] = left[-(i+1)]
        matrix[i][-(i+1)] = right[-(i+1)]
    return matrix