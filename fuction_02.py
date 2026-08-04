# "================================================="
print("==============매개변수=================")

# 간단한 인사말을 함수로 만든다고 가정하면, 사람마다 인사말을 만들어야 하기때문에
# 코드의 반복이나, 함수가 길어질 수 밖에 없다.
# 해결책은 하나의 함수에서 다양성을 제공할 수 있어야하고, 이것이 매개변수이다.


# 예제 1)
def say_hi(name):
    print(f"안녕하세요, {name}")


say_hi("Ned")
say_hi("Tuna")
## name이 이때 매개변수로 작용을 한다.


# 예제 2)
def check(name):
    print(f"{name} 장비의 점검을 시작합니다.")


check("압축기A")
check("펌프B")


# 예제 3) 매개 변수가 2개 이상인 함수
# STEP 1
def calc_sum():
    number_a = 1
    number_b = 2
    total = number_a + number_b
    print(f"{number_a}+{number_b}={total}")


calc_sum()

# ================================================
# STEP 2


def calc_sum(number_a, number_b):
    # number_a = 1
    # number_b = 2
    total = number_a + number_b
    print(f"{number_a}+{number_b}={total}")


calc_sum(1, 2)


# 매개변수가 2개 이상인 예제 - 장비 이름과 온도 정보 출력
def report(name, temp):
    # name = "압축기A"
    # temp = 75.3
    print(f"{name}의 온도는 {temp}도 입니다.")


report("압축기A", 75.3)
report("펌프B", 85.2)

# 엉뚱하게 호출
report(35.2, "보일러C")
# 첫 번째 매개변수는 무조건 name이 되고,
# 두 번째 매개변수는 무조건 temp가 되니까
# 원하지 않는 결과가 나올수도 있다.

# 매개변수가 부족하거나 더 있으면? TypeError: report() missing 1 required positional argument: 'temp'
# reprot("압축기A", 75.3, "가동중")
# reprot("펌프B")


# 키워드 인자
def reprot_keywords(name, temp):
    print(f"{name}의 온도는 {temp}도 입니다.")


# 키워드 인자 없이 호출
reprot_keywords("펌프A", 37.4)
reprot_keywords(37.4, "펌프A")  # 이 경우는 문제 발생

# 키워드 인자 사용해 호출 : 순서 바꿔 호출해 생기는 문제 근본 차단
reprot_keywords(name="펌프A", temp=37.4)
reprot_keywords(temp=37.4, name="펌프A")


# ================================
# 반환값


def add(a, b):
    total = a + b
    # a = 1 # 주석처리된 애들은 위에 total로 함축가능
    # b = 2
    # # total = a + b
    return total


print(add(1, 2))
print(add(11, 224))
print(add(13, 20))

# 여러번 같은 결과를 호출해야 한다면
# 차라리 변수에 담아서 쓰기
result = add(1, 2)
print(result + 1)
print(result + 2)
print(result + 3)


# 평균 내는 함수 만들기
def calc_average(a, b):
    return (a + b) / 2


avg = calc_average(75.3, 88.0)
print(f"평균 온도: {avg}")


# 여러 값을 한 번에 반환하기
# 다음의 함수는 배열을 받아서 그 안의 최소값과 최대값을 동시에 return한다
def calc_min_max(values):
    minmum = min(values)  # 배열 안의 최소값을 찾아 minmum에 담기
    maximum = max(values)  # 배열 안의 최댓값을 찾아 maximum에 담기


target_list = [1, 2, 3, 4, 5]
result = calc_min_max(target_list)
print(result)  # 튜플인 것을 확인

# 반환값을 언패킹으로 받기
# 함수의 결과를 받는 순간에
# 결과 튜플의 내용을 풀어서
# 개별 변수에 담아 사용하기
# result_min, result_max = calc_min_max(target_list) # 😿😿😿😿Error 떠서 나중에 확인해보기
# print("최소값" + str(result_min))
# print("최대값" + str(result_max))

# return 반환값이 없는 함수를 호출해놓고
# 결과를 어디에 담겠다고 하면, 담기는 값은 None이 됨


def say_greet():
    print("만나서 반갑습니다")
    return


greet = say_greet()
print(greet)  # None

print("=== 실습 5 ===")
# 내장 함수 min(), max(), sum(), len() 활용