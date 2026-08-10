print("=== 실습 1 ===")

file = None

try:
    file = open("test.txt", "w", encoding="utf-8")
    file.write("센서 데이터 저장")

    number = 10 / 0

except ZeroDivisionError:
    print("오류가 발생했습니다.")

finally:
    if file is not None:
        file.close()
        print("파일이 안전하게 닫혔습니다.")

print("=== 실습 2 ===")
values = [
    "123.45",
    "25.6",
    "고양이",
    "30.5",
    "45.2",
    "abc",
    "18.7",
    "52.1",
    "27.8",
    "33.3",
    "잘못된값",
    "41.5",
    "22.4",
    "38.9",
    "19.8",
    "55.6",
    "31.2",
    "error",
    "28.5",
    "47.3",
]

total = 0

for value in values:
    try:
        value = float(value)
        total += value

    except ValueError:
        print("잘못된 데이터:", value)
        continue

print("정상 데이터 합계:", total)
