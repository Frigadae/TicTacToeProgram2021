"""
name: Daniel Wang
UPI: wany889
date: 24/11/20
"""
from gameModules import gameGrid
from gameModules import player

def main():
    while True:
        print("Python Tic Tac Toe 2021 version \n")
        player1 = ""
        player2 = ""
        getOption = gameMode()
        if getOption == 0:
            print("\nThank you for playing \n")
            break
        else:
            game(getOption)

def gameMode():
    modeNum = 0
    optionList = ["0: Quit", "1: Player vs AI", "2: Player vs Player"]
    while modeNum == 0:
        print("Game modes: ")
        for i in optionList:
            print(">" + i)
        getInput = input("Select your game mode: ")
        if getInput.isnumeric() == True:
            if int(getInput) == 0:
                return modeNum
            elif int(getInput) == 1:
                modeNum = 1
            elif int(getInput) == 2:
                modeNum = 2
            else:
                print("\nInvalid option, please reenter\n")
        else:
            print("\nInvalid option, please reenter\n")
    return modeNum

def game(modeNumber):
    print("Game Mode: " + str(modeNumber))
    grid = gameGrid()
    if modeNumber == 1:
        player1 = player(getName(), False)
        player2 = player("Computer", True)
    elif modeNumber == 2:
        player1 = player(getName(1), False)
        player2 = player(getName(2), False)
    while True:
        grid.printGrid()
        gameOver = grid.putMarker(player1.name, player1.isAI)
        if declareWinner(gameOver, player1, grid):
            grid.printGrid()
            break
        grid.printGrid()
        gameOver = grid.putMarker(player2.name, player2.isAI)
        if declareWinner(gameOver, player2, grid):
            grid.printGrid()
            break

def declareWinner(winCode, player, grid):
    if winCode == 1:
        print("\nRound Draw! Nobody wins!")
        print("That round took " + str(grid.turns) + " turns!\n")
        return True
    elif winCode == 2:
        print("\n" + player.name + " is the winner!")
        player.addScore()
        print("That round took " + str(grid.turns) + " turns!\n")
        return True
    else:
        return False

def getName(number = ""):
    while True:
        name = input("Enter your name for Player " + str(number) + ": ")
        print("Are you sure this is the name you entered?\n Name: " + name)
        confirm = input("Y/N: ")
        if confirm == "Y" or confirm == "y":
            return name
        elif confirm == "N" or confirm == "n":
            pass
        else:
            print("Invalid option, please reenter\n")
        
main()
