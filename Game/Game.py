from Board.Board import StrategyBoard
from Board.Board import HitMatrix
from AI.AI import AI
from Ships.Carrier import Carrier
from Ships.Cruiser import Cruiser
from Ships.Battleship import Battleship
from Ships.Submarine import Submarine
from Ships.Destroyer import Destroyer

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
        """
        since we know the way the UI asks for ships, they can be added just by using their order in the list
        :param playerShip:
        :return:
        """
        if playerShip[1] =='carrier':
            self._player["shipBoard"].addShip(Carrier(playerShip[0][0], playerShip[0][1], playerShip[0][2], playerShip[0][3]), playerShip[1])
        if playerShip[1] =='battleship':
            self._player["shipBoard"].addShip(Battleship(playerShip[0][0], playerShip[0][1], playerShip[0][2], playerShip[0][3]), playerShip[1])
        if playerShip[1] =='cruiser':
            self._player["shipBoard"].addShip(Cruiser(playerShip[0][0], playerShip[0][1], playerShip[0][2], playerShip[0][3]), playerShip[1])
        if playerShip[1] =='destroyer':
            self._player["shipBoard"].addShip(Destroyer(playerShip[0][0], playerShip[0][1], playerShip[0][2], playerShip[0][3]), playerShip[1])
        if playerShip[1] =='submarine':
            self._player["shipBoard"].addShip(Submarine(playerShip[0][0], playerShip[0][1], playerShip[0][2], playerShip[0][3]), playerShip[1])

    def addComputerShips(self, computerShip):
        """
        since the ships come in a certain order, from the way the AI is structured, we know what each time will be from
        their position in the list
        :param computerShip:
        :return:
        """
        #list = [computerShip[0]._startRow, computerShip[0]._startCol,computerShip[0]._endRow,computerShip[0]._endCol]
        self._computer["shipBoard"].addShip(computerShip[0], 'carrier')
        #list = [computerShip[1]._startRow, computerShip[1]._startCol, computerShip[1]._endRow, computerShip[1]._endCol]
        self._computer["shipBoard"].addShip(computerShip[1], 'battleship')
        #list = [computerShip[2]._startRow, computerShip[2]._startCol, computerShip[2]._endRow, computerShip[2]._endCol]
        self._computer["shipBoard"].addShip(computerShip[2], 'cruiser')
        #list = [computerShip[3]._startRow, computerShip[3]._startCol, computerShip[3]._endRow, computerShip[3]._endCol]
        self._computer["shipBoard"].addShip(computerShip[3], 'destroyer')
        #list = [computerShip[4]._startRow, computerShip[4]._startCol, computerShip[4]._endRow, computerShip[4]._endCol]
        self._computer["shipBoard"].addShip(computerShip[4], 'destroyer')
        #list = [computerShip[5]._startRow, computerShip[5]._startCol, computerShip[5]._endRow, computerShip[5]._endCol]
        self._computer["shipBoard"].addShip(computerShip[5], 'submarine')
        #list = [computerShip[6]._startRow, computerShip[6]._startCol, computerShip[6]._endRow, computerShip[6]._endCol]
        self._computer["shipBoard"].addShip(computerShip[6], 'submarine')

    def startGame(self, playerShips):
        """
        initiates the game using the list given from the UI layer
        :param playerShips: list of ships and types
        :return: nothing, get the game going
        """
        for ship in playerShips:
            self.addPlayerShips(ship)
        computerShip = self._enemy.generateShips()
        self.addComputerShips(computerShip)

    def placeHits(self, X, Y):
        """
        receives the coordonates of the hit
        sends it to the Game layer where it is vertified if there was a hit and the extent of the damages
        if the hit causes a sink, the function asks for the remaining fleet size to see if there are any left
        and stops the game if so
        asks the ai to generate hits to do the same process for the ai
        :param X: int
        :param Y: int
        :return: 1 for player win, -1 for computer win, 0 for continue game
        """
        X = int(X)
        Y = int(Y)
        result = self._computer["shipBoard"].checkIfHit(X, Y)
        if result == 'sink':
            self._player["hitBoard"].noteShot(X, Y, 'sink')
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
            if self._player["shipBoard"]._repo.getFleetSize() == 0:
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
        """
        gets the current status of the player
        in form of the two matrixes explained in Board layers
        :return:
        """
        boards = []
        boards.append(self._player["shipBoard"].getBoard())
        boards.append(self._player["hitBoard"].getBoard())
        return boards