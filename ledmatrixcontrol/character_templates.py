fillerNegative = "_"

""" Character template partial as bool
"""
def charAsBool(char):
    if char == fillerNegative:
        return False
    return True

""" Templates for individual numbers (matrices)
"""

""" Digits template for reference
__________________________________________________________
__X___XX___XX___X_X____XX____XX___XXX___XXX___XXX____X____
_XX____X____X___X_X____X____X_______X___X_X___X_X___X_X___
__X___X____XX___XXX____XX___XXX_____X___XXX____XX___X_X___
__X___X_____X_____X_____X___X_X_____X___X_X_____X___X_X___
__X___XX___XX_____X____XX___XXX_____X___XXX_____X____X____
__________________________________________________________

"""

digitOne = """
__X
XXX
__X
__X
__X
"""

digitTwo = """
XXX
__X
_X_
X__
XXX
"""

digitThree = """
XXX
__X
_XX
__X
XXX
"""

digitFour = """
X_X
X_X
XXX
__X
__X
"""

digitFive = """
XXX
X__
XXX
__X
XXX
"""

digitSix = """
_XX
X__
XXX
X_X
XXX
"""

digitSeven = """
XXX
__X
__X
__X
__X
"""

digitEight = """
XXX
X_X
XXX
X_X
XXX
"""

digitNine = """
XXX
X_X
_XX
__X
__X
"""

digitZero = """
_X_
X_X
X_X
X_X
_X_
"""

divider = """
___
_X_
___
_X_
___
"""

# Character to template map
renderDict = {
    '0': digitZero,
    '1': digitOne,
    '2': digitTwo,
    '3': digitThree,
    '4': digitFour,
    '5': digitFive,
    '6': digitSix,
    '7': digitSeven,
    '8': digitEight,
    '9': digitNine,
    ':': divider
}