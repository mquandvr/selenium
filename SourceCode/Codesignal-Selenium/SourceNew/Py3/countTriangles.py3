def countTriangles(x, y):

    result = 0
    for i in range(1,len(x)):
        for j in range(i + 1, len(x)):
            for k in range(j + 1, len(x)):
                doubleArea = ((x[i] - x[j]) * (y[i] - y[k])
                          - (x[i] - x[k]) * (x[i] - x[j]))
                if doubleArea != 0:
                    result += 1
    return result
