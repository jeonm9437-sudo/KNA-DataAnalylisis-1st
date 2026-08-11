# 미국식 속더 (miles)를 우리가 쓰는 속도(Km)로 변환시켜주는
# NumPy 배열 예제 코드

import numpy as np
miles = np.array([94.7, 104.5, 105.5])

# 속도(km/h) = 속도(mph)x1.60934

print(miles * 1.60934) # [152.404498 168.17603  169.78537 ]

# 실습 4=======================
print("=== 실습 4 ===")
import numpy as np

# 웬만하면 2차원 배열 만들기
apt_games = np.array([
    [3, 6, 9],
    [4, 8, 10]
])

print(apt_games)

# ndim 차원확인
print(apt_games.ndim)
# shape 형태확인
print(apt_games.shape)
# size 전체 개수 확인
print(apt_games.size)

# 실습 5 자료형 확인과 변환======================
print("=== 실습 5 ===")

import numpy as np
data = np.array([1234.789, 456.486, 789.564])

# dtype으로 현재 자료형 확인
print(data.dtype) # float64

# astype으로 정수형으로 변환한 새 배열 출력
converted_data = data.astype(int)
print(converted_data) # [1234  456  789]

# ==================================
print("=== 실습 6 ===")

import numpy as np

# 연속 정수 배열을 arange로 생성


# ==============================
print("=== 실습 7 ===")

import numpy as np

# 시점과 센서 수를 곱한 개수만큼 연속값을 arange로 생성
# 만약 시점이 오후 3시, 오전 3시라면 시점 (timestamp)은 2개
# 센서는 5개 있다고 가정
# 시점 X 센서 = 10
data = np.arange(10)

# 행을 시점, 열을 센서 수로 정해 reshape로 표 형태 변환
converted_data = data.reshape(2, 5)

# 정리된 표 배열 출력
print(converted_data)


# ==================================
print("=== 실습 8 ===")

import numpy as np

# [최종결과]
# 형태와 자료형 확인 후 3행 2열 표로 정리된 배열 출력
# 최종형태 shape : (3, 2)
# 최종형태 size : 3 * 2 = 6 

# 센서 측정값을 np.array로 배열 생성
data = np.array([4.5, 3.2, 1.7, 9.8, 5.4, 7.6])

# shape과 dtype으로 구조 확인
print(f"shape: {data.sahpe}")
print(f"dtype: {data.dtype}")

# reshape으로 분석용 표 형태로 정리한 뒤 출력
converted = data.reshape(3, 2)
print(converted)

# ==========================
print("=== 실습 1 ===")
# 실습1. 특정 센서,구간 추출하기

import numpy as np

# 예시 : 회전수 배열
rpm = np.array([1551, 1408, 1498,])