def passwordCheck(inputString):
    rs = [0,0,0,0]
    if len(inputString) >= 5:
        rs[0] = 1
    for i in inputString:
        if 'A' <= i <= 'Z':
            rs[1]= 1
        elif 'a' <= i <= 'z':
            rs[2] = 1
        elif '0' <= i <='9':
            rs[3] = 1
            
    return sum(rs) == 4
