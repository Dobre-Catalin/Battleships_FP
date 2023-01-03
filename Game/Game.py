from Board.Board import StrategyBoard
from Board.Board import HitMatrix
from AI.AI import AI

class Game():
    def __init__(self):
        self._player = {
            "shipBoard": StrategyBoard(),
            "hitBoard": HitMatrix()
        }
        self._computer = {
            "shipBoard": StrategyBoard(),
            "hitBoard": HitMatrix()
        }
        self._enemy = AI()

    def addPlayerShips(self, playerShip):
        self._player["shipBoard"].addShip(playerShip[0], playerShip[1])

    def addComputerShips(self, computerShip):
        list = [computerShip[0]._startRow, computerShip[0]._startCol,computerShip[0]._endRow,computerShip[0]._endCol]
        self._computer["shipBoard"].addShip(list, 'carrier')
        list = [computerShip[1]._startRow, computerShip[1]._startCol, computerShip[1]._endRow, computerShip[1]._endCol]
        self._computer["shipBoard"].addShip(list, 'battleship')
        list = [computerShip[2]._startRow, computerShip[2]._startCol, computerShip[2]._endRow, computerShip[2]._endCol]
        self._computer["shipBoard"].addShip(list, 'cruiser')
        list = [computerShip[3]._startRow, computerShip[3]._startCol, computerShip[3]._endRow, computerShip[3]._endCol]
        self._computer["shipBoard"].addShip(list, 'destroyer')
        list = [computerShip[4]._startRow, computerShip[4]._startCol, computerShip[4]._endRow, computerShip[4]._endCol]
        self._computer["shipBoard"].addShip(list, 'destroyer')
        list = [computerShip[5]._startRow, computerShip[5]._startCol, computerShip[5]._endRow, computerShip[5]._endCol]
        self._computer["shipBoard"].addShip(list, 'submarine')
        list = [computerShip[6]._startRow, computerShip[6]._startCol, computerShip[6]._endRow, computerShip[6]._endCol]
        self._computer["shipBoard"].addShip(list, 'submarine')

    def startGame(self, playerShips):
        for ship in playerShips:
            self.addPlayerShips(ship)
        computerShip = self._enemy.generateShips()
        self.addComputerShips(computerShip)

    def placeHits(self, X, Y):
        X = int(X)
        Y = int(Y)
        result = self._computer["shipBoard"].checkIfHit(X, Y)
        if result == 'sink':
            self._player["hitBoard"].noteShot(X, Y, 'hit')
            if self._computer["shipBoard"]._repo.getFleetSize() == 0:
                return 1
        elif result == 'miss':
            self._player["hitBoard"].noteShot(X, Y, result)
        elif result == 'hit':
            self._player["hitBoard"].noteShot(X, Y, result)

        toHit = self._enemy.doMove()
        result = self._player["shipBoard"].checkIfHit(toHit[0], toHit[1])
        if result == 'sink':
            self._computer["hitBoard"].noteShot(X, Y, 'hit')
            if self._player["shipBoard"].getFleetSize() == 0:
                self._enemy.setLastResult(result)
                return -1
        elif result == 'hit':
            self._computer["hitBoard"].noteShot(X, Y, result)
            self._enemy.setLastResult(result)
        elif result == 'miss':
            self._computer["hitBoard"].noteShot(X, Y, result)
            self._enemy.setLastResult(result)
        return 0

    def getBoardsPlayer(self):
        boards = []
        boards.append(self._player["shipBoard"].getBoard())
        boards.append(self._player["hitBoard"].getBoard())
        return boards


