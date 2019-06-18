def chessKnightMoves(cell):
    a=ord(cell[0])
    b=ord(cell[1])
    a=[(a+2,b+1),(a+2,b-1),(a+1,b+2),(a+1,b-2),(a-2,b+1),(a-2,b-1),(a-1,b+2),(a-1,b-2)]
    count=0
    for x,y in a:
        if x in range(97,105) and y in range(49,57):
            count+=1
    return count
    



