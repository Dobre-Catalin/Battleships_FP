from repo.ShipRepo import ShipRepo
from Ships.Battleship import Battleship
from Ships.Cruiser import Cruiser
from Ships.Carrier import Carrier
from Ships.Submarine import Submarine
from Ships.Destroyer import Destroyer

class StrategyBoard():
    _water = 0
    _ship = 1
    _fire = 2
    def __init__(self):
        super().__init__()
        self._gameBoard = []
        for i in range(10):
            self._gameBoard.append([self._water] * 10)
        self._ships = 0
        self._repo = ShipRepo()

    def isLost(self):
        if self._ships == 0:
            return 1

    def getBoard(self):
        matrix = []
        for i in self._gameBoard:
            matrix.append(i)
        return matrix

    def checkIfPlaceable(self, value, type):
        return True

    def addShip(self, value, type):
        if self.checkIfPlaceable(value, type):
        #     if value[0] == value[2]:
        #         up = min(value[3], value[1])
        #         down = max(value[3], value[1])
        #         for position in range(up, down+1):
        #             self._gameBoard[value[0]][position] = 1
        #     else:
        #         left = min(value[2], value[0])
        #         right = max(value[0], value[2])
        #         for position in range(left, right + 1):
        #             self._gameBoard[position][value[3]] = 1
            coord = value.getOccupiedCoordonates()
            for co in coord:
                self._gameBoard[co[0]][co[1]] = 1

            if type == 'carrier':
                self._repo.addCarrier(value)
            if type == 'battleship':
                self._repo.addBattleship(value)
            if type == 'cruiser':
                self._repo.addCruiser(value)
            if type == 'destroyer':
                self._repo.addDestroyer(value)
            if type == 'submarine':
                self._repo.addSubmarine(value)
            self._ships += 1
        else:
            return 'unplaceable'

    def sinkShip(self, toSink):
        for sector in toSink:
            self._gameBoard[sector[0]][sector[1]] = self._water
        self._ships -= 1

    def checkIfHit(self, X, Y):
        X = int(X)
        Y = int(Y)
        element = self._gameBoard
        if int(element[X][Y]) == int(self._ship):
            result = self._repo.registerHit(X, Y)
            if type(result) == list:
                self.sinkShip(result)
                return 'sink'
            elif result == 'hit':
                self._gameBoard[X][Y] = self._fire
                return 'hit'
            else:
                return 'miss'
        else:
            return 'miss'

    def __str__(self):
        toPrint = ''
        for i in range(10):
            toPrint += f'{self._gameBoard[i]}\n'
        return toPrint


class HitMatrix():
    """
    0 - water
    1 - hit
    -1 - miss
    :return:
    """
    def __init__(self):
        self._historyBoard = []
        for i in range(10):
            self._historyBoard.append([0] * 10)
        self._ships = 0

    def noteShot(self, X, Y, result):
        X = int(X)
        Y = int(Y)
        res = 0
        if result == 'hit' or result == 'sink':
            res = 1
            self._historyBoard[X][Y] = res
        elif result == 'miss':
            res = -1
            self._historyBoard[X][Y] = res

    def getBoard(self):
        return self._historyBoard


    def __str__(self):
        toPrint = ''
        for i in range(10):
            toPrint += f'{self._historyBoard[i]}\n'
        return toPrint
