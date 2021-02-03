"""
name: Daniel Wang
UPI: wany889
date: 24/11/20
"""
import random
import re

class gameGrid:
    def __init__(self):
        self.grid = [["1,1", "1,2", "1,3"],
                     ["2,1", "2,2", "2,3"],
                     ["3,1", "3,2", "3,3"]]
        self.turns = 0

    def printGrid(self):
        print()
        for row in self.grid:
            for cell in row:
                print("[" + cell + "]", end = "")
            print()
        print()

    def reset(self):
        self.grid = [["1,1", "1,2", "1,3"],
                     ["2,1", "2,2", "2,3"],
                     ["3,1", "3,2", "3,3"]]

    def isFull(self):
        objectsFound = 0
        for row in self.grid:
            for cell in row:
                found = re.search(".,.", cell)
                if found != None:
                    objectsFound += 1
        if objectsFound == 0:
            return True
        else:
            return False

    def putMarker(self, player, checkAI):
        if checkAI == True:
            print("Computer makes their move...")  
        while True:
            if self.isFull() == True:
                return 1
            if checkAI == False:
                print(player + ", place your marker on a coordinate.")
                row = input("Row number: ")
                cell = input("Col number: ")
            else:
                row = str(random.randint(1, 3))
                cell = str(random.randint(1, 3))
            if row.isnumeric() == True and cell.isnumeric() == True:
                row = int(row)
                cell = int(cell)
                if 1 <= row <= 3 and 1 <= cell <= 3:
                    if re.search(".,.", self.grid[row - 1][cell - 1]) != None:
                        if self.turns % 2 == 0:
                            self.grid[row - 1][cell - 1] = " X "
                            self.turns += 1
                            if self.checkWin(" X ") == True:
                                return 2
                            return 0
                        else:
                            self.grid[row - 1][cell - 1] = " O "
                            self.turns += 1
                            if self.checkWin(" O ") == True:
                                return 2
                            return 0
                    else:
                        if checkAI == False:
                            print("Cell already occupied! Pick another cell!")
                else:
                    print("Coordinate out of range!")
            else:
                print("Not a coordinate!")

    def checkWin(self, marker):
        win = False
        gridCount = len(self.grid)
        for row in self.grid:
            if all(cell == marker for cell in row):
                win = True
        for i in range(gridCount):
            if self.grid[0][i] == marker and self.grid[1][i] == marker and self.grid[2][i] == marker:
                win = True
        if self.grid[0][0] == marker and self.grid[1][1] == marker and self.grid[2][2] == marker:
                win = True
        if self.grid[0][2] == marker and self.grid[1][1] == marker and self.grid[2][1] == marker:
                win = True
        return win

class player:
    def __init__(self, name, isComputer):
        self.name = name
        self.isAI = isComputer
        self.score = 0

    def addScore(self):
        self.score += 1

    def isAI(self):
        return self.isAI
