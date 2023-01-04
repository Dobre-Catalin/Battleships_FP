from Ships.Submarine import Submarine

class SubmarineRepo():
    def __init__(self):
        self._data = []

    def getList(self):
        return self._data

    def getLen(self):
        res = len(self._data)
        return res

    def add(self, value):
        self._data.append(value)

    def removeAtPosition(self, position):
        if len(self._data) == 1:
            self._data = []
        elif position == 0:
            self._data = [self._data[1]]
        elif position == 1:
            self._data = [self._data[0]]

    def __str__(self):
        return str(self._data)