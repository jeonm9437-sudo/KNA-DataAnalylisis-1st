# """ """ - 여러 줄 문자열

notice = """설비 점검 안내
1. 전원 확인
2. 센서 점검"""

print(notice)
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
# 위와 같이 직접 작성한 줄바꿈이 반영되어 여러 줄로 출력함

notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""
print(notice)
#
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
#
# 개발자가 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나옴
# """ """ (삼중 따옴표를 사용할 시 그 내부의 모든 줄바꿈이 다 반영되어 출력)

# 탭
notice = """설비 점검 안내
  1. 전원 확인
 2. 센서 점검"""

print(notice)
# 삼중 따옴표는 탭도 그대로 유지됨

# =======================
# 이스케이프 문자

print("=== 이스케이프 문자 ===")


# notice 이스케이프 사용해서 개선
notice = "설비 점검 안내\n1, 전원 확인\n2,센서 점검"
print(notice)

tap = "이름\t상태"
print(tap)
print("이름 상태")

backslash = "이름\\상태"
print(backslash)  # 이름\상태 > 첫 번째는 \는 이스케이프 문자라는 것을 알리는 용도

# quotes = 'It\'s me'  # 감싸는 따옴표와 str 내부 따옴표의 종류가 같을 때는 \를 사용
# 자동저장때문에 \넣었을때 바뀌는 것, 그대로 하고 싶으면 주석처리
# print(quotes)

# 빈 문자열과 공백 문자열의 차이
# "" 따옴표로 감싸졌지만 아무것도 작성되지 않았다면 "빈 문자열"
# 빈 문자열을 글자수 0, 길이 0
# " " 따옴표 안에 공백(스페이스바)이 있는 경우 "공백 문자열"
# 공백(스페이스바)의 수 만큼 글자가 잇고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨
print("" == "")  # False

code = "PUMP_A"
state = "정상"
hour = 1200
date = "2026-07-16"
card = "설비: " + code + "\n상태: " + state + "\n가동: " + str(hour) + "\n점검: " + date
print(card)

# 예상 출력 결과
# 설비: PUMP_A
# 상태: 정상
# 가동: 1200
# 점검: 2026-07-16


# ===========================
# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 문자열[인덱스번호]
# 문자열의 첫 글자 인덱스는 0
print("=== 인덱싱 ===")

word = "PYTHON"
print(word[0], word[3], word[5])  # P H N

# print(word[100])  # IndexError
# word 변수에 저장된 문자열의 길이보다 큰 인덱스를 호출했기 때문

abc = "abcdefghijklnmopqrstuvwxyz"
print(abc[13] + abc[8] + abc[18] + abc[14])  # miso

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# 주의사항은 음수 인덱스는 가장 마지막 글자가 -1부터 시작

# =================================
print("=== 슬라이싱 ===")

# 슬라이싱은 - 구간으로 잘라내기
# 문자열[시작:끝]
# 시작 인덱스 글자는 포함해서 출력
# 끝인덱스 글자는 제외하고 출력

print("word[3:5] 결과:", word[3:5])  # HO
print("word[3:6] 결과:", word[3:6])  # HON
# 슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱스인 6도 사용할 수 있음

# print(word[6])  # 인덱싱은 정확하게 마지막 인덱스까지만 쓸 수 있고, 넘치면 Error

# 슬라이싱 - start 생략
# 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용
print(word[:4])  # print(word[0:4])와 동일한 동작

# 슬라이싱 - end 생략
# 특정 인덱스부터 끝까지 구간을 뽑아내고 싶을 때 사용
print(word[2:])  # 2번 인덱스까지 끝까지 출력
# print(word[2:6])과 동일한 동작

# 슬라이싱 - 전체 생략
print(word[:])  # print(word[0:6])과 동일한 동작
# :을 사용하고 start와 end를 모두 생략하면 모든 인덱스의 구간을 뽑아냄

# 슬라이싱 - 음수 인덱스 사용
print(word[-3:])  # HON
# 음수 인덱스 작성 시 그냥 그 인덱스부터 정방향으로 출력함
print(word[:-1])  # PYTHON
# 처음부터 -1(5)를 제외한 구간을 뽑아냄
# 역순 아님 주의
# 음수 인덱스 사용 시 컴퓨터가 정수 인덱스 찾아 치환해서 동작

# step으로 건너뛰기
print(word[0:6:2])  # PTO
# PYTHON에서 첫 번째 글자는 명시했으니 거기서부터 출력
# step이 2이기 때문에 Y 뛰고, T(두번째 점프)출력
# H 뛰고, O(두번째 점프) 출력
# N 뛰고 끝
# 두 글자를 뛰는게 아니라 두 "번" 뛰는 것 (뛴 그 자리 글자를 출력한다)

print(word[0:6:1])  # PYTHON

# start와 end를 생략하고 step만 입력
print(word[::2])  # PTO
# word 변수의 모든 글자를 두 칸씩 뛰면서 출력

# 순서 뒤집기
print(word[::-1])  # NOHTYP
# step은 인덱스가 아니고, 음수 입력 시 순서를 뒤집음

# 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
print("범위를 벗어난 슬라이싱", word[0:100])  # PYTHON을 정상 출력

# ===============================
# len() - 문자열의 길이 반환
# len(문자열)

print("=== len() 활용 ===")

print(len("Hello world!"))  # 12 (공백도 모두 글자 취급)
print(len(""))  # 0 (빈 문자열은 0 출력)

var = "여러분~! 한 시간만 더 하면 됩니다! 조금만 더 힘을 내주세요!"
print(len(var))  # 변수에 담긴 문자열의 길이 출력도 가능


print(len("이것도") - len("가능할까?"))
# len()은 int를 반환하기 때문에 연산 가능

print("abc 변수의 길이:", len(abc), " / 마지막 인덱스 번호:", len(abc) - 1)

# 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때
print(abc[len(abc) - 1])

print("=== 실습 ===")
a = "01012345678"
print(len(a))


# =====================
print("=== in 활용 ===")


# in - 특정 문자가 문자열에 포함되었는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool)으로 결과 반환
# 찾을문자열 in 문자열
print("고장" in "설비 고장 발생")  # True
print("정상" in "설비 고장 발생")  # False
print("설비에서 고장" in "설비 고장 발생")  # False
print("설비에서 고장" in "설비에서 고장이 났습니다.")  # True

# not in - in의 정반대 동작
print("고장" not in "설비 고장 발생")  # False
print("정상" not in "설비 고장 발생")  # True
print("설비에서 고장" not in "설비 고장 발생")  # True
print("설비에서 고장" not in "설비에서 고장이 났습니다.")  # False

print(" " in "설비 고장 발생")  # True
# 따옴표로 감싼 공백(스페이스바)는 정말 "한 글자"로 취급

# ====================
print("=== count() ===")

# .count() - 문자열에 특정 글자의 수(int)를 반환
# 문자열.count("찾을 글자")
print("banana".count("a"))  # 3
print("010-1234-1234".count("-"))  # 2
print("layla@spreatics.com".count("@"))  # 1

print("1,2,3,4".count(","))

# =====================
print("=== find() ===")
# 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1을 반환

email = "hong@company.com"
at = email.find("@")  # @ 위치의 인덱스인 4가 할당
user_id = email[:at]  # hong 이라는 사용자의 아이디만 추출
print(user_id)  # hong

# SQE-00Q8이라는 설비의 SQE만 뽑아내기 (find와 슬라이싱 사용)
sqe = "SPE-00Q8"

# sqe_index = sqe

sqe_index = sqe.find("SQE")
print(sqe_index)  # 0

sqe_index = sqe.find("-")
print(sqe_index)  # 3
sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
print(sqe_fin)

# ===============================
print("=== index() ===")

# 특정 문자열의 위치(인덱스 번호)를 반환
# 앞에서부터 가장 처음 나오는 인덱스 번호만 반환
# 찾는 문자열이 없으면 Error 발생

email = "layla@spreatics.com"
at = email.index("@")  # 5
print(email[0:at])  # layla
print(email[:at])  # 시작 번호가 0이라면 start 생략 가능
print(email[at:])  # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략
# 위처럼 시작하면 5번 인덱스부터 출력하기 때문에 @를 포함
print(email[at + 1 :])  # at + 1을 하면 @를 포함하지 않고 출력

# find에서 했던 SQE 뽑아내기 실습 index 사용으로 바꾸기
sqe = "SQE-00Q8"
sqe_index = sqe.index("-")  # / 없으니 Error 나고 중단
print(sqe_index)  # 3
sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
print(sqe_fin)  # SQE

# 만약에

# sqe = "SQE-00Q8"
# sqe_index = sqe.index("/") # / 없으니 Error 나고 중단
# print(sqe_index)  # 3
# sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
# print(sqe_fin) # SQE


# ===============================
print("=== count() ===")

# 문자열에서 특정 문자열의 갯수 세기

str = "a, b, c, d, e,a, a"

# a의 갯수 세기
print(str.count("a"))  # 3

# ,의 갯수 세기
print(str.count(","))  # 6

print(str.count(", "))  # 5 # count로 찾는 문자열와 완전히 동일해야 갯수를 셈

# =========================
print("=== startswith() ===")

# 특정 문자열로 시작하는지 검사
# True/False (불리언)

# EQP로 시작하는지 검사하기
print("EQP-001".startswith("EQP"))

# 변수 활용
eqp = "EQP"
print("EQP-001".startswith(eqp))
# 주의사항) 변수면 따옴표 감싸기 금지 !!!

# ==========================
print("=== startswith() ===")

# 특정 문자열로 끝나는지 확인
# True/False로 반환

str2 = "월요일입니다! 여러분은 할 수 있어요!"
print(str2.endswith("!"))  # True
print(str2.endswith("요!"))  # True
print(str2.endswith("음!"))  # False
print(str2.endswith("월요일입니다! 여러분은 할 수 있어요!"))  # True
print(str2.endswith("월요일입니다!     여러분은 할 수 있어요!"))  # False
print(str2.endswith("월요일입니다! 여러분은 할 수 있어요! "))  # False
print(str2.endswith(" 월요일입니다! 여러분은 할 수 있어요!"))  # False

print("=== 실습5 ===")
str5 = "sensor_log.csv"
print(str5.startswith("sensor"))
print(str5.endswith(".csv"))


# == 로 대소문자 구분

label = "WARNING"
print(label == "WARNING")
print(label == "warning")

# ===============================
print("=== 값은 객체다 ===")

print(type("잊어먹으면 안돼!!!"))  # <class 'str'>
print(len("이렇게 썼죠??"))
# endswith와 len의 차이는
# endswith는 .으로 연결
# .으로 연결하는 이른 도구들은 "메서드"
# 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능

# len은 . 사용 안함
# () -> 함수
# len과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 "내장함수"

"str".startswith("S")
# 123.startswith(1)
# .으로 사용하는 메서드들은 특정 자료형(객체 타입)마다 다름
# int 자료형의 객체에는 startswith라는 메서드가 없음


# print(len(123))  # len 내장함수는 길이를 반환하기 때문에 int 자료형은 사용 불가

word = "python"
print(word.upper())  # upper는 모두 대문자로 바꿔줌 # PYTHON
print(word.count("p"))  # 1
print(word.startswith("p"))  # True


# ====================
# 재할당 복습

num = 1
num = num + 1  # 2
num += 1  # 3
# += 은 복합할당연산자
# 원래 내 자신의 값에 다음 오는 연산자와 값을 적용해서 재할당

# ========================
print("=== .upper() ===")

str3 = "abcdefg"
print(str3)  # abcdefg


str3 = str3.upper()  # ABCDEFG > 반환은 대문자인데, 값에 재할당은 X
print(str3)  # abcdefg > 기존 str3의 값인 소문자를 그대로 출력

# 앞으로 계속 대문자로 변환한 값을 사용하고 싶다면
# 변수에 재할당
# 변수 재할당에서 변수 스스로 부르는 것이 가능
# 재할당에서 변수 스스로 값을 부르려면 무조건 "재할당"이어야 함
str3 = str3.upper()


# 최초 변수 할당 시에는 저장된 값이 없어서
# 변수 스스로 값을 불러와 할당 불가능
# str4 = str4.upper()

print("=== 실습1 ===")
name = "ready"
print(name.upper())

name = "WARNING"
print(name.lower())

name = "kim chul soo"

# capitalize는 문자열의 첫 글자만 대문자로 변환
print(name.capitalize())  # Kim chul soo

# title은 띄어쓰기 기준으로 각 단어의 첫 글자들을 모두 대문자로 변환
print(name.title())  # Kim Chul Soo

# '를 사용한 경우 다른 단어로 인식
print("i'm full".title())  # I'm Full
print("i'm full".title())  # I'm Full

a = "Fault"
b = "FAULT"
print(a == b)
print(a.lower() == b.lower())

a = "ABC"
b = "abc"
c = "Abc"
print(a.isupper())
print(b.islower())
print(c.isupper())

print("=== 실습6 ===")

name = "Sensor_LOG.CSV"
low = name.lower()
print(low.startswith("sensor"))
print(low.endswith(".csv"))
print(name.endswith(".csv"))


# =====================
print("=== .strip() ===")

# 공백 제거
# .strip(): 앞과 뒤의 모든 공백 제거 (중간 띄어쓰기는 그대로 유지)
# .lstrip(): left(왼쪽) 공백만 제거
# .rstrip(): right(오른쪽) 공백만 제거

raw = "    정상       "
print(raw.strip())  # "정상"
print(raw.lstrip())  # "정상   "
print(raw.rstrip())  # "   정상"

# 문자열의 가운데 공백은 strip으로 지우지 못함
print("     정    상       ".strip())  # "정   상"

print(raw)  # "       정상    "
# strip은 재할당이나 새 변수에 할당하지 않는 이상 휘발

# strip으로 문자 제거
str4 = "===정상==="
print(str4.strip("="))  # 정상
# 인자로 전달한 양 끝의 =이 모두 지워짐

str5 = "=정상===="
print(str5.strip("="))  # 정상
# 갯수 상관없이 인자로 전달한 문자를 무조건 삭제
print(str5.strip("= "))
# strip 자체가 공백을 지우는 것이기 때문에
# 공백 상관없이 해당 문자열을 양 끝의 해당 문자열 삭제

str6 = "==정==상====="
print(str6.strip("="))  # 정==상
# 글자 중간에 있는 문자열은 건드리지 않음

# ================================
print("=== 체이닝 ===")

raw = "   NORMAL   "

# 체이닝 X
step1 = raw.strip()  # "NORMAL"
step2 = step1.lower()  # "normal"

# 체이닝 X, 기존 변수에 재할당
raw = raw.strip()  # "NORMAL"
raw = raw.lower()  # "normal"


# 체이닝 0
chain = raw.strip().lower()  # "normal"

# 기존 변수에 재할당도 가능
raw = raw.strip().lower()

# 변수에 할당하지 않고 사용 가능
print(raw.strip().lower())  # "normal"

str10 = "     Warning    "
print("[" + str10.lower() + "]")
print("[" + str10.lower().strip() + "]")
