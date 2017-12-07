from renderer_abstract import rendererAbstract
from neopixel import *

""" LED strip configuration """
numPixels      = 256                   # 32 * 8
LED_PIN        = 18                    # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000                # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5                     # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 4                     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False                 # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0                     # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

""" Renderer for matrix on BTF Lighting 8x32 """
""" https://www.amazon.com/gp/product/B01DC0IPVU/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1 """
class rendererBtfLighting8x32(rendererAbstract):
    """ Colors for positive and negative """
    colorFillerPositive = Color(10, 10, 100)
    colorFillerNegative = Color(1, 1, 1)
    """ Initialize """
    def __init__(self):
        self.strip = Adafruit_NeoPixel(numPixels, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self.strip.begin()
    """ Main function to render things on screen """
    def render(self, matrix):
        # Show string on LED screen
        translatedMatrixArr = self.translateMatrixToLine(matrix)
        for i in range(len(translatedMatrixArr)):
            color = self.colorFillerPositive if translatedMatrixArr[i] == matrix.fillerPositive else self.colorFillerNegative
            self.strip.setPixelColor(i, color)
        self.strip.show()
    """ Convert matrix to line """
    def translateMatrixToLine(self, matrix):
        # Initiate empty array
        pixelLine = [None] * matrix.numPixels
        for i in range(0, len(matrix.matrixArr)):
            for j in range(0, len(matrix.matrixArr[i])):
                # Revert vertically
                if ((j + 1) % 2) > 0:
                    pos = len(matrix.matrixArr) * j + abs(i - (len(matrix.matrixArr) - 1))
                elif ((j + 1) % 2) == 0:
                    pos = len(matrix.matrixArr) * j + i
                pos = matrix.numPixels - pos - 1 #revert horizontally
                pixelLine[pos] = matrix.fillerPositive if matrix.matrixArr[i][j] == matrix.fillerPositive else matrix.fillerNegative
        return pixelLine
