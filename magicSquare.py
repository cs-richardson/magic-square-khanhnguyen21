#Magic Square Checker
#BY Khanh Nguyen

def fillSquare(n, sqArr):
    '''
    This procedure prompts the user for n^2 inputs to populate a
    2D square array which has alreay been declared
    precondition:  sqArr has been declared with a size of nxn
    '''

    #note: I could have used len(sqArr) instead of passing n in as a parameter
    # but I thought it would be easier for you to understand if it was passed...
    for r in range(n):
        print("----ROW " + str(r + 1) + "----")
        for c in range(n):
            sqArr[r][c] = int(input("Enter value: "))
    

def printSquare(n, sqArr):
    '''
    This procedure "pretty" prints a 2D square array of size n
    '''
    for r in range(n):
        for c in range(n):
            print(sqArr[r][c], end="\t")
        print("\n")
    
def checkRow(n, sqArr, mNum):
    '''
    This procedure will return true if every row of sqArr has a sum of mNum
    It's left for you to do.
    '''
    for r in range (n):
        sum = 0
        for c in range (n):
            sum = sum + sqArr[r][c]
        if sum != mNum:
            return False
    return True

def checkCol(n, sqArr, mNum):
#Compare the sum of each column to the mNum
    for r in range (n):
        sum = 0
        for c in range (n):
            sum = sum + sqArr[c][r]
        if sum != mNum:
            return False
    return True
def checkDiag1(n, sqArr, mNum):
#Compare the sum of the main diagonal to the mNum
    sum = 0
    for r in range (n):
            sum = sum + sqArr[r][r]
    if sum != mNum:
        return False
    return True

def checkDiag2(n, sqArr, mNum):
#Compare the sum of the the other diagonal to the mNum
    sum = 0
    for r in range (n):
            sum = sum + sqArr[n - 1][n - r - 1]
    if sum != mNum:
        return False
    return True

def checkUnique(n, sqArr):
#Check for a number's uniqueness
    numSeen = []
    for r in range (n):
        for c in range (n):
            if sqArr[r][c] in numSeen or sqArr[r][c] > n**2:
                return False
            numSeen.append(sqArr[r][c])
    return True

def checkSquare(size, square):
    '''
    Returns True if inputed square is magic, and False if not.
    '''
    magicNum = size * ((size*size) + 1)/2 # You will need to calculate the magic number here 
    if(checkRow(size, square, magicNum) and  \
       checkCol(size, square, magicNum) and  \
       checkDiag1(size, square, magicNum) and  \
       checkDiag2(size, square, magicNum) and   \
       checkUnique(size, square)):
        return True
    else:
       return False



# ---MAIN---
s = int(input("Enter square side length:  "))
sq = [[0 for x in range(s)] for y in range(s)]
fillSquare(s, sq)

'''
if you get tired of typing in the square multiple times,
for testing purposes, you may want to comment out the 3 lines above and
uncomment the 2 lines below.  It will make your testing life *much* easier :)
'''
#s = 3
#sq = [[2,7,6], [9,5,1], [4,3,8]]

printSquare(s, sq)
print(checkSquare(s, sq))
   

