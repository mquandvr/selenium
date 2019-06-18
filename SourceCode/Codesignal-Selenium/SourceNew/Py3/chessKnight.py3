def chessKnight(cell):
    s = {0:0, 1:2, 2:4, 3:5, 4:6}
    x = sum([cell[0]<'b',cell[0]<'c',cell[0]>'f',cell[0]>'g',
           cell[1]<'2',cell[1]<'3',cell[1]>'6',cell[1]>'7'])
    return 8 - s[x]