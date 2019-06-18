def growingPlant(upSpeed, downSpeed, desiredHeight):
    cnt = 0
    h = 0
    while h < desiredHeight: 
        if cnt % 2 == 0: 
            h += upSpeed 
        else: 
            h -= downSpeed 
        cnt +=1
    return cnt //2 + 1
