def equationSolutions(l, r):
    x = 0
    for i in range(l,r+1):
        for j in range(l,r+1):
            if i**2 == j**3:
                x+=1
    return x
