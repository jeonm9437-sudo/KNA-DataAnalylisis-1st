# replace() : 특정 글자, 단어를 다른것으로 바꾸기
# replace(" ","")는 중간 공백까지 모두 제거
# 전화번호 하이픈도 replace("-")로 제거
# strip이 못하던 중간 공백 해결

# ex
text = "정 상 가 동"
text = text.replace(" ", "")
print(text)
phone = "010-1234-5678".replace("-", "")
print(phone)

name = "설비 정상 가동".replace("정상", "점검")
print(name)

# split() : 정해진 구분자로 문자열을 여러 조각으로 나눠줌
# 구분자가 나오는 자리마다 잘라서 리스트로
# 슬라이싱은 위치로 자름, split은 구분자로 나눠줌
# 조각들은 리스트에 순서대로
# 괄호를 비우면 공백을 기준으로 나눔

drinkgs = "에스프레소 아메리카노 카페라테"
print(drinkgs.split())
print(drinkgs.split())

s = "a, b, c, d"
print(s.split(","))
print(s.split(",", 1))

# join() : 리스트의 여러 조각을 하나의 문자열로 합치기
# 순서가 독특. 구분자가 앞에 옴
parts = ["2025", "01", "15"]
print("-".join(parts))

# print(값, 값, sep="구분자")로 출력할 때 값들 사이에 구분자 넣기
print("2025", "01", "15", sep="-")
print("2025", "01", "15", sep=",")

# split은 문자열 > 리스트, join은 리스트 > 문자열 (정반대)
# 둘을 묶으면 구분자를 통째로 교체 가능
# 문법 - 문자열.split() / 구분자.join()

text = "사과,배,감"
parats = text.split(",")
joined = "/".join(parts)
print(text)

raw = "2025/01/15"
parts = raw.split("/")
print("-".join(parts))
# 나누기(split)->정리(strip/lower)->합치기(join)

raw = "1, NORMAL, 25.3"
parts = raw.split(",")
status = parts[1].strip().lower()  # 체이닝 사용
print(status)

# replace는 문자열, split은 리스트, join은 문자열
# 원본은 안 바뀌고 결과를 변수에 다시 받기
# join 대상은 모든 문자열 (숫자는 str로)

# 메서드              용도                결과
# replace(A, B) - A를 B로 바꾸거나 제거 - 문자열
# split() - 공백으로 나누기 - 리스트
# split(",") - 구분자로 나누기 - 리스트
# 구분자.join() - 조각 합치기 - 문자열

# f-string : 문자열 안에 변수 값을 바로 끼워 넣는 출력
# 따옴표 앞에 f, 변수 자리에 중괄호{변수}
# f"설비{code}점검"은 "설비 EQP-001 점검"
# 완성될 문장 그대로 쓰고 변수만 중괄호 표시

name = "홍길동"
age = 25
print(f"{name}님은 {age}살입니다")
code = "EQP-001"
print(f"설비 {code} 점검 완료")

name = "PUMP_A"
temp = 87
print(f"설비 {name}, 온도 {temp}도")
# f-string 안에서는 숫자를 str로 안 바꿔도 끼워짐
# f-string 안에서 계산
hour = 8
print(f"{hour*60}")

# f-string 안에서 계산
a = 80
b = 91
c = 90
print(f"평균 {(a + b + c) / 3}")

# f-string 소수점 자리 지정
# 중괄호 안에 :.2f를 붙여 소수점 자릿수 지정
# {value:.2f}는 소수점 둘째 자리까지 (자동 반올림)
# :.1f는 첫째, :3f는 셋째자리. 측정값, 평균, 비율 정리에 유용

# EX)
value = 25.34567
print(f"측정값 {value}")
print(f"측정값 {value:.2f}")
print(f"측정값 {value:.1f}")

a = 87.456
print(f"{a:.1f}, {a:.2f}")

# 텍스트 정리 도구
# 만들기,출력 - 따옴표,print,f-string, 형변환
# 꺼내기 - 인덱싱, 슬라이싱, split
# 확인, 다듬기 - len, in, find / strip, lower, replace, join
# 텍스트 정리 : 공백 제거 -> 통일,치환 -> 나누기 -> 정리 -> 합치기

rate = 87.456
print(f"{rate:.1f}")
print(f"{rate:.2f}")

print("=== 실습 4 ===")
raw = " 5, sensor_2, WARNING, 0.78912"
parts = raw.strip().split(",")
sid = parats[1].strip()
status = float(parts[3].strip())
value = float(parts[3].strip())
print(f"[센서 {sid} 상태 {status}, 측정값 {value:.2f}]")

# 리스트 만들기와 출력
# 숫자 리스트
temps = [25, 26, 24, 28, 27]
print(temps)

# 글자 리스트
machines = ["펌프", "모터", "압축기"]
print(machines)

# 리스트는 담는 값의 종류 안가림
# 숫자와 글자, 참거짓 값을 한 리스트에 섞어 담기 가능
temps = [25, 26, 24, 28, 27]
print(len(temps))
results = []
print(len(results))

print("=== 실습 1 ===")
temps = [25, 26, 24, 27, 26]
print(temps)
print(len(temps))
empty = []
print(len(empty))

# 인덱스[] - 순서로 값 찾기
# 인덱스는 첫 번째 값이


print("===복습===")
for i in range(5, 0, -1):
    print(i)

n = int(input("몇 번 반복할까요? "))
for i in range(n):
    print("반복 중...")

for i in range(3):
    print("현재 i:", i)


for i in range(3):
    print("반복")
print("끝")

n = int(input("끝 숫자 N을 입력하세요: "))
for i in range(1, n + 1):
    print(i)
for i in range(2, n + 1, 2):
    print(i)
for i in range(n, 0, -1):
    print(i)

print("===")
# if문의 기본 구조
temp = 85
if temp > 80:
    print("온도 주의")
print("측정 종료")

# 콜론은 여기부터 이 조건에 속하는 코드 시작이라는 신호
# if, elif, else 모두 콜론으로 끝나는 공통 규칙
# 그 아래 들여 쓴 코드 한 덩어리가 코드 블록
# 조건 판단 설계 3단계(상황파악 -> 조건 정의 -> 결과 지정)

print("== 실습 1 ==")
age = int(input("나이를 입력하세요: "))
if age >= 19:
    print("성인입니다")
else:
    print("미성년자입니다")

# else로 나머지 경우 처리
# else는 if 조건이 거짓일 때 실행할 코드를 담음
# else는 조건식을 따로 쓰지 않는다
# if 와 else 중 항상 하나만 실행

# 예)
score = 75
if score >= 60:
    print("합격")
else:
    print("불합격")

# elif는 갈림길이 셋 이상일 때 중간 조건을 추가
# 앞 조건이 거짓일 때만 elif 조건을 검사

# if - elif - else 전체구조
score = 82
if score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
else:
    print("미흡")

# 논리 연산자 not
# not은 참을 거짓, 거짓을 참으로 뒤집음
# "~가 아닐 때"를 표현
# and, or 섞을 때는 괄호로 범위를 분명히

temp = 45
if temp >= 20 and temp <= 60:
    print("정상 범위")
if 20 <= temp <= 60:
    print("정상 범위")
    