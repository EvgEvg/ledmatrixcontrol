from renderer_abstract import rendererAbstract

""" Renderer for matrix on BTF Lighting 8x32 """
""" https://www.amazon.com/gp/product/B01DC0IPVU/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1 """
class rendererBtfLighting8x32(rendererAbstract):
    """ Main function to render things on screen """
    def render():
        pass
    """ Convert matrix to line """
    def translateMatrixToLine(self, matrix):
        # Initiate empty array
        pixelLine = [None] * matrix.numPixels
        for i in range(0, len(matrix.matrixArr)):
            for j in range(0, len(matrix.matrixArr[i])):
                if ((j + 1) % 2) > 0:
                    pos = len(matrix.matrixArr) * j + abs(i - (len(matrix.matrixArr) - 1))
                elif ((j + 1) % 2) == 0:
                    pos = len(matrix.matrixArr) * j + i
                pos = matrix.numPixels - pos - 1
                pixelLine[pos] = matrix.fillerPositive if matrix.matrixArr[i][j] == matrix.fillerPositive else matrix.fillerNegative
        return pixelLine
