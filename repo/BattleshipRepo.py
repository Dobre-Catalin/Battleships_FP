from Ships.Battleship import Battleship

class BattleshipRepo():
    def __init__(self):
        self._data = []

    def getLen(self):
        res = len(self._data)
        return res

    def getList(self):
        list = self._data
        return list

    def add(self, value):
        self._data.append(value)
    def removeAtPosition(self, position):
        if (len(self._data) == 1):
            self._data = []
            return
        self._data = self._data[:position-1] + self._data[position:]

    def __str__(self):
        return str(self._data)