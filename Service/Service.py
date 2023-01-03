from Game.Game import Game
from Ships.Carrier import Carrier
from Ships.Battleship import Battleship
from Ships.Cruiser import Cruiser
from Ships.Destroyer import Destroyer
from Ships.Submarine import Submarine

class Service():
    def __init__(self):
        self._game = Game()

    def start(self, player, computer):
        self.game.startGame(player, computer)

    def getPlayerSituation(self):
        return self._game.getBoardsPlayer()

    def addShip(self, listOfShips):
        self._game.addPlayerShips()