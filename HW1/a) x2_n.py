"""
2020142149 김사윤
신호와 시스템 HW1 - (8) 과제 소스코드 2

"""

import matplotlib.pyplot as matplot
import numpy as np

pi = np.pi
n = np.arange(0, 100, 1)

u_n_delay50 = np.heaviside(n-50, 1)
x_n2 = np.sin(n*pi/25)*u_n_delay50

signalGraph = matplot.stem(n, x_n2)
markerline, stemlines, baseline = signalGraph

# 그래프 설정
matplot.xticks(np.arange(0, 100, 5))
markerline.set_markersize(3)

matplot.title('x2[n] Plot')
matplot.xlabel('Discrete Time n')
matplot.ylabel('x2[n]')
matplot.grid(True)
matplot.show()
