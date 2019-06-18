def digitSum(n):
    rs=0
    for i in list(str(n)):
        rs +=int(i)
    return rs