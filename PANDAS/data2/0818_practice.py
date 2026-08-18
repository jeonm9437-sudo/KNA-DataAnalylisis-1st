print("=== 실습 1 ===")

import pandas as pd

df = pd.read_csv("PANDAS/data2/14_hydraulic.csv", encoding="utf-8")
df.info()
print(df.head(3))

print(df["밸브상태"].value_counts())

print(df["운전부하"].value_counts())

print("=== 실습 2 ===")

df_qc = pd.read_csv("PANDAS/data2/14_hydraulic_qc.csv", encoding="utf-8")
df_qc.info()
print(df_qc.head(3))

print(df_qc["검사결과"].value_counts())

print(df_qc["검사결과"].value_counts(normalize=True))

print(df_qc["검사결과"].value_counts(normalize=True).round(1))

print("=== 실습 3 ===")

import pandas as pd

df_qc = pd.read_csv("PANDAS/data2/14_hydraulic_qc.csv", encoding="utf-8")
df_qc.info()
print(df.head(3))
print(df["진동"].max())
print(df["진동"].min())

band = pd.cut(df["진동"], bins=[0.0, 0.6, 0.7, 10.0])
print(band.value_counts())
print(band.value_counts(normalize=True).round(3))

print("=== 선택문제 1 ===")

import pandas as pd

df = pd.read_csv("PANDAS/data2/students_groupby_practice.csv")

print("전체 학생 수: ", len(df))

# 2번
print(df.groupby("학년").size())

# 3번
print(df.groupby(["학년", "반"]).size())
