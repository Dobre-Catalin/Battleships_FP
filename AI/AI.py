import random
import copy
from Ships.Battleship import Battleship
from Ships.Submarine import Submarine
from Ships.Cruiser import Cruiser
from Ships.Destroyer import Destroyer
from Ships.Carrier import Carrier

class AI():
    def __init__(self):
        self._phase = 'scout'
        self._lastResult = 'start'
        self._innerShot = []
        self._allShots = []
        self._shipShot = []

    def placeShips(self):
        starRow = random.randint(0, 9)

    def setLastResult(self, result):
        self._lastResult = result

    def addShipShot(self, value):
        self._shipShot.append(value)

    def addAllShots(self, value):
        self._allShots.append(value)

    def resetShipShot(self):
        self._shipShot = []

    def selectPhase(self):
        pass

    def scoutPhase(self):
        """
        function shots random shots either anywgere in the arena, or using the bias variable
        it may shoot somewhere in the center sector of the matrix, where statistically, there
        are odds of finding something, especially larger ships
        :return:
        """
        bias = random.randint(1, 10)
        if len(self._innerShot) <= 15 and bias > 7:
            X = random.randint(3, 6)
            Y = random.randint(3, 6)
            while [X, Y] in self._allShots:
                X = random.randint(3, 6)
                Y = random.randint(3, 6)
            self._innerShot.append([X,Y])
            self.addAllShots([X, Y])
            print([X, Y])
            return [X, Y]
        else:
            X = random.randint(0, 9)
            Y = random.randint(0, 9)
            while [X, Y] in self._allShots:
                X = random.randint(0, 9)
                Y = random.randint(0, 9)
            self.addAllShots([X, Y])
            if X >= 3 and X <= 6:
                if Y >= 3 and Y <= 6:
                    self._innerShot.append([X, Y])
            print([X,Y])
            return [X, Y]

    def checkShot(self, X, Y):
        if X > 9 or Y > 9:
            return False
        if X < 0 or Y < 0:
            return False
        if [X,Y] in self._allShots:
            return False
        return True

    def attackPhase(self):
        if self._lastResult == 'hit':
            if self._shipShot == []:
                #self._shipShot.append(self._allShots[-1])
                nextShot = copy.deepcopy(self._allShots[-1])
            else:
                nextShot = copy.deepcopy(self._shipShot[-1])
        nextShot[0] = int(nextShot[0])
        nextShot[1] = int(nextShot[1])
        sequnece = [0, 1, -1]
        pas = False
        tries = 0
        while pas == False and tries != 10:
            nextShot[0] = nextShot[0] + random.choice(sequnece)
            nextShot[1] = nextShot[1] + random.choice(sequnece)
            pas = self.checkShot(nextShot[0], nextShot[1])
            tries += 1
        if tries == 10:
            self.resetShipShot()
            return self.scoutPhase()
        return nextShot

    def notInFleet(self, current, fleet):
        currentCoordonates = current.getOccupiedCoordonates()
        for i in range(len(fleet)):
            itemInFleet = fleet[i]
            for sector in itemInFleet.getOccupiedCoordonates():
                if sector in currentCoordonates:
                    return False
        return True

    def generateOne(self, lenght, fleet):
        startingPointX = random.randint(0, 9)
        startingPointY = random.randint(0, 9)
        fits = False
        while fits == False:
            direction = random.randint(0, 3)
            if direction == 0:
                if lenght == 1:
                    current = Submarine(startingPointX, startingPointY, startingPointX, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 2 and (startingPointX + 1 < 10 and startingPointX > -1):
                    current = Destroyer(startingPointX, startingPointY, startingPointX + 1, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 3 and (startingPointX + 2 < 10 and startingPointX > -1):
                    current = Cruiser(startingPointX, startingPointY, startingPointX + 2, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 4 and (startingPointX + 3  < 10 and startingPointX > -1):
                    current = Battleship(startingPointX, startingPointY, startingPointX + 3, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 5 and (startingPointX + 4  < 10 and startingPointX > -1):
                    current = Carrier(startingPointX, startingPointY, startingPointX + 4, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
            if direction == 1:
                if lenght == 1:
                    current = Submarine(startingPointX, startingPointY, startingPointX, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 2 and startingPointX -1 > -1:
                    current = Destroyer(startingPointX, startingPointY, startingPointX - 1, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 3 and startingPointX - 2 > -1:
                    current = Cruiser(startingPointX, startingPointY, startingPointX - 2, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 4 and startingPointX - 3> -1:
                    current = Battleship(startingPointX, startingPointY, startingPointX - 3, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 5 and startingPointX - 4 > -1:
                    current = Carrier(startingPointX, startingPointY, startingPointX - 4, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
            if direction == 2:
                if lenght == 1:
                    current = Submarine(startingPointX, startingPointY, startingPointX, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 2 and (startingPointY + 1 < 10 and startingPointY > -1):
                    current = Destroyer(startingPointX, startingPointY+1, startingPointX, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 3 and (startingPointY +2 < 10 and startingPointY > -1):
                    current = Cruiser(startingPointX, startingPointY+2, startingPointX, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 4  and (startingPointY + 3 < 10 and startingPointY > -1):
                    current = Battleship(startingPointX, startingPointY+3, startingPointX, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 5  and (startingPointY + 4 < 10 and startingPointY > -1):
                    current = Carrier(startingPointX, startingPointY+4, startingPointX, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
            if direction == 3:
                if lenght == 1:
                    current = Submarine(startingPointX, startingPointY, startingPointX, startingPointY)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 2 and (startingPointY - 1 < 10 and startingPointY - 1> -1):
                    current = Destroyer(startingPointX, startingPointY, startingPointX, startingPointY -1)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 3 and (startingPointY - 2 < 10 and startingPointY -2> -1):
                    current = Cruiser(startingPointX, startingPointY, startingPointX, startingPointY -2)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 4 and (startingPointY - 3 < 10 and startingPointY-3 > -1):
                    current = Battleship(startingPointX, startingPointY, startingPointX, startingPointY -3)
                    if self.notInFleet(current, fleet) == True:
                        return current
                if lenght == 5 and (startingPointY - 4 < 10 and startingPointY -4> -1):
                    current = Carrier(startingPointX, startingPointY, startingPointX, startingPointY-4)
                    if self.notInFleet(current, fleet) == True:
                        return current
            startingPointX = random.randint(0, 9)
            startingPointY = random.randint(0, 9)



    def generateShips(self):
        fleet = []
        fleet.append(self.generateOne(5, fleet))
        fleet.append(self.generateOne(4, fleet))
        fleet.append(self.generateOne(3, fleet))
        fleet.append(self.generateOne(2, fleet))
        fleet.append(self.generateOne(2, fleet))
        fleet.append(self.generateOne(1, fleet))
        fleet.append(self.generateOne(1, fleet))
        return fleet


    def doMove(self):
        if self._lastResult == 'start' or (self._lastResult == 'miss' and self._shipShot == []):
            result = self.scoutPhase()
            self.addAllShots(result)
            return result

        if self._lastResult == 'sink':
            #checks if it sank a submarine with a random shot
            if self._shipShot == []:
                result = self.scoutPhase()
                self.addAllShots(result)
                return result

            elif self._shipShot != []:
                self.resetShipShot()
                result = self.scoutPhase()
                self.addAllShots(result)
                return result

        if self._lastResult == 'hit':
            result = self.attackPhase()
            self.addAllShots(result)
            self.addShipShot(self._allShots[-1])
            return result

        if self._lastResult == 'miss' and self._shipShot != []:
            self.resetShipShot()
            result = self.scoutPhase()
            self.addAllShots(result)
            return result


