import sys
import math

def generate(difficulty):
        dif = validateDifficulty(difficulty)
        if(not dif):
                print("Invalid Difficulty")
        else:
                print(dif)

def update(grid):
        for i in range(9):
                for j in range(9):
                        if (grid[i][j].value == "0"):
                                for m in range(9):
                                        for n in range(9):
                                                if(grid[i][j].row == grid[m][n].row or grid[i][j].column == grid[m][n].column or grid[i][j].quadrant == grid[m][n].quadrant):
                                                        if(grid[m][n].value in grid[i][j].pot):
                                                                grid[i][j].pot.remove(grid[m][n].value)                
        # Set values of pot and empty if one value in pot
        for i in range(9):
                for j in range(9):
                        if (grid[i][j].value == "0" and len(grid[i][j].pot)==1):
                                grid[i][j].value = grid[i][j].pot[0]
                                update(grid)

def printGrid(grid):
        print ()              
        for i in range(0,9):
                for j in range(0,9):
                        print(grid[i][j].value + " ", end = "")
                print()

def isComplete(grid):
        for i in range(9):
                for j in range(9):
                        if(grid[i][j].value == "0"):
                                return 0
        return 1

def simplify(grid):
        # Go through and update pots
                update(grid)
               
                # Check rows for unique pot number
                for i in range(9):
                        temp = [0]*9
                        for j in range(9):
                                if (grid [i][j].value == "0"):
                                        for m in grid[i][j].pot:
                                                temp[int(m)-1]+=1
                        for m in range(9):
                                if(temp[m] == 1):
                                        for j in range(9):
                                                if(str(m+1) in grid[i][j].pot):
                                                        grid[i][j].value = str(m+1)
                                                        grid[i][j].pot = [str(m+1)]
                                                        update(grid)
                
               

                # Check column for unique pot number
                for j in range(9):
                        temp = [0]*9
                        for i in range(9):
                                if (grid [i][j].value == "0"):
                                        for m in grid[i][j].pot:
                                                temp[int(m)-1]+=1
                        for m in range(9):
                                if(temp[m]==1):
                                        for i in range(9):
                                                if(str(m+1) in grid[i][j].pot):
                                                        grid[i][j].value = str(m+1)
                                                        grid[i][j].pot = [str(m+1)]
                                                        update(grid)
                
        
                
                # Check quadrant for single pot number
                '''for q in range(9):
                        temp = [0]*9
                        for i in range(3*int((q/3)), 3*int((q/3))+2):
                                for j in range((q%3)*3, (q%3)*3+2):
                                        if (grid [i][j].value == "0"):
                                                for m in grid[i][j].pot:
                                                        temp[int(m)-1]+=1
                        print(temp)
                        for m in range(9):
                                if(temp[m]==1):
                                        for i in range(3*int((q/3)), 3*int((q/3))+2):
                                                for j in range((q%3)*3, (q%3)*3+2):
                                                        if(str(m+1) in grid[i][j].pot):
                                                                grid[i][j].value = str(m+1)
                                                                grid[i][j].pot = [str(m+1)]
                                                                update(grid)

                for q in range(9):
                        temp = [0]*9
                        for i in range(9):
                                for j in range(9):
                                        if(grid[i][j].quadrant == q and grid[i][j].value == "0"):
                                                for m in grid[i][j].pot:
                                                        temp[int(m)-1]+=1
                        for m in range(9):
                                if(temp[m]==1):
                                        for i in range(9):
                                                for j in range(9):
                                                        if(grid[i][j].quadrant == q):
                                                                if(str(m+1) in grid[i][j].pot):
                                                                        grid[i][j].value = str(m+1)
                                                                        grid[i][j].pot = [str(m+1)]
                                                                        update(grid)'''
                return grid
                                                        
def solve(puzzle):
        if(not validatePuzzle(puzzle)):
                print("Invalid Puzzle")
        else:
                #print(puzzle)
                
                grid = [0]*9
                for i in range(0,9):
                        grid[i] = [0]*9
                        for j in range(0,9):
                                grid[i][j] = Cell(i, j, puzzle[(i*9)+j])
                                print(grid[i][j].value + " ", end = "")
                        print()

                # While loop
                '''while(not isComplete(grid)):
                        grid = simplify(grid)
                        printGrid(grid)'''
                for i in range(0,4):
                        grid = simplify(grid)
                        printGrid(grid)'''
                


                
def validateDifficulty(dif):
        if(dif == "easy"):
                return 1
        elif(dif == "medium"):
                return 2
        elif(dif == "hard"):
                return 3
        else:
                return 0

def validatePuzzle(puzzle):
        if len(puzzle) == 81:
                return True
        else:
                return False
        
def clear():
        print("clear")

class Cell(object):
        row = 0
        column = 0
        value = 0
        quadrant = 0
        pot = []
        def __init__(self, i, j, k):
               self.row = i
               self.column = j
               self.value = k
               if(math.floor(i/3)==0):
                       self.quadrant = math.ceil((j+0.1)/3)
               elif(math.floor(i/3)==1):
                       self.quadrant = 3+math.ceil((j+0.1)/3)                   
               else:
                       self.quadrant = 6+math.ceil((j+0.1)/3)
               self.pot = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
               if(k != "0"):
                       self.pot = [k]
                
                
# 2 inputs:
# 1st is gen or solve
# 2nd is either difficulty or sudoku grid respectively
for line in sys.stdin: 
        query = line.split() 
        if len(query) == 2: 
                if query[0] == "gen":
                        generate(query[1])
                elif(query[0] == "solve"):
                        solve(query[1])
                else:
                        print("Invalid request")
        else:
                print("Too few arguments")
        clear()

        
