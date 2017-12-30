from renderer_abstract import rendererAbstract
from neopixel import * # see https://github.com/jgarff/rpi_ws281x

""" LED strip configuration """
numPixels      = 256                   # 32 * 8
LED_PIN        = 18                    # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000                # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5                     # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 20                     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False                 # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0                     # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

""" Renderer for matrix on BTF Lighting 8x32 """
""" https://www.amazon.com/gp/product/B01DC0IPVU/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1 """
class rendererBtfLighting8x32(rendererAbstract):
    """ Colors for positive and negative """
    colorFillerPositive = Color(0, 0, 100)
    colorFillerNegative = Color(0, 0, 0)
    """ Initialize """
    def __init__(self):
        self.strip = Adafruit_NeoPixel(numPixels, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self.strip.begin()
    """ Main function to render things on screen """
    def render(self, matrix):
        # Show string on LED screen
        translatedMatrixArr = self.translateMatrixToLine(matrix)
        for i in range(len(translatedMatrixArr)):
            self.strip.setPixelColor(i, translatedMatrixArr[i])
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
                pixelLine[pos] = self.translateMatrixFillToColor(i, j, matrix)
        return pixelLine
    """
        Translate matrix filler to an actual color on screen

        @return Color
    """
    def translateMatrixFillToColor(self, rowNum, columnNum, matrix):
        matrixFiller = matrix.matrixArr[rowNum][columnNum]
        if matrix.fillerPositive == matrixFiller:
            return self.colorFillerPositive
        elif matrix.fillerNegative == matrixFiller:
            return self.colorFillerNegative
        elif matrix.fillerSeconds == matrixFiller:
            redBase = 25
            greenBase = int(25 - (columnNum * 0.78)) # I need 0-25 as function of 0-32
            blueBase = 0
            return Color(redBase, greenBase, 0)
        return self.colorFillerNegative
