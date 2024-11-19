"""
2020142149 김사윤
신호와 시스템 HW1 - (8) 과제 소스코드 1

"""

import matplotlib.pyplot as matplot
import numpy as np

# 범위는 0 <= n < 100
n = np.arange(0, 100, 1)

# numpy에서 unit step function 만들기 위해 쓴 heaviside이다.
# 0보다 크면 1, 작으면 0, 그리고 0일때는 설정값이다 (설졍값은 현재 1)
u_n = np.heaviside(n, 1)
u_n_delay50 = np.heaviside(n-50, 1) # 50만큼 delay

x_n = 0.5*(u_n - u_n_delay50)

# 그래프에 5 단위의 격자를 추가하였음.
matplot.xticks(np.arange(0, 100, 5))

# 불연속 신호를 그리는 경우이므로 stem을 사용하였음.
matplot.stem(n,x_n)
matplot.title('x1[n] Plot')
matplot.xlabel('Discrete Time n')
matplot.ylabel('x1[n]')
matplot.grid(True)
matplot.show()
