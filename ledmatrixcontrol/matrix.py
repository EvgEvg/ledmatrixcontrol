""" Character templates """
import character_templates as ct
import time

""" Main class handle display of any string on a matrix of specified size """
class Matrix:
    """ Properties """
    fillerNegative = "." # representation of 0
    fillerPositive = "o" # representation of 1
    fillerSeconds = "s" # representation for "seconds" filler
    """
        Initiate instance, set property data
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.numPixels = self.width * self.height
        # Initate matrix property with default values
        self.matrixArr = []
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
        Calculate step size for a character
        @return int
    """
    def calculateStep(self, char):
        splitChar = ct.renderDict[char].strip().split("\n")
        lineLengths = []
        for i in range(0, len(splitChar)):
            lineLengths.append(len(splitChar[i]))
        return max(lineLengths)
    """
        Print string onto matrix
        startCoords array format [x, y]
    """
    def addString(self, string, startCoords):
        startCoordX = startCoords[0]
        startCoordY = startCoords[1]
        charStepX = 0
        for i in range(len(string)):
            self.addCharToMatrix(string[i], [charStepX + startCoordX, startCoordY])
            charStepX += self.calculateStep(string[i])
    """
        Fill matrix with "seconds" progress bar
    """
    def fillSecondsProgress(self):
        # Calculate column
        secondsOnMinute = int(time.localtime().tm_sec)
        fillToColumn = secondsOnMinute / 2
        fillToColumn = self.width if (fillToColumn > self.width) else fillToColumn
        # Fill matrix
        for i in range(0, 1):
            for j in range(0, fillToColumn):
                self.matrixArr[i][j] = self.fillerSeconds
