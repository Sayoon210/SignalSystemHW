"""
2020142149 김사윤
신호와 시스템 HW2 - (6) 과제 소스코드 (a)
"""

import matplotlib.pyplot as matplot
import numpy as np

pi = np.pi
k = np.arange(0, 10, 1)

# w = 2pi/N, N=10이다.
w = pi / 5

a = 0.1 * (
    np.exp(-(1j * w * k))
    + 2 * np.exp(-(2 * 1j * w * k))
    + 3 * np.exp(-(3 * 1j * w * k))
    + 2 * np.exp(-(4 * 1j * w * k))
    + np.exp(-(5 * 1j * w * k))
)
mag = np.sqrt(np.power(a.real, 2) + np.power(a.imag, 2))

# plot code
signalGraph = matplot.stem(k, mag)
markerline, stemlines, baseline = signalGraph
# labeling
for i in range(len(k)):
    matplot.text(k[i], mag[i] + 0.02, f"{mag[i]:.2f}", ha="center", va="bottom")
matplot.xticks(np.arange(0, 10, 1))
markerline.set_markersize(3)
matplot.title("Coefficient Magnitude Plot")
matplot.xlabel("k")
matplot.ylabel("Size")
matplot.ylim(0, 1)
matplot.grid(True)
matplot.show()
