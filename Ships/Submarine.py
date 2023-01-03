class Submarine():
    def __init__(self, startRow, startCol, endRow, endCol):
        self._startRow = startRow
        self._startCol = startCol
        self._endRow = endRow
        self._endCol = endCol
        self._hitpoints = 1

    def gotHit(self):
        self._hitpoints-=1
        if self._hitpoints == 0:
            return -1
        return self._hitpoints

    def getOccupiedCoordonates(self):
        ocupiedSectors = []
        # vertical
        if self._startCol == self._endCol:
            left = min(self._endRow, self._startRow)
            right = max(self._startRow, self._endRow)
            for position in range(left, right + 1):
                ocupiedSectors.append([position, self._startCol])
        # horizontal
        else:
            up = min(self._startRow, self._startCol)
            down = max(self._startRow, self._startCol)
            for position in range(up, down+1):
                ocupiedSectors.append([self._endRow, position])
        return ocupiedSectors

    def getType(self):
        return "submarine"