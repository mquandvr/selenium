def matrixTrace(matrix):

    s = 0
    for i in range(len(matrix)):
        s+= matrix[i][i]
    return s