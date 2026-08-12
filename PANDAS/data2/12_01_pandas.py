import pandas as pd
import os

print("=== 실습 1 ===")

filepath = os.path.join("PANDAS", "data2", "12_metro_small.csv")
df = pd.read_csv(filepath)
print(df.shape)


print("=== 실습 4 ===")

import pandas as pd

df = pd.read_csv(
    "PANDAS/data2/12_metro_small.csv",
    usecols=["측정시각", "오일온도", "가동상태"],
)
print(df.shape)
print(df.head(2))

print("=== 실습 5 ===")
import pandas as pd

filepath = "PANDAS/data2/12_metro_small.csv"
# df = pd.read_csv("아무거나주세요.csv") # FileNotFoundError
df = pd.read_csv(filepath)
print(df.shape)


print("=== 실습 6 ===")
# pandas/data/12_metro_compressor_semicolon.csv
# sep을 잘 사용해서 여러 컬럼이 얽히도록
# encoding 지정
# 모든 컬럼 다 읽지말고, "측정시각", "오일온도", "모터전류" 컬럼만 읽기

import pandas as np

filepath = "PANDAS/data2/12_metro_compressor_semicolon.csv"

df = pd.read_csv(
    filepath, sep=";", encoding="utf-8", usecols=["측정시각", "오일온도", "모터전류"]
)

print(df.shape)
print(df)
