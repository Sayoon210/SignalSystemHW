"""
2020142149 김사윤
신호와 시스템 HW2 - (6) 과제 소스코드 (b) - (1)
"""

import matplotlib.pyplot as matplot
import numpy as np

pi = np.pi
prob = 4
w = pi/5
ak_mag = []
ak_phs = []

for k in range(prob):
    a = 0.1 * (np.exp(-(1j*w*k)) + 2*np.exp(-(2*1j*w*k)) + 3* np.exp(-(3*1j*w*k)) + 2* np.exp(-(4* 1j*w*k)) + np.exp(-(5* 1j*w*k)))
    Re = a.real
    Im = a.imag
    mag = np.sqrt(np.power(Re,2) + np.power(Im,2))
    phs = np.arctan(Im/Re)
    ak_mag.append(mag)
    ak_phs.append(phs)

# 푸리에 게수 크기 위상 배열
mag_arr = np.array(ak_mag)
phs_arr = np.array(ak_phs)

# 재조합
for n in range(-15, 15):
    x_n = sum((mag_arr[k]*np.exp(1j*w*k*n+phs_arr[k])) for k in range(prob))
    signalGraph = matplot.stem(n, x_n.real)
# plot code

markerline, stemlines, baseline = signalGraph
'''# labeling
for i in range(len(k)):
    matplot.text(k[i], mag[i]+0.02, f'{mag[i]:.2f}', ha='center', va='bottom')'''
matplot.xticks(np.arange(-10, 30, 1))
markerline.set_markersize(3)

# 불연속 신호를 그리는 경우이므로 stem을 사용하였음.
matplot.title('Reconstructed x[n] - (1)')
matplot.xlabel('n')
matplot.ylabel('Size')
matplot.grid(True)
matplot.show()
