def multiplicationTable(n):
    return list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
