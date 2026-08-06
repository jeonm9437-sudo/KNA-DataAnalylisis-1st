# 트레이스백으로 에러 읽기

# ValueError: 글자를 숫자로 변환 요구 - 당연히 실패
# temp = int("스물") # ValueError: invalid literal for int() with base 10: '스물'

# 정상
temp = int("20")
print(temp)

print("=" * 20)

# ZerodivisionError : 숫자는 0으로 나눌 수 없음
# result = 10 / 0 # ZeroDivisionError: division by zero


# 정상
result = 10 / 3
print(result)

# NameError : 그런 이름도 있었어요? 라는 뜻의 에러
# hello() # NameError: name 'hello' is not defined. Did you mean: 'help'?
