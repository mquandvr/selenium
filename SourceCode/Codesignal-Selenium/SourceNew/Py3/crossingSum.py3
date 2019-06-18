def crossingSum(matrix, row, column):

    result = 0
    for i in range(len(matrix)):
        result += matrix[i][column]
    for i in range(len(matrix[0])):
        result += matrix[row][i]
    result -= matrix[row][column]

    return result
