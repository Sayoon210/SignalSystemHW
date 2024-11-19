"""
2020142149 김사윤
신호와 시스템 HW2 - (6) 과제 소스코드 (a)
"""

import matplotlib.pyplot as matplot
import numpy as np

pi = np.pi
k = np.arange(0, 10, 1)

# w = 2pi/N, N=10이다.
w = pi/5

# 실수부와 허수부 구분 (1/10 은 마지막에 계산할 때 곱함)
Re_cos_sum = np.cos(w*k) + 2*np.cos(2*w*k) + 3*np.cos(3*w*k) + 2*np.cos(4*w*k) + np.cos(5*w*k)
Im_sin_sum = np.sin(w*k) + 2*np.sin(2*w*k) + 3*np.sin(3*w*k) + 2*np.sin(4*w*k) + np.sin(5*w*k)

# 크기 계산 {(Re제곱 + Im제곱)의 제곱근} / 10 으로 계산
mag = np.sqrt(pow(Re_cos_sum, 2) + pow(Im_sin_sum, 2)) / 10

# plot code
signalGraph = matplot.stem(k, mag)
markerline, stemlines, baseline = signalGraph
# labeling
for i in range(len(k)):
    matplot.text(k[i], mag[i]+0.02, f'{mag[i]:.2f}', ha='center', va='bottom')
matplot.xticks(np.arange(0, 10, 1))
markerline.set_markersize(3)

# 불연속 신호를 그리는 경우이므로 stem을 사용하였음.
matplot.title('Coefficient Magnitude Plot')
matplot.xlabel('k')
matplot.ylabel('Size')
matplot.ylim(0, 1)
matplot.grid(True)
matplot.show()
