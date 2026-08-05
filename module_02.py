# 표준 라이브러리 math 모듈
import math

# import random # import 들은 다 위로 모아둠


print(math.sqrt(9))  # 제곱근값 3.0
print(math.ceil(4.2))  # 올림값 5
print(2**3)  # 2의 2승 = 2 *2 = 8

# math에서 sqrt, ceil 두개만 사용한다면 이렇게 써도 됨
from math import sqrt, ceil

print(sqrt(9))
print(ceil(4.2))

print("=" * 20)


print("==========================")

# 표준 라이브러리 random 모듈
import random

print(random.randint(1, 10))  # 1~10 중 무작위 정수
print(random.choice(["정상", "경고", "위험"]))  # 셋 중 무작위

print("==========================")

# 표준 라이브러리의 detetime.모듈
import datetime

# datetime 모듈 안의 datetime 클래스에스 지원하는 now() 함수 호출
now = datetime.datetime.now()
print(now)

print("==========================")
# 모듈 도움말 보기 : 참고만 하고 구글링한 웹사이트에서 보기
# print(dir(math))
# help(math.sqrt)
