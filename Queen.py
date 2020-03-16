'''
    Program Finds a Solution to the n Queens puzzle 
    Uses Hill Climbing Technique 
    
    Created By: Joshua Fairfield 
    Date: 3/16/2020 
'''
import random
import sys
import copy
from pip._vendor.distlib.compat import raw_input

class Search():
    #PrintList stores how the board is solved 
    printList = []
    
    #Search algorithm finds number of queens attacking each other 
    def search(self, board):
        #Input: a multidimensional array board 
        #Output: Number of queens attacking 
        
        #Count stores number of queens attacking, x and y stores the coordinates
        count = 0
        x = []
        y = []
        
        #Finds the coordinates of each queen on the board 
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 9:
                    x.append(i)
                    y.append(j)
        
        #Finds instances of a number, finds if attacking in same row/column 
        for i in range(len(board)):
            if x.count(i) > 1:
                count += x.count(i)
            if y.count(i) > 1:
                count += y.count(i)
        
        #Finds if queens are attacking diagonally 
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if x[i] == x[j]:
                    if y[i] == y[j]:
                        count += 1
                elif x[i] != x[j]:
                    if abs((y[j] - y[i]) / (x[j] - x[i])) == 1:
                        count += 1
        return count    
    
    #Hill moves a queen to the next best location based on hill climbing 
    def hill(self, board):
        #Input: Multidimensional array board 
        #Output: The next board iteration based on the input 
        
        #X and y store coordinates, tempBoard acts as a temp, minboard is the 
        #optimal board, min stores how many queens are attacking
        x = []
        y = [] 
        tempBoard = copy.deepcopy(board)
        minBoard = []
        min = self.search(board)
        
        #If the printList is empty, add the initial board to it
        if self.printList == []:
            self.printList.append(board)
        
        #If min == 0, the board is solved, and the list is printed 
        if min == 0:
            for i in range(len(self.printList)):
                self.printBoard(self.printList[i])
                print('-------')
            print('Done in', len(self.printList), 'moves')
            g = raw_input('Enter a key to exit')
            sys.exit(0)
        
        #Finds the coordinates for each 9
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 9:
                    x.append(i)
                    y.append(j)
        
        #Tests the viability of each queen in each place on the board, 
        #finding the optimal move
        for d in range(len(x)):
            for i in range(len(tempBoard)):
                for j in range(len(tempBoard)):
                    if tempBoard[i][j] == 0:
                        tempBoard[i][j] = 9
                        tempBoard[x[d]][y[d]] = 0 
                        t = self.search(tempBoard)
                        if t < min:
                            minBoard = copy.deepcopy(tempBoard)
                            min = t 
                        tempBoard = copy.deepcopy(board)
        
        #Randomizes the board if no optimal movement found 
        if minBoard == []:
            self.printList.clear()
            return self.randomize(board)
        
        #Adds the next iteration of the board, and returns it 
        self.printList.append(minBoard)
        return minBoard
    
    #Function randomizes the board 
    def randomize(self, board):
        #Input: Multidimensional array boardf 
        #Output: a randomized board 
        
        
        tempBoard = copy.deepcopy(board)
        
        #Ensures the board contains all zeroes 
        for i in range(len(tempBoard)):
            for j in range(len(tempBoard)):
                tempBoard[i][j] = 0
        count = 0
        
        #Randomizes the board
        while count < len(tempBoard):
            queenx = random.randint(0, len(tempBoard) - 1)
            queeny = random.randint(0, len(tempBoard) - 1)
            if tempBoard[queenx][queeny] == 0:
                tempBoard[queenx][queeny] = 9
                count = count + 1
        return tempBoard
    
    #Prints the board 
    def printBoard(self, board):
        #Input: multidimensional array board 
        #Output: printing the board 
        
        for i in range(len(board)):
            print(board[i])

''' -----------RUNNER---------- '''
#Initializes the board based on the number inputed, width >= 8
width = 0
print('Enter a number for the number of queens')
width = int(raw_input())
board = [[0 for i in range(width)] for j in range(width)]

#Runs the search algorithm to solve the puzzle 
search = Search()
board = search.randomize(board)
while(True):
    board = search.hill(board)