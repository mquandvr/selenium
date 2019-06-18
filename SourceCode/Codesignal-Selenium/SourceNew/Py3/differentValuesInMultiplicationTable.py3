def differentValuesInMultiplicationTable(n, m):
    s = set() 
    for i in range(n): 
        for j in range(m): 
            s.add((i+1) * (j+1)) 
    return len(s)
