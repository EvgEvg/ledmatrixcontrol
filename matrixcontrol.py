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
    matrix.addString(
        time.strftime("%H%M", time.localtime()),
        [0, 0]
    )
    renderer.render(matrix)
    rendererLed.render(matrix)
    time.sleep(1)
#
#     phrase = 'Welcome to the New 2018th year!!! Let\'s turn up!'
#     for i in range(0, (len(phrase) * 8)): # 8 is constant space per character not sure how to define it
#         matrix = Matrix(ledScreenWidth, ledScreenHeight)
#         matrix.addString(
#             phrase,
#             [i * -1, 0]
#         )
#         renderer.render(matrix)
#         rendererLed.render(matrix)
#         time.sleep(0.05)
#     for i in range(0, 30):
#         matrix = Matrix(ledScreenWidth, ledScreenHeight)
#         matrix.addString(
#             time.strftime("%H%M", time.localtime()),
#             [0, 0]
#         )
#         renderer.render(matrix)
#         rendererLed.render(matrix)
#         time.sleep(1)
