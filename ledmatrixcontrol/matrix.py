""" Character templates """
import character_templates as ct
""" Main class handle display of any string on a matrix of specified size """
class Matrix:
    """ Properties """
    width = 0 # width property
    height = 0 # height property
    numPixels = 0 #total number of pixels
    fillerNegative = "." # representation of 0
    fillerPositive = "o" # representation of 1
    """ Matrix container """
    matrixArr = [] # container for matrix data
    """
        Initiate instance, set property data
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.numPixels = self.width * self.height
        # Initate matrix property with default values
        for i in range(self.height):
            # Vertical
            if (len(self.matrixArr) < self.height):
                self.matrixArr.append([])
            # Horizontal
            for j in range(self.width):
                if (len(self.matrixArr[i]) < self.width):
                    self.matrixArr[i].append(self.fillerNegative)
    """
        Add a character to matrix
        startCoords array format [x, y]
    """
    def addCharToMatrix(self, char, startCoords):
        # Get char template and split it into parts so it can be translated
        splitChar = ct.renderDict[char].strip().split("\n")
        startCoordX = startCoords[0]
        startCoordY = startCoords[1]
        # Iterate through array and add characters to matrix
        for i in range(0, len(splitChar)):
            for j in range(0, len(splitChar[i])):
                # Convert matrix element to positive if coordinates are correct
                if (ct.charAsBool(splitChar[i][j])
                        and (0 < (i + startCoordY) < len(self.matrixArr))
                        and (0 < (j + startCoordX) < len(self.matrixArr[i]))):
                    self.matrixArr[i + startCoordY][j + startCoordX] = self.fillerPositive
    """
        Print string onto matrix
        startCoords array format [x, y]
    """
    def addString(self, string, startCoords):
        charStepX = 4
        startCoordX = startCoords[0]
        startCoordY = startCoords[1]
        for i in range(len(string)):
            self.addCharToMatrix(string[i], [(i * charStepX) + startCoordX, startCoordY])

