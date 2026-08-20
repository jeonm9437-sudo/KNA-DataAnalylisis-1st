print("=== 실습 1 ===")

import pandas as pd

df_log = pd.read_csv("data2/15_사출성형_로그.csv", encoding="utf-8")

print(df_log.isna().sum())

print("=== 위장 결측치 ===")
print("사출압력 0:", (df_log["사출압력"] == 0).sum())
print("스크루속도 -999:", (df_log["스크루속도"] == -999).sum())

print("=== 실습 2 ===")

import pandas as pd

df = pd.read_csv("data2/15_사출성형_로그.csv", encoding="utf-8")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

print("=== 실습 3 ===")

import pandas as pd

df_log = pd.read_csv("data2/15_사출성형_로그.csv", encoding="utf-8")

print((df["배럴온도"] == -999.0).sum())
print((df["스크루속도"] == -999.0).sum())
