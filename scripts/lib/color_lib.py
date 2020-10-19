import colorsys
import numpy as np


def _nonlin(x, sig):
    rez = 1 / (1 + np.exp(-sig * (x - 0.5)))
    rez -= np.min(rez)
    rez *= np.max(x) / np.max(rez)
    return rez


# Generate n "distinct" colors
# Use HSL->RGB conversion
# Use nonlinearity, because human eye seems to tell apart reds better than greens
def rainbow(n):
    hues = _nonlin(np.arange(n) / n, 3)
    return np.array([colorsys.hsv_to_rgb(hue, 1, 1) for hue in hues])