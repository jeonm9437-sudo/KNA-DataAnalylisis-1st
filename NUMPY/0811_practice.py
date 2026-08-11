print("=== 실습 1 ===")
import numpy as np

rotation = np.array([1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600])
specific_value = rotation[3]
front = rotation[1:3]
interval = rotation[::2]

print("특정 시점 값: ", specific_value)
print("앞 구간: ", front)
print("두 칸 간격 값: ", interval)

print("=== 실습 2 ===")

import numpy as np

data = np.array([[1200, 10], [1300, 12], [1400, 14], [1500, 16]])

equipment = data[2]
rotation = data[:, 0]
torque = data[:, 1]

print("특정 설비: ", equipment)
print("회전수: ", rotation)
print("토크: ", torque)

print("=== 실습 3 ===")

import numpy as np

rotation = np.array([1000, 1200, 1500, 1800, 2000])

min_value = rotation.min()
max_value = rotation.max()
normalized = (rotation - min_value) / (max_value - min_value)

print("원본 회전수: ", rotation)
print("최솟값: ", min_value)
print("최댓값: ", max_value)
print("정규화 결과: ", normalized)

print("=== 실습 4 ===")

import numpy as np

rpm4 = np.array([1350, 1520, 2180, 1450, 2750, 1600])
torque4 = np.array([45.2, 38.6, 52.1, 48.7, 6.5, 43.9])

print(rpm4[rpm4 > 2000])

# 다중 조건으로 회전수 과다 또는 토크 과소 위험 시점 필터링
# -> rpm[0] 데이터와 torque[0] 데이터는 같은 시기의 상황을 다룬다

print(rpm4[(rpm4 > 2000) | (torque4 < 10)])

print("=== 실습 5 ===")

import numpy as np

torque5 = np.array([35.5, 42.3, 51.7, 28.6, 63.2, 47.8, 55.4, 39.1])

condition = torque5 >= 50
count = condition.sum()
ratio = condition.mean()

print("조건 만족 개수: ", count)
print("조건 만족 비율: ", ratio)

# ====================================
print("=== 실습 6 ===")
import numpy as np

data6 = np.array([[1200, 35.5], [1500, 42.3], [1800, 51.7], [1400, 28.6], [1600, 63.2]])

print("센서별 평군: ", data6.mean(axis=0))
print("센서별 표준편차: ", data6.std(axis=0))
