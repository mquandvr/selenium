def differentValuesInMultiplicationTable2(n, m):
    x = []
    for i in range(n+1):
        for j in range(m+1):
            if i*j not in x:
                x.append(i*j)
    
    return len(x)-1

