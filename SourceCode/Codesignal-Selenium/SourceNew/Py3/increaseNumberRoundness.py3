def increaseNumberRoundness(n):
    trail = True
    for c in str(n)[::-1]:
        if c != '0':
            trail = False
            
        if c == '0' and not trail:
            return True
        
    return False