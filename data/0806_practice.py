print("=== 실습 1 ===")
f = open("data/sample.txt", "r", encoding="utf-8")
print(type(f).__name__)
content = f.read()
print(content)

f.seek(0)

lines = f.readlines()
print(lines)

print(type(content).__name__)
print(type(lines).__name__)

f.close()

print("=== 실습 2 ===")

with open("data/sample.txt", "w", encoding="utf-8") as f:
    f.write("Python 파일 쓰기 실습\n")
    f.write("공부해야지...😿😿\n")

f = open("data/sample.txt", "r", encoding="utf-8")

content = f.read()
print(content)

f.close()

print("=== 실습 3 ===")

with open("data/sample.txt", "a", encoding="utf-8") as f:
    f.write("🐱🐱🐱😾\n")
    f.write("😾😾😾\n")
    f.write("살려줘🙀🙀🙀\n")

f = open("data/sample.txt", "r", encoding="utf-8")

content = f.read()
print(content)

f.close()

print("=== 실습 4 ===")

import csv

with open("data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

print("=== 실습 5 ===")

import csv

with open("data/result.csv", "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["고양이😻"])
    writer.writerow(["돼지 🐷"])
    writer.writerow(["유니콘 🦄"])
    writer.writerow(["부엉이 🦉"])
    writer.writerow(["판다 🐼"])

print("=== 실습 6 ===")

import csv

with open("data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    header = next(reader)

    result = []

    for row in reader:
        value = float(row[2])

        if value > 90:
            result.append(row)

with open("data/result.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for row in result:
        writer.writerow(row)

print("=== 실습 3 ===")

while True:
    try:
        num1 = int(input("첫 번째 숫자: "))
        num2 = int(input("두 번째 숫자: "))

        result = num1 / num2

        print("결과:", result)
        break

    except ValueError:
        print("숫자를 입력해주세요.")

    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
