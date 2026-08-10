# 파이썬에서 기본 제공하는 기능들 외에
# 다양한 외부 라이브러리들을 가져오려면
# https://pypi.org/ 사이트에서 검색부터 하기

# 터미널에서 바로 pip로 설치를 시도하면 (pip install numpy)
# 전체 시스템에 영향을 주는 설치로 생각되어 거절함
# 그래서 개별 Working Directory마다 별도의 환경을 구축해
# 그 안에 개별 프로젝트가 사용할 pip 라이브러리들을 따로 받아 쓰게 함
# 이것이 바로 가상환경 (venv)


# 1. 현재 경로에 가상환경 생성
# python -m venv .venv

# 2. 가상환경 활성화
# source .venv/bin/activate
# (이후에는 가상환경 안에서 터미널 명령 실행 가능, 예) pip intall numpy)

# 3. (작업/실행 끝나고) 가상환경 종료
# deactivate
import numpy as np

numbers = [1, 2, 3, 4, 5]
# 위 int값들의 리스트를 사용해서 numpy의 배열 만들기
np_numbers = np.array(numbers)
print(np_numbers)

# =========================================
print("=== array ===")
import numpy as np

# 파이썬의 리스트로부터 NumPy 배열 만들기
temp = np.array([70.5, 69.8, 73.7])

print(temp)  # [70.5 69.8 73.7] 항목 사이에 콤마 없음 유의

# 배열의 항목들마다 +5씩 더하려면?
# 리스트였다면 for문으로 항목마다 직접 처리해줬어야함
# NumPy라면 간단하게
print(temp + 5)  # [75.5 74.8 78.7]

# 소숫점 이하가 없는 숫자 타입들로 가득찬 배열
print(np.array([1, 2, 3, 4, 5]))  # [1 2 3 4 5]

# 소숫점 이하가 있는 숫자 타입들로 가득 찬 배열
print(np.array([3.14, 6.7, 7.67]))  # [3.14 6.7  7.67]

# 소숫점 이하가 있는것 없는것이 섞여있다면?
# 모두 소숫점 이하가 있는 것으로 배열 생성
print(np.array([1, 3, 5, 3.14, 6.7, 4])) # [1.   3.   5.   3.14 6.7  4.  ]

print("=== arange ===")

import numpy as np

# 0부터 4까지 생성 (5는 제외)
under_five = np.arange(5)
print(under_five) # [0 1 2 3 4]

# 0부터 8까지 2간격 (8보다 큰 숫자가 만들어지면 덧붙이지 않고 끝)
gab_two = np.arange(0, 10, 2)
print(gab_two) # [0 2 4 6 8]

# ============================
print("=== linspace ===")

import numpy as np

# linspace
# 개수 중심 균등 분할
# 시작과 끝 구간을 지정한 개수만큼 정확시 나눔
# 간격은 알아서 계산하도록 함

# 0부터 1까지 5개로 균등 분할
div_five = np.linspace(0, 1, 5)
print(div_five) # [0.   0.25 0.5  0.75 1.  ]  

# =================================
print("=== zeros ===")

import numpy as np

# 0으로 채우기
block_zero = np.zeros(5)
print(block_zero) # [0. 0. 0. 0. 0.]

# 7으로 채우기
block_seven = np.full(4, 7)
print(block_seven) # [7 7 7 7]

# 명시적으로 7.0처럼 float값을 지정해줘야
# float 타입 값들로 채워지는 배열이 만들어진다
block_seven = np.full(4, 7.0)
print(block_seven) # [7. 7. 7. 7.] 

# =======================
# 0부터 30까지 6간격으로 배열 채워만들기
# 0부터 숫자 6씩 증가시켜가면서 30보다 작은 값들일때 배열에 붙여나감
import numpy as np

gab_six = np.arange(0, 30, 6)

# 0부터 30까지 6등분 나누어 배열 내용 채우기
div_six = np.linspace(0, 30, 6)
print(div_six)

# ====================================
# 측정 시간축 배열 만들기

import numpy as np

# 특정 시작 시각과 끝 시각을 정해서
# 특정 간격 시간들이 지난다면
# 언제 언제 체크포인트가 만들어지나를
# numpy의 배열로 알아보기

# 예를 들어 0초부터 60초 사이에
# 5초간격으로 체크를 한다면
# 실제로는 몇초 몇초... 체크하는 지점이 생기나
# 알아보기
checks = np.arange(0, 60, 5)
print(checks)
# [ 0  5 10 15 20 25 30 35 40 45 50 55]

# ==============================
print("=== convert ===")

import numpy as np

# 형변환(astype)
# 예를들어 아래의 float들로 가득한 배열이 있다면
convertable = np.array([3.14, 6.7, 1.23])
print(convertable.dtype) # float64


# int들로 가득한 배열로 알아서 바꿔줌
converted = convertable.astype(int)
print(converted) # [3 6 1]
print(converted.dtype) # int64

# ============================
# reshpae로 형태 바꾸기
# size로 확인되는 값 개수는 같아야 함

import numpy as np

under_ten = np.arange(10)
print(under_ten)
print(f"ndim: {under_ten.ndim}") # 1
print(f"shape: {under_ten.shape}") # (10, )
print(f"size: {under_ten.size}") # 10

reshape_ten = under_ten.reshape(2, 5)
print(reshape_ten)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]
print(f"ndim: {reshape_ten.ndim}") # 2
print(f"shape: {reshape_ten.shape}") # (2, 5)
print(f"size: {reshape_ten.size}") # 10 -> 안바뀜 😻😻

# flatten으로 1차원 만들기
flatten_ten = reshape_ten.flatten()
print(flatten_ten) # [0 1 2 3 4 5 6 7 8 9]