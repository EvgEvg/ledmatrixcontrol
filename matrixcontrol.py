import time
from ledmatrixcontrol import Matrix
from ledmatrixcontrol import rendererConsole
from ledmatrixcontrol import rendererBtfLighting8x32

ledScreenWidth = 32
ledScreenHeight = 8

renderer = rendererConsole()
rendererLed = rendererBtfLighting8x32()

while(True):
    matrix = Matrix(ledScreenWidth, ledScreenHeight)
    renderer.render(matrix.matrixArr)
    matrix.addString(
        time.strftime("%H:%M:%S", time.localtime()),
        [1, 1]
    )
    renderer.render(matrix.matrixArr)
    rendererLed.render(matrix)
    time.sleep(5)


