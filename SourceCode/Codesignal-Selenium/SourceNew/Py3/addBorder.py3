def addBorder(picture):
    
    l = len(picture[0])
    
    o = ['*' * (l + 2)]
    for i in picture:
        o += '*' + i + '*',
    o += '*' * (l + 2),
    return o
        
    

