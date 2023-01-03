from Game.Game import Game
from Ships.Carrier import Carrier
from Ships.Battleship import Battleship
from Ships.Cruiser import Cruiser
from Ships.Destroyer import Destroyer
from Ships.Submarine import Submarine

class InvalidCoordonates(Exception):
    pass

class UI:
    def __init__(self):
        self.game = Game()

    def start(self):
        print("Ships given:\n"
              "1x Aircraft Carrier\n"
              "1x Battleship\n"
              "1x Cruiser\n"
              "2x Destroyer\n"
              "2x Submarine\n")
        print("Place the ships:")
        ships = self.inputFleet()
        self.game.startGame(ships)
        self.showCurrentStatus()
        self.runGame()

    def runGame(self):
        isWon = 0
        while(isWon == 0):
            X = input("row to hit:")
            Y = input("col to hit:")
            isWon = self.game.placeHits(X, Y)
            self.showCurrentStatus()
        if isWon == 1:
            print("Congrats")
            exit(0)
        if isWon == -1:
            print("GG")

    def showCurrentStatus(self):
        lists = self.game.getBoardsPlayer()
        ships = lists[0]
        shots = lists[1]
        for i in range(len(ships)):
            print(ships[i])
        print("\n")
        for i in range(len(ships)):
            print(shots[i])
        print("\n")

    def inputFleet(self):
        ships = []
        current = self.inputShip()
        ships.append([current, 'carrier'])
        current = self.inputShip()
        ships.append([current, 'battleship'])
        current = self.inputShip()
        ships.append([current, 'cruiser'])
        current = self.inputShip()
        ships.append([current, 'destroyer'])
        current = self.inputShip()
        ships.append([current, 'destroyer'])
        current = self.inputShip()
        ships.append([current, 'submarine'])
        current = self.inputShip()
        ships.append([current, 'submarine'])
        return ships

    def inputShip(self):
        startRow = int(input("Start Row:"))
        startCol = int(input("Start Col:"))
        endRow = int(input("End Row:"))
        endCol = int(input("End Col:"))
        coordonates = [startRow, startCol, endRow, endCol]
        return coordonates


if __name__ == "__main__":
    ui = UI()
    ui.start()