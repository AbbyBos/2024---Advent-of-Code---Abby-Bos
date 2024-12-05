source = 'Day 4\Day 4 Test.txt'
puzzel = []
xmascount = int(0)

def importfile (source):        ## Import file in a matrix (list of lists)
    with open(source, "r") as f:   
        lines = f.readlines()
        for row in lines:
            puzzel.append(list(row))
        for row in puzzel:
            try:
                row.pop(row.index('\n'))
            except ValueError:
                pass



def loopthroughmatrix(matrix): ## Loop through all posistions in the matrix.
    count = 0
    found = []  # Keep track of found XMAS starting positions

    for Y, row in enumerate(matrix):            ##Loop by row
        for X, char in enumerate(row):          ##Loop by column
            if char == "X":          ##Only look for xmas on x
                if checkeast(Y, X, found):
                    count += 1
                if checkwest(Y, X, found):
                    count += 1
                if checknorth(Y, X, found):
                    count += 1
                if checksouth(Y, X, found):
                    count += 1
                if checknortheast(Y, X, found):
                    count += 1
                if checknorthwest(Y, X, found):
                    count += 1
                if checksoutheast(Y, X, found):
                    count += 1
                if checksouthwest(Y, X, found):
                    count += 1
    print(count)



def checkeast(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x-1][y] + puzzel[x-2][y] + puzzel[x-3][y] == 'XMAS':
            found.append(((x,y),"east"))  # Add all parts of XMAS to found
            return True
    except IndexError:
        pass
    return False

def checkwest(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x+1][y] + puzzel[x+2][y] + puzzel[x+3][y] == 'XMAS':
            found.append(((x , y), "west"))
            return True
    except IndexError:
        pass
    return False

def checknorth(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x][y-1] + puzzel[x][y-2] + puzzel[x][y-3] == 'XMAS':
            found.append(((x, y), "north"))
            return True
    except IndexError:
        pass
    return False

def checksouth(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x][y+1] + puzzel[x][y+2] + puzzel[x][y+3] == 'XMAS':
            found.append(((x, y ), "south"))
            return True
    except IndexError:
        pass
    return False

def checknortheast(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x-1][y-1] + puzzel[x-2][y-2] + puzzel[x-3][y-3] == 'XMAS':
            found.append(((x, y ), "northeast"))
            return True
    except IndexError:
        pass
    return False

def checknorthwest(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x-1][y+1] + puzzel[x-2][y+2] + puzzel[x-3][y+3] == 'XMAS': 
            found.append(((x , y ), "northwest"))
            return True
    except IndexError:
        pass
    return False

def checksoutheast(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x+1][y-1] + puzzel[x+2][y-2] + puzzel[x+3][y-3] == 'XMAS': 
            found.append(((x , y ), "southeast"))
            return True
    except IndexError:
        pass
    return False

def checksouthwest(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x+1][y+1] + puzzel[x+2][y+2] + puzzel[x+3][y+3] == 'XMAS':
            found.append(((x , y ), "southwest"))
            return True
    except IndexError:
        pass
    return False


def checkxmas(matrix): ## Loop through all posistions in the matrix.
    count = 0

    for Y, row in enumerate(matrix):            ##Loop by row
        for X, char in enumerate(row):          ##Loop by column
            if char == "A":          ##Only look for xmas on A
                try:
                    checksum = matrix[Y-1][X-1] + matrix[Y-1][X+1] + matrix[Y+1][X+1] + matrix[Y+1][X-1]
                    if checksum.count('M') == 2 and checksum.count('S') == 2:
                        if matrix[Y-1][X-1] != matrix[Y+1][X+1]:
                            print(checksum)
                            count += 1
                except IndexError:
                    print("out of bounds")
                    pass
    print(count)
           


importfile(source)
loopthroughmatrix(puzzel)
checkxmas(puzzel)