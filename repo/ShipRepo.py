from repo.SubmarineRepo import SubmarineRepo
from repo.BattleshipRepo import BattleshipRepo
from repo.CarrierRepo import CarrierRepo
from repo.CruiserRepo import CruiserRepo
from repo.DestroyerRepo import DestroyerRepo

class ShipRepo():
    def __init__(self):
        """
        All repos untied in one.
        There should be:
        1x Carrier
        1x Battleship
        1x Cruiser
        2x Destroyers
        2x Submarines
        """
        self._battles = BattleshipRepo()
        self._subs = SubmarineRepo()
        self._destroy = DestroyerRepo()
        self._carry = CarrierRepo()
        self._cruiser = CruiserRepo()

    def getFleetSize(self):
        return self._battles.getLen() + self._subs.getLen() + self._destroy.getLen() + self._carry.getLen() + self._cruiser.getLen()

    def addCruiser(self, value):
        self._cruiser.add(value)

    def addCarrier(self, value):
        self._carry.add(value)

    def addBattleship(self, value):
        self._battles.add(value)

    def addSubmarine(self, value):
        self._subs.add(value)

    def addDestroyer(self, value):
        self._destroy.add(value)

    def registerHit(self, row, col):
        """
        IF THERE IS TIME, MOVE THIS FUNCTION IN EACH SHIPREPO...
        checks what kind of ship has been hit and if it should sink
        :param row: row coordonate of board
        :param col: collomn coordonate of board
        :return: nothing. modifies the board should need be
        """
        found = False

        #Checks the battle ships
        checkShips = self._battles.getList()
        i = 0
        if len(checkShips) > 0:
            for ship in checkShips:
                sectorOcupied = ship.getOccupiedCoordonates()
                for sectors in sectorOcupied:
                    if sectors[0] == row:
                        if sectors[1] == col:
                            result = ship.gotHit()
                            found = True
                            if result == -1:
                                self._carry.removeAtPosition(i)
                                print("bat destroyed")
                                return 'sink'
                            break
                i += 1

        #check the carrier (truthfully ne need for for loop)
        i = 0
        checkShips = self._carry.getList()
        if found == False and len(checkShips) > 0:
            for ship in checkShips:
                sectorOcupied = ship.getOccupiedCoordonates()
                for sectors in sectorOcupied:
                    if sectors[0] == row:
                        if sectors[1] == col:
                            result = ship.gotHit()
                            found = True
                            if result == -1:
                                self._carry.removeAtPosition(i)
                                print("car destroyed")
                                return sectorOcupied
                            break
                i += 1

        #checks cruisers
        checkShips = self._cruiser.getList()
        if found == False and len(checkShips) > 0:
            i = 0
            for ship in checkShips:
                sectorOcupied = ship.getOccupiedCoordonates()
                for sectors in sectorOcupied:
                    if sectors[0] == row:
                        if sectors[1] == col:
                            result = ship.gotHit()
                            found = True
                            if result == -1:
                                self._carry.removeAtPosition(i)
                                print("cruiser destroyed")
                                return sectorOcupied
                            break
                i += 1

        #checks destroyer
        i = 0
        checkShips = self._destroy.getList()
        if found == False and len(checkShips) > 0:
            for ship in checkShips:
                sectorOcupied = ship.getOccupiedCoordonates()
                for sectors in sectorOcupied:
                    if sectors[0] == row:
                        if sectors[1] == col:
                            result = ship.gotHit()
                            found = True
                            if result == -1:
                                self._carry.removeAtPosition(i)
                                print("destroyer destroyed")
                                return sectorOcupied
                            break
                i += 1

        #checks submarines
        checkShips = self._subs.getList()
        if found == False and len(checkShips) > 0:
            i = 0
            for ship in checkShips:
                sectorOcupied = ship.getOccupiedCoordonates()
                for sectors in sectorOcupied:
                    if sectors[0] == row:
                        if sectors[1] == col:
                            result = ship.gotHit()
                            found = True
                            if result == -1:
                                self._carry.removeAtPosition(i)
                                print("sub destroyed")
                                return sectorOcupied
                            break
                i += 1
        if found == True:
            return 'hit'
        return 'weird'


