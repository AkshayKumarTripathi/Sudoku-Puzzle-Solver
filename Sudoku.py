#we are going to implement a sudoku puzzle solver using the back tracking algorithm


def start():
#This function will have the baord and we will see if any solution is possible or not
    
    sudoku=[[0,2,6,0,0,0,8,1,0],[3,0,0,7,0,8,0,0,6],[4,0,0,0,5,0,0,0,7],[0,5,0,1,0,7,0,9,0],[0,0,3,9,0,5,1,0,0],[0,4,0,3,0,2,0,5,0],[1,0,0,0,3,0,0,0,2],[5,0,0,2,0,4,0,0,9],[0,3,8,0,0,0,4,6,0]]
    printoi(sudoku)

    #This line is asking if the user wants to enter his own puzzle or wants to see the solution of the sample puzzle
    automatic=int(input("Do you want to enter your own puzzle to find the solution or want to use the above sample puzzle?  Enter 1 for yes and 0 for no   "))
    
    #using List Comprehension to build the sudoku puzzle
    if automatic:
        sudoku=[list(map(int,input("Enter The 9 Numbers Row-wise with spaces and for the missing numbers enter 0 (ROW {}) ".format(x+1)).split())) for x in range(9)]
    
    #if not making the puzzle use the default puzzle 

#     sudoku=[[0,2,6,0,0,0,8,1,0],[3,0,0,7,0,8,0,0,6],[4,0,0,0,5,0,0,0,7],[0,5,0,1,0,7,0,9,0],[0,0,3,9,0,5,1,0,0],[0,4,0,3,0,2,0,5,0],[1,0,0,0,3,0,0,0,2],[5,0,0,2,0,4,0,0,9],[0,3,8,0,0,0,4,6,0]]
    
    #checking if the solution really exists by calling the function
    if possible(sudoku):
        printoi(sudoku)
    else:
        print("NO SOLUTION IS POSSIBLE!!!")



#This Function prints the solution of the board in presentable way
def printoi(sudoku):
    for row_print in range(9):
        print(" ")
        if row_print%3==0 and row_print!=0:
            print("------|-------|------")
        for column_print in range(9):

            if column_print%3==0 and column_print!=0:
                print("|",end=" ")

            print(sudoku[row_print][column_print],end=" ")

    print(" ")
    print(" ") #This print is here so that while printing the sample puzzle the next question does not come in the same line

#THE MAIN FUNCTION WHERE RECURSION HAPPENS!!!
def possible(sudoku):
    """
        I created a function which tracks the empty points so that we can back-track to the initial position if the solution is not available is we have used a for loop instead of static points 
        every time the function back tracks instead of using the initial point the for loop will give another new empty point thats why we used an external function.
    """

    #Tuple unpacking to get the set of points
    x,y=findempty(sudoku)
    
    #base case 
    if x==8 and y==8:
        for final in range(1,10):
            if isvalid(sudoku,x,y,final):
                sudoku[x][y]=final
        return True

    #recursive case
    else:
        
        for number in range(1,10):
            
            if isvalid(sudoku,x,y,number):
                sudoku[x][y]=number
                
                if possible(sudoku):
                    return True
                
                sudoku[x][y]=0                                     #BACKTRACKING
        
        return False                                               #returning false so we can change the value

def isvalid(sudoku,x,y,number):                                    # THIS FUNCTION IF THE NUMBER IS PRESENT IN THE SAME ROW OR COLUMN OR INTHJE SAME 9X9 SQUARE WHERE THE NUMBER IS PRESENT
    for row in range(9):
        if sudoku[x][row]==number:
            return False
    
    for column in range(9):
        if sudoku[column][y]==number:
            return False
                                                                                                        
    newx=x//3
    newy=y//3                                                                                           #dividing the whole puzzle into 9 gaint squares
    for nex in range(newx*3,newx*3+3):
        for ney in range(newy*3,newy*3+3):
            if sudoku[nex][ney]==number and (nex,ney)!=(x,y):
                return False

    return True

def findempty(sudoku):                              #The function which checks if the values are empty or not
    for x in range(9):
        for y in range(9):
            if sudoku[x][y]==0:
                return (x,y)

start()  
