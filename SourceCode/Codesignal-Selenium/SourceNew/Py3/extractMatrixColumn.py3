def extractMatrixColumn(matrix, column):
    return list(matrix[i][column] for i in range(len(matrix)))
