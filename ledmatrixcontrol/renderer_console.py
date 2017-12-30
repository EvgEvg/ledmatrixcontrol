from renderer_abstract import rendererAbstract

""" Renderer for matrix on console """
class rendererConsole(rendererAbstract):
    """ Show matrix to user (render on screen)"""
    def render(self, matrix):
        for i in range(len(matrix.matrixArr)):
            matrixRow = ''
            for j in range(len(matrix.matrixArr[i])):
                matrixRow += matrix.matrixArr[i][j]
            print(matrixRow)