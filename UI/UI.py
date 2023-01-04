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

    def endGame(self, type):
        if type == 1:
            print("You win")
        else:
            print("GG")

    def runGame(self):
        """
        Asks for input and cheks if the move ends the game
        :return:
        """
        isWon = 0
        while(isWon == 0):
            while True:
                try:
                    X = int(input("row to hit:"))
                    break
                except ValueError:
                    print("Invalid Coordonates")

            while True:
                try:
                    Y = int(input("COL to hit:"))
                    break
                except ValueError:
                    print("Invalid Coordonates")

            isWon = self.game.placeHits(X, Y)
            self.showCurrentStatus()
        if isWon == 1 or isWon == -1:
            self.endGame(isWon)

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

    def notInFleet(self, current, fleet):
        currentCoordonates = current.getOccupiedCoordonates()
        for i in range(len(fleet)):
            itemInFleet = fleet[i]
            for sector in itemInFleet.getOccupiedCoordonates():
                if sector in currentCoordonates:
                    return False
        return True

    def inputFleet(self):
        ships = []
        fleet =[]
        current = self.inputShip()
        fleet.append(Carrier(current[0],current[1],current[2],current[3]))
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
        while True:
            try:
                startRow = int(input("Start Row:"))
                break
            except ValueError:
                print("Invalid Coordonates")
        while True:
            try:
                startCol = int(input("Start Col:"))
                break
            except ValueError:
                print("Invalid Coordonates")
        while True:
            try:
                endRow = int(input("End Row:"))
                break
            except ValueError:
                print("Invalid Coordonates")
        while True:
            try:
                endCol = int(input("End Col:"))
                break
            except ValueError:
                print("Invalid Coordonates")
        coordonates = [startRow, startCol, endRow, endCol]
        return coordonates


if __name__ == "__main__":
    ui = UI()
    ui.start()