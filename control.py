import time
import characterTemplates

""" Matrix fillers """
fillerNegative = "."
fillerPositive = "o"

""" Create a matrix and initialize it with 0s
"""
matrixHeight = 8
matrixWidth = 32
numPixels = matrixHeight * matrixWidth

""" Initialize a matrix with 0s
"""
def freshMatrix(matrix, matrixWidth, matrixHeight):
    for i in range(matrixHeight):
        if (len(matrix) < matrixHeight):
            matrix.append([])
        matrix[i] = []
        for j in range(matrixWidth):
            if (len(matrix[i]) < matrixWidth):
                matrix[i].append(fillerNegative)
            matrix[i][j] = fillerNegative
    return matrix

""" Convert template character to matrix character
"""
def convertTemplateToMatrix(templateChar):
    if templateChar == "_":
        return False
    return True

""" Show matrix to user (render on screen)
"""
def renderMatrixOnScreen(matrix):
    for i in range(matrixHeight):
        matrixRow = ''
        for j in range(matrixWidth):
            matrixRow += matrix[i][j]
        print(matrixRow)


""" Render letter into a matrix
    render is ontop of whatever in the matrix
"""
def addCharToMatrix(char, matrix, startCoord):
    splitChar = char.strip().split("\n")
    startCoordX = startCoord[0]
    startCoordY = startCoord[1]
    if (startCoordY + len(splitChar)) > len(matrix):
        raise IndexError("Character won't fit on the matrix!")
    for i in range(0, len(splitChar)):
        for j in range(0, len(splitChar[i])):
            if convertTemplateToMatrix(splitChar[i][j]):
                matrix[i + startCoordY][j + startCoordX] = fillerPositive

""" Convert matrix to line """
def translateMatrixToLine(matrix):
    # Initiate empty array
    pixelLine = [None] * numPixels
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if ((j + 1) % 2) > 0:
                pos = len(matrix) * j + i
#                 print("{} = {} * {} + {}".format(pos, len(matrix), j, i))
            elif ((j + 1) % 2) == 0:
                pos = len(matrix) * j + abs(i - (len(matrix) - 1))
#                 print("{} = {} * {} + abs({} - ({} - 1))".format(pos, len(matrix), i, j, len(matrix)))
#             print (i,j,pos)
            pixelLine[pos] = fillerPositive if matrix[i][j] == fillerPositive else fillerNegative
    return pixelLine

"""                """
""" Execution flow """
"""                """

renderDict = {
    '0': characterTemplates.digitZero,
    '1': characterTemplates.digitOne,
    '2': characterTemplates.digitTwo,
    '3': characterTemplates.digitThree,
    '4': characterTemplates.digitFour,
    '5': characterTemplates.digitFive,
    '6': characterTemplates.digitSix,
    '7': characterTemplates.digitSeven,
    '8': characterTemplates.digitEight,
    '9': characterTemplates.digitNine,
    ':': characterTemplates.divider
}

for i in range(1):
    freshMatrix = freshMatrix([], matrixWidth, matrixHeight)
    strTime = time.strftime("%H:%M:%S", time.localtime())
    charStepX = 4
    for j in range(len(strTime)):
        addCharToMatrix(renderDict[strTime[j]], freshMatrix, [j * charStepX, 0])
    renderMatrixOnScreen(freshMatrix)
    print(translateMatrixToLine(freshMatrix))
    time.sleep(1)
