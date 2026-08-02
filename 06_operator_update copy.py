# 산술연산자
# + - * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5)  # 8
print(10 - 4)  # 6
print(4 * 5)  # 20
print(20 / 4)  # 5.0 나눗셈 결과는 항상 float
print(7 // 3)  # 2 (나눗셈 결과의 몫)

# 7개의 음료수를 3봉투에 나눠담으면, 2봉투와 1개의 음료수가 나옴
print(7 % 3)  # 1 (나눗셈 결과의 나머지)
print(2**5)  # 32 (2의 5제곱)


# =================
# 연산 우선순위와 우선순위 지정
# **(거듭제곱) > *(곱하기) /(나누기) //(몫) %(나머지) > +(더하기) -(빼기)


print(2 + 8 * 3)  # 8 * 3 연산 후 그 결과를 2와 더함
print((2 + 8) * 3)  # 괄호 안의 연산을 먼저한 뒤 곱하기 계산


# ==================
# 복합연산자

result = 3 * 5
print(result)  # 15
# += : 기존 값에서 오른쪽 값을 더한 뒤 재할당
# -= : 기존 값에서 오른쪽 값을 뺀 뒤 재할당
# *= : 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /= : 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10  # 25
print(result)
result -= 5  # 20
print(result)
result *= 3  # 60
print(result)
result /= 2  # 30.0
print(result)

# ================
# 문자열 연산
print("안녕" + "하세요")  # 안녕하세요

# 만약 "안녕"과 "하세요"사이에 공백을 1개 넣고싶다면
# 방법 1) , 사용
print("안녕", "하세요")
# 방법 2) 안녕 뒤에 공백 추가
print("안녕 " + "하세요")
# 방법 3) 공백만 있는 문자열 더하기
print("안녕" + " " + "하세요")

# 문자열 곱하기
print("안녕" * 5)

# 문자열에 연산자를 사용할 경우 모두 이어져서 나온다
print("=== 실습 ===")

a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)


print("=== 실습2 ===")
x = 40
y = 56
z = 60
print((x + y + z) / 3)
side = 7
print(side**2)
print(3 * 4 * 5)

print(10 == 10)
print(10 != 10)
print(10 > 5)
print(5 < 10)
print(10 >= 5)
print(10 <= 5)

print("=== 실습4 ===")
temp = 85
temp_ok = 60 <= temp and temp <= 90
print(temp_ok)
pressure = 5
pres_ok = 3 <= pressure and pressure <= 7
print(pres_ok)
print(temp_ok and pres_ok)

print("=== 실습5 ===")
stock = 100
print(stock)
stock += 50
print(stock)
stock -= 30
print(stock)
stock += 5
print(stock)


print("=== 실습6 ===")
total = 500
defect = 23
print(defect / total * 100)
run_h = 21
all_h = 24
print(run_h / all_h * 100)


print("=== 실습7 ===")
minutes = 500
print(minutes // 60)
print(minutes % 60)
