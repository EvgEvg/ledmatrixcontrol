from renderer_abstract import rendererAbstract

""" Renderer for matrix on console """
class rendererConsole(rendererAbstract):
    """ Show matrix to user (render on screen)"""
    def render(self, matrix):
        for i in range(len(matrix)):
            matrixRow = ''
            for j in range(len(matrix[i])):
                matrixRow += matrix[i][j]
            print(matrixRow)