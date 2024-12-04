source = 'Day 4\Day 4 Prod.txt'
puzzel = []
xmascount = int(0)

def importfile (source):        ## Import file in a matrix (list of lists)
    with open(source, "r") as f:   
        lines = f.readlines()
        for row in lines:
            puzzel.append(list(row))

def loopthroughmatrix(matrix): ## Loop through all posistions in the matrix.
    count = 0
    found = []  # Keep track of found XMAS starting positions

    for i, row in enumerate(matrix):            ##Loop by row
        for j, char in enumerate(row):          ##Loop by column
            if char == "X":          ##Only look for xmas on x
                if checkeast(i, j, found):
                    count += 1
                if checkwest(i, j, found):
                    count += 1
                if checknorth(i, j, found):
                    count += 1
                if checksouth(i, j, found):
                    count += 1
                if checknortheast(i, j, found):
                    count += 1
                if checknorthwest(i, j, found):
                    count += 1
                if checksoutheast(i, j, found):
                    count += 1
                if checksouthwest(i, j, found):
                    count += 1
    print(found)
    print(count)


def checkeast(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x-1][y] + puzzel[x-2][y] + puzzel[x-3][y] == 'XMAS':
            found.append((x,y))  # Add all parts of XMAS to found
            return True
    except IndexError:
        pass
    return False

def checkwest(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x+1][y] + puzzel[x+2][y] + puzzel[x+3][y] == 'XMAS':
            found.append((x , y))
            return True
    except IndexError:
        pass
    return False

def checknorth(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x][y-1] + puzzel[x][y-2] + puzzel[x][y-3] == 'XMAS':
            found.append((x, y))
            return True
    except IndexError:
        pass
    return False

def checksouth(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x][y+1] + puzzel[x][y+2] + puzzel[x][y+3] == 'XMAS':
            found.append((x, y ))
            return True
    except IndexError:
        pass
    return False

def checknortheast(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x-1][y-1] + puzzel[x-2][y-2] + puzzel[x-3][y-3] == 'XMAS':
            found.append((x, y ))
            return True
    except IndexError:
        pass
    return False

def checknorthwest(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x-1][y+1] + puzzel[x-2][y+2] + puzzel[x-3][y+3] == 'XMAS':  #Corrected indices here
            found.append((x , y ))
            return True
    except IndexError:
        pass
    return False

def checksoutheast(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x+1][y-1] + puzzel[x+2][y-2] + puzzel[x+3][y-3] == 'XMAS':  # Corrected indices
            found.append((x , y ))
            return True
    except IndexError:
        pass
    return False

def checksouthwest(x, y, found):
    try:
        if puzzel[x][y] + puzzel[x+1][y+1] + puzzel[x+2][y+2] + puzzel[x+3][y+3] == 'XMAS':
            found.append((x , y ))
            return True
    except IndexError:
        pass
    return False


importfile(source)
loopthroughmatrix(puzzel)