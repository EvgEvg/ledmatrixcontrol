from ledmatrixcontrol import Matrix
from ledmatrixcontrol import rendererConsole
from ledmatrixcontrol import rendererBtfLighting8x32

matrix = Matrix(32, 8)
renderer = rendererConsole()
rendererLed = rendererBtfLighting8x32()

matrix.addString('11:11:13', [1, 1]);
renderer.render(matrix.matrixArr)
translatedMatrix = rendererLed.translateMatrixToLine(matrix)
print(translatedMatrix)
