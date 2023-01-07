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
        "checks if there are any ships left on the board"
        if self._ships == 0:
            return 1

    def getBoard(self):
        """
        gets the game board
        :return: self.gameboard
        """
        matrix = []
        for i in self._gameBoard:
            matrix.append(i)
        return matrix

    def checkIfPlaceable(self, value, type):
        """
        Left-over Function, no need for it
        UI handles overlaps for the user and the ai generates ships so there are no overlaps
        :param value:
        :param type:
        :return:
        """
        return True

    def addShip(self, value, type):
        """
        function receives a ship and it's type so it can be added to the accordin repo
        :param value: any  type of ship
        :param type: string containing the type of the ship
        :return: return unplaceable if the ship couldn't be placed
        """
        if self.checkIfPlaceable(value, type):
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
        """
        when a ship gets hit, this function may get called, if the hit function returns a list
        the list would be containing the list of coordonates that the destroyed sheep is placed at
        and makes it disappear
        :param toSink:
        :return:
        """
        for sector in toSink:
            self._gameBoard[sector[0]][sector[1]] = self._water
        self._ships -= 1

    def checkIfHit(self, X, Y):
        """
        checks if the shot provided from the repo layer hit something, if it did, it checks if it is
        a blow that should cause sinking and call the apropiate function
        if not, it marks the ships with self._fire which is int value 2 or miss for -1
        :param X:
        :param Y:
        :return:
        """
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
        """
        dependent on checkIfHit from gameBoard
        this function is fed by the game layer the result from the shot, and it's coordonates
        basically this keeps track of the shots taken and their result accordongly
        :param X:
        :param Y:
        :param result:
        :return:
        """
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


def testFunction():
    testGame = StrategyBoard()
    carrier = Carrier(0, 0, 0, 4)
    testGame.addShip(carrier, 'carrier')
    checkBoard = []
    for i in range(10):
        checkBoard.append([0] * 10)
    checkBoard[0] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    assert checkBoard == testGame.getBoard()

    assert testGame.checkIfHit(2, 2) == 'miss'
    assert testGame.checkIfHit(0, 0) == 'hit'
    testGame.checkIfHit(0,0)
    testGame.checkIfHit(0,1)
    testGame.checkIfHit(0,2)
    testGame.checkIfHit(0,3)
    testGame.checkIfHit(0,4)
    checkBoard[0] = [0]*10
    assert checkBoard == testGame.getBoard()


    testGame = HitMatrix()
    testGame.noteShot(0,0, 'hit')
    testGame.noteShot(0,1, 'miss')
    checkBoard[0][0] = 1
    checkBoard[0][1] = -1
    assert testGame.getBoard() == checkBoard

testFunction()