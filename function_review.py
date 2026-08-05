# 함수의 기본 예제
def say_hello():
    pass  # 아무일도 안한는 코드


def say_hi():
    print("안녕하세요")


# 함수는 선언된(def) 후에 호출되어야 한다
say_hi()


# 매개변수를 사용하면 더 다양한 일을 할 수 있음
def show_hello(name):
    # name = "Ned"
    print(f"안녕하세요, {name}")


show_hello("Ned")
show_hello("Tuna")
show_hello("Layla")


# 매개변수는 여러 값을 받을 수 있고
def show_hi(name, message):
    # message = "반갑습니다"
    print(f"{message}, {name}")


say_hi("Ned", "안녕하세요")
say_hi("Tuna", "반갑습니다")


# 매개변수에는 따로 안알려주면 기본값을 적용할 수도 있음
def show_greeting(name, message="안녕하세요"):
    print(f"{message}, {name}")


show_greeting("Layla")
show_greeting("Jake", message = "Hello")