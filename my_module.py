print("=== 실습 1 ===")


def test():
    return 4.05


import my_module

print(my_module.test())

from my_module import test

print(test())

import my_module as mm

print(mm.test())


print("=== 실습 2 ===")

import random
import math

sensor_value = random.randint(1, 100)
print("센서값:", sensor_value)

result = math.sqrt(sensor_value)
print("제곱근:", result)


print("=== 실습 3 ===")
import os

current_path = os.getcwd()
print("현재 경로:", current_path)

files = os.listdir(current_path)
for file in files:
    if file.endswith(".csv"):
        print(file)


print("=== 실습 4 ===")

import os

folder = "."
filename = "test.txt"
path = os.path.join(folder, filename)

if os.path.exists(path):
    print("파일있음")
else:
    print("파일없음")


print("=== 실습 5 ===")
import os
from datetime import datetime

files = os.listdir(".")
file_count = len(files)
now = datetime.now()

print(f"파일 {file_count}개, 점검 시각 {now}")
