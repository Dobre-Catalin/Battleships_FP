from Ships.Battleship import Battleship

class BattleshipRepo():
    def __init__(self):
        self._data = []

    def getLen(self):
        return len(self._data)

    def getList(self):
        list = self._data
        return list

    def add(self, value):
        self._data.append(value)
    def removeAtPosition(self, position):
        self._data = self._data[:position-1] + self._data[position:]

    def __str__(self):
        return str(self._data)