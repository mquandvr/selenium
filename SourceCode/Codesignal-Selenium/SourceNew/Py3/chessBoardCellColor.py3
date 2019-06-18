def chessBoardCellColor(cell1, cell2):
    def cellval(cell):
        return " ABCDEFGH".index(cell[0]) + int(cell[1])
    
    return cellval(cell1)%2 == cellval(cell2)%2
