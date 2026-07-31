# =======================================
print("==========tuple,set==========")

# 기존 list의 가독성과 호환성이 불편해 tuple과 set이 생김.
# 기본 구성 : ( ,)으로 데이터를 묶고 , 으로 여러형의 자료형의 값을 저장(, 는 마지막 값에 꼭 붙여야 한다.)
# 짝 지어진 값을 하나로 묶을 때 사용 가능한 자료형

# 예시 1
sensor = ("모터 온도", 78)  # 일반
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # class <tuple>

sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = (
    "모터온도",
    78,
)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'int'>

sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = ()  # 괄호 있고, 끝에 쉼표 없고, 값도 안담김
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# tuple이 판단 기준
## tuple이 되는 기준은 기본 구성 요소인 ( )와 ,의 여부이고 이 두 개의 구성 요소 중 , 만 있더라도 tuple이 만족함.
## 예외로 () 안에 아무런 값이 없다면 값을 구분 지을 필요가 없기에 tuple의 기본 구성 요소인 ()으로 tuple이 만족함.

# 요소(값)의 개수
## 요소 2개 이상 : 쉼표가 있다면 tuple
## 요소 1개 : 쉼표 여부(끝에)
## 요소 0개 : ()의 여부

# 예시로 보는 tuple의 기준
## (1) >> int
## (1,) >> tuple

# tuple의 index
sensor = ("모터 온도", 78)
print(sensor[0])

# tuple의 slice(ing)
s = (
    "a",
    "b",
    "c",
    "d",
    "e",
)
print(s[1:4])  # type : class <tuple>

# tuple unpacking : tuple에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언 할 떄, a,b,c = "a","b","c" 의 형태를 따른다.
# tuple에 적용 시켜 보기
unpacking = (
    1,
    2,
    3,
)  # 각각 변수 one, 변수 two, 변수 three로 선언할려고 한다.
# unpacking = one, two, three >> 이 줄의 의미는 one two three의 변수를 unpacking에 할당하는 의미 따라서,
one, two, three = unpacking  # 으로 = 기준으로 좌 우를 바꾸면 가능하다.
print("one:", one)
print("two:", two)
print("three:", three)

# 응용) list unpacking 가능할까?
one, two, three, four = [11, 22, 33, 44]
print("one:", one)
print("two:", two)
print("three:", three)
print("four:", four)


# tuple 과 list의 가장 큰 차이점은 수정 가능성이다.
## tuple은 절대 수정이 불가하다. >> 이후 원본의 변경을 막는 기능이다.
## 따라서 내림차순, 오름차순, 뒤집기 등등 원본에 영향을 주는 메서드는 사용이 불가하다.(Error 발생)

# ====================

tup = ("normal", "normal", "warning", "normal", "warning")

# 튜플의 길이
print(len(tup))  # 5

# 특정 값의 갯수 세기
print(tup.count("warning"))  # 2
print(tup.count("Warning"))  # 0

# 특정 값이 처음 나온 인덱스
print(tup.index("warning"))  # 2
# 찾고자 하는 값이 없으면 Error 발생
# print(tup.index("Warning"))  # ValueError: tuple.index(x): x not in tuple


# ===========================

# 튜플 리스트
# 리스트 안에 튜플을 담은 것을 표현
# for문으로 리스트를 사용해서
# 리스트 내부의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을
# 변수에 바로 할당해서 접근

hour_13 = [
    ("모터온도", 77),
    ("모터진동, 0.2"),
    ("모터압력", 91),
]

now = 0

# for name, value in hour_13: # 오류떠서 나중에 코드보고 확인해보기
#     now += 1
#     print(now, "번째 반복")
#     print("name:", name, "value", value)

# ===================

temps_13 = [
    ("qox_001", 81),
    ("qox_002", 88),
    ("qox_003", 95),
    ("qox_004", 89),
]

warning = 90

for name, temp in temps_13:
    if temp >= warning:
        print("경고", name, "설비 온도 이상")


# 리스트 안의 튜플 값 갯수가 늘어나면 for문에서 변수를 여러 개 작성하면 됨

tup_list = [("일", "one", 1, "1"), ("이", "two", 2, "2")]


# for문에서도 언배킹 할 때는 무조건 튜플의 값 개수와
# for문의 변수 갯수 통일
# 통일하지 않을 경우 Error 발생
for kor_str, eng_str, num, num_str in tup_list:
    print("kor_str:", kor_str, "eng_str:", eng_str, "num_str:", num, num_str)

# ====================

# 튜플 리스트 정렬
# sorted()를 사용하여 튜플이 특정 값 기준으로 리스트를 정렬

temps_13 = [
    (81, "qox_001"),
    (88, "qox_002"),
    (95, "qox_003"),
    (89, "qox_004"),
]

hot = sorted(temps_13, reverse=True)
print(hot)

print("=== 실습 1 ===")
sensor = ("모터온도", 78)
print(sensor)
print(sensor[0])
print(sensor[1])
name, value = sensor
print(name, value)

print("=== 실습2 ===")
sensor = [
    ("모터온도", 76),
    ("회전속도", 160),
    ("펌프압력", 90),
    ("유량", 42),
]
for name, value in sensor:
    print(name, value)
limit = 90
for name, value in sensor:
    if value > limit:
        print(name, "경고")

print("=== 실습 3 ===")
sensor = [
    ("모터온도", 78, (3, 5)),
    ("베어링진동", 0.5, (7, 2)),
    ("펌프압력", 95, (4, 8)),
]
for name, value, pos in sensor:
    x, y = pos
    print(name, "위치:", x, y)
for name, value, pos in sensor:
    x, y = pos
    if x <= 5:
        print(name, "1구역")

  