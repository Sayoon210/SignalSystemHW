"""
2020142149 김사윤
신호와 시스템 HW2 - (6) 과제 소스코드 (b) - (2)
"""

import matplotlib.pyplot as matplot
import numpy as np

pi = np.pi

# k의 (2)에서 범위 최대값
prob = 7

# 문제의 범위보다 살짝 크게  plot
n = np.arange(-11, 15, 1)
w = pi / 5
a_rr = np.zeros(prob, dtype=complex)

for k in range(prob):
    a = 0.1 * (
        np.exp(-(1j * w * k))
        + 2 * np.exp(-(2 * 1j * w * k))
        + 3 * np.exp(-(3 * 1j * w * k))
        + 2 * np.exp(-(4 * 1j * w * k))
        + np.exp(-(5 * 1j * w * k))
    )
    a_rr[k] = a

# 재조합
x_n = sum((a_rr[k] * np.exp(1j * w * k * n)) for k in range(prob))
signalGraph = matplot.stem(n, x_n.real)
markerline, stemlines, baseline = signalGraph
matplot.xticks(np.arange(-11, 15, 1))
markerline.set_markersize(3)
matplot.title("Reconstructed x[n] - (2)")
matplot.xlabel("n")
matplot.grid(True)
matplot.show()
