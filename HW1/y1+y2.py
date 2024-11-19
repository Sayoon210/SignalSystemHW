"""
2020142149 김사윤
신호와 시스템 HW1 - (8) 과제 소스코드 7

"""

import matplotlib.pyplot as matplot
import numpy as np

pi = np.pi
n = np.arange(0, 100, 1)

u_n = np.heaviside(n, 1)
u_n_delay50 = np.heaviside(n-50, 1)

x_n = 0.5*(u_n - u_n_delay50)
x_n2 = np.sin(n*pi/25)*u_n_delay50
h_n = np.exp((-1)*n*pi/25)*(u_n - u_n_delay50)/25

y1 = np.convolve(x_n, h_n, mode='same')
y2 = np.convolve(x_n2, h_n, mode='same')

signalGraph = matplot.stem(n, y1+y2)
markerline, stemlines, baseline = signalGraph
matplot.xticks(np.arange(0, 100, 5))
markerline.set_markersize(3)
markerline.set_color('red')
stemlines.set_color('red')
# 불연속 신호를 그리는 경우이므로 stem을 사용하였음.
matplot.title('y1+y2 plot')
matplot.xlabel('Discrete Time n')
matplot.ylabel('y1+y2')
matplot.grid(True)
matplot.show()
