# 기존 배열의 모든 요소에 3을 곱한 갑슬 가진 새 리스트 작성
temps = [1, 5, 2, 7, 4, 8, 10, 3]
doubled = []

for t in temps:
    doubled.append(t * 3)

print(doubled)

# 조건에 맞는 값으로 새 리스트 만들기

# temps = [1, 5, 2, 7, 4, 8, 10, 3]
high = []
low = []

for t in temps:
    if t < 5:
        low.append(t)
    else:
        high.append(t)

print("high:", high)
print("low:", low)

# 복습) sort(): 원본 배열을 오름차순으로 정렬해줌
# 하지만 반환해주지 않기 때문에 print로 바로 찍으면 None 출력
print(low.sort())

# 정렬된 배열을 출력하고 싶다면 아래처럼
low.sort()
print(low)

print("=== 실습 4 ===")
temps = [32, 35, 31, 33, 28, 29, 30, 25]
a = []
for t in temps:
    if t > 30:
        a.append(t)
print(a)
print(len(a))


print("==========list 속의 list==========")

# 예시 1
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
## 표(행과 열의 형식)처럼 한 줄에 여러 데이터가 묶인 데이터, 가장 큰 대괄호를 행 / 내부의 대괄호를 열 로 취급한다.

print(rows[0])  # ["펌프", 0]
print(type(rows[0]))  # <class 'list'>

## 대괄호 속 내부의 대괄호 데이터 접근
print(
    rows[1][1]
)  # 32 >> [1[1]]이 아닌 [1][1]와 같이 이어서 코드를 써야 안에 있는 데이터로 접근이 가능하다.

# list 내부 list의 온도 값만 출력
for row in rows:
    print(row[0], "온도", row[1])  # 펌프 온도 25
## rows는 가장 바깥의 대괄호이고, row는 내부의 리스트들을 뜻한다. 따라서 row[1]이 25가 되는것이다.

# ======(실습)======

temps = [25, 32, 28, 35, 27, 31, 24, 33, 29, 36]
total = 0

# 전체 평균 구하기
for t in temps:
    total += t
print("전체 평균:", total / len(temps))

# 고온 데이터(30 초과)만 골라 새 리스트 만들기
hot = []
for t in temps:
    if t > 30:
        hot.append(t)

# 고온 개수 및 고온 평균 구하기
hot_total = 0
for h in hot:
    hot_total += h

print("고온 개수:", len(hot))
print("고온 평균:", hot_total / len(hot))