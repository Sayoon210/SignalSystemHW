"""
2020142149 김사윤
신호와 시스템 HW1 - (8) 과제 소스코드 5

"""

import matplotlib.pyplot as matplot
import numpy as np

pi = np.pi
n = np.arange(0, 100, 1)

u_n = np.heaviside(n, 1)
u_n_delay50 = np.heaviside(n-50, 1)

x_n = 0.5*(u_n - u_n_delay50)
x_n2 = np.sin(n*pi/25)*u_n_delay50

x3 = x_n + x_n2

signalGraph = matplot.stem(n, x3)
markerline, stemlines, baseline = signalGraph
matplot.xticks(np.arange(0, 100, 5))
markerline.set_markersize(3)

# 불연속 신호를 그리는 경우이므로 stem을 사용하였음.
matplot.title('x3 = x1[n] + x2[n] Plot')
matplot.xlabel('Discrete Time n')
matplot.ylabel('x3')
matplot.grid(True)
matplot.show()
