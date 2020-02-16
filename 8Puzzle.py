# CS4242
# Joshua Fairfield 
# 000-83-1638
# Assignment 1
# 2/12/2020

import copy 
import random
from pip._vendor.distlib.compat import raw_input

class ASearch: 
    #Initializing the lists that will be used to store puzzles 
    openList = []
    closedList = []
    
    #Initializes the puzzle by adding the first array to the list 
    def __init__(self, puzzle):
        if (len(self.openList) >= 2):
            self.puzzle = None 
            self.openList.clear()
        self.puzzle = puzzle 
        self.openList.append(puzzle) 
    
    #Prints the puzzle 
    def printPuzzle(self, puzzle):
        for i in range(3):
            for j in range(3):
                print(puzzle[i][j], end = ' ')
            print('')
        print('')
    
    #Returns true of false whether or not the given tiles are within the 8 puzzle
    def inBounds(self, x, y):
        if (x >= 0 and x <= 2 and y >= 0 and y <= 2):
            return True 
        return False
    
    def move(self):
        #Moves the blank tile until puzzle is solved
        while True: 
            min = self.getHeuristic(self.openList[0])
            index = 0
            #Locates the minimum heuristic value 
            for i in range(len(self.openList)):
                if self.getHeuristic(self.openList[i]) < min:
                    min = self.getHeuristic(self.openList[i])
                    index = i
                
            self.generateChildren(self.openList[index])
            self.closedList.append(self.openList[index])
            if self.compareGoal(self.closedList[len(self.closedList)-1]) == 0:
                break
            self.openList.pop(index)
        
        #Prints Result 
        #for i in range(len(self.closedList)):
            #self.printPuzzle(self.closedList[i])
        self.printFinal(self.closedList)
        
    #returns true or false if the puzzle is in the closed list 
    def find(self, puzzle):
        for i in range(len(self.closedList)):
            if (puzzle == self.closedList[i]):
                return True
        return False 
        
    #generates children for the parent 
    def generateChildren(self, puzzle):
        #Creating the blank x and y tile positions 
        x = None 
        y = None 
        
        #finding the x and y positions of the blank tile
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == 0:
                    x = i 
                    y = j
                    break     
        
        #Copying the array
        temp = copy.deepcopy(puzzle)
        
        #Move Down
        if self.inBounds(x - 1, y):
            num = temp[x][y]
            temp[x][y] = temp[x-1][y]
            temp[x-1][y] = num
            #adding another to the openList, ensuring it is not on the closed list
            if (self.find(temp) == False):
                self.openList.append(temp)
            temp = copy.deepcopy(puzzle)
            
        #Move Up 
        if self.inBounds(x + 1, y):
            num = temp[x][y]
            temp[x][y] = temp[x+1][y]
            temp[x+1][y] = num
            #adding another to the openList, ensuring it is not on the closed list
            if (self.find(temp) == False):
                self.openList.append(temp)
            temp = copy.deepcopy(puzzle)
            
        #Move to the Left 
        if self.inBounds(x, y - 1):
            num = temp[x][y]
            temp[x][y] = temp[x][y-1]
            temp[x][y-1] = num
            #adding another to the openList, ensuring it is not on the closed list
            if (self.find(temp) == False):
                self.openList.append(temp)
            temp = copy.deepcopy(puzzle)
            
        #Move to the Right
        if self.inBounds(x, y + 1):
            num = temp[x][y]
            temp[x][y] = temp[x][y+1]
            temp[x][y+1] = num
            #adding another to the openList, ensuring it is not on the closed list
            if (self.find(temp) == False):
                self.openList.append(temp)
            temp = copy.deepcopy(puzzle)
        
    #Returns the heuristic value
    def getHeuristic(self, puzzle):
        sum = 0
        for i in range(3):
            for j in range(3):
                sum += self.ManhattanDistance(i, j)
        sum += self.compareGoal(puzzle)
        return sum
    
    #Finds the number of mismatched tiles, used for the heuristic value, and to determine if the puzzle is solved
    def compareGoal(self, puzzle):
        sum = 0
        goal = [1,2,3], [8, 0, 4], [7,6,5]
        for i in range(3):
            for j in range(3):
                if (goal[i][j] != puzzle[i][j] and goal[i][j] != 0):
                    sum += 1
        return sum 
    
    #The first variable in the heuristic value
    def ManhattanDistance(self, x, y):
        num = self.puzzle[x][y]
        if (num == 1):
            return abs(x - 0) + abs(y - 0)
        elif (num == 2):
            return abs(x - 0) + abs(y - 1)
        elif (num == 3):
            return abs(x - 0) + abs(y - 2)
        elif (num == 8):
            return abs(x - 1) + abs(y - 0)
        elif (num == 0):
            return 0
        elif (num == 4):
            return abs(x - 1) + abs(y - 2)
        elif (num == 7):
            return abs(x - 2) + abs(y - 0)
        elif (num == 6):
            return abs(x - 2) + abs(y - 1)
        elif (num == 5):
            return abs(x - 2) + abs(y - 2)
        else:
            return 
    
    #Compares 2 puzzles, used for print final, determines the number of difference tiles
    def comparePuzzles(self, puzzle, opuzzle):
        differentTiles = 0
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] != opuzzle[i][j]:
                    differentTiles += 1
        return differentTiles
    
    #Prints the final path order, removing any moves that were not made to achieve the result 
    def printFinal(self, puzzle):
        path = []
        path.append(puzzle[len(puzzle)-1])
        index = 0
        x = len(puzzle)-2
        #Goes from the end result up, determining which moves were possible, to find path 
        while x != 0:
            if self.comparePuzzles(puzzle[x] , path[index]) == 2:
                path.append(puzzle[x])
                index += 1
            x-=1
        
        #Prints the path for solving the puzzle 
        y = len(path)-1
        while y != -1:
            self.printPuzzle(path[y])
            y -= 1
        
#Runner
goal = [1,2,3], [8,0,4], [7,6,5]

while True: 
    puzzle = copy.deepcopy(goal)
    solver = ASearch(puzzle)
    
    #Randomizes the puzzle
    while solver.compareGoal(puzzle) < 5:
        for i in range(3):
            r1 = random.randint(0,2)
            r2 = random.randint(0,2)
            num = puzzle[i][r1]
            puzzle[i][r1] = puzzle[r1][r2]
            puzzle[r1][r2] = num 

    temp = []
    for i in range(3):
        for j in range(3):
            if (puzzle[i][j] != 0):
                temp.append(puzzle[i][j])
    
    #Determines the solvability of the puzzle
    invert = 0
    for i in range(len(temp) - 1):
        for j in range(i, len(temp)):
            if temp[i] > temp[j]:
                invert += 1
    if (invert % 2 == 1):
        print(puzzle, "Solvable")
        print('Solving.....')
        solver.move()
        print('Done!')
        break
    else:
        print(puzzle, "Unsolvable")

g = raw_input('Press any key to end...')