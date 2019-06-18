def lastDigit(a, b):
    
    last = 1 
    for i in range(b):
        last = (last*a)%10 
    return last
