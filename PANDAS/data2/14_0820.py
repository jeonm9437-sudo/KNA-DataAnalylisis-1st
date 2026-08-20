import pandas as pd

df_qc = pd.read_csv("data2/14_hydraulic_qc.csv", encoding="utf-8")
df_qc.info()

r1 = df_qc["지표07"].corr(df_qc["지표08"])
print(r1)  # -0.96908773235797 강한 음의 상관관계
print(r1.round(3))  # -0.969

cols = [
    "지표01",
    "지표02",
    "지표03",
    "지표04",
    "지표05",
    "지표06",
    "지표07",
    "지표08",
    "지표09",
    "지표10",
]
r2 = df_qc[cols].corr()
print(r2.round(2))


# =============================
print("=== 실습 3 ===")

import pandas as pd

df_qc = pd.read_csv("data2/14_hydraulic_qc.csv", encoding="utf-8")
df_qc.info()

# 전체 데이터의 지표07과 지표08 상관관계
r_all = df_qc["지표07"].corr(df_qc["지표08"])
print(r_all.round(3))  # -0.969

# 검사결과가 합격인 데이터 그룹의 지표07과 지표08 상관관계
df_qa = df_qc[df_qc["검사결과"] == "합격"]
r_qa = df_qa["지표07"].corr(df_qa["지표08"])
print(r_qa.round(3))  # 0.385

# 검사결과가 불합격인 데이터 그룹의 지표07과 지표08 상관관계
df_nqa = df_qc[df_qc["검사결과"] == "불합격"]
r_nqa = df_nqa["지표07"].corr(df_nqa["지표08"])
print(r_nqa.round(3))  # -0.998

# ================================
print("=== 실습 4 ===")

df = pd.read_csv("data2/14_equipment_sensor.csv", encoding="utf-8")
df.info()

# 라인(line)로 그룹을 나눠
# (temp)의 측정수(count).평균온도(mean).온도편차(agg) 요약 -> agg
report = df.groupby("line")["temp"].agg(["count", "mean", "std"]).round(2)

# 위 결과를 그대로 복사해서 보고서에 붙여넣으면 다른사람은 알아보기 힘듬
# 그래서 label 처리 (Pandas 권장사항)
report = (
    df.groupby("line")
    .agg(측정수=("temp", "count"), 평균온도=("temp", "mean"), 온도편차=("temp", "std"))
    .round(2)
)

print(report)

# 표 안에서도 심각한 정보를 먼저 보여주는 게 필요
# 이 경우 온도편차가 큰 경우가 심각한 정보라서 우선 나타나게 해주자
print("==============================")
print("라인별 통계")
print(report.sort_values("온도편차", ascending=False))

#        측정수   평균온도   온도편차
# line
# C라인    31  79.88  10.38
# A라인    54  76.86  10.18
# B라인    35  77.69   7.60

# 온도(temp)와 진동(vibration)의 상관계수(corr)를 구해 움직임 확인
print("==============================")
print("라인별 고장 건수")
r = df["temp"].corr(df["vibration"])
print(r.round(3))  # 0.345

# 고장(result == 고장) 행을 걸러 라인별 고장 건수까지 더해 우선 점검 대상 정리
df_bad = df[df["result"] == "고장"]
print(df_bad.head(2))


print("==============================")
print("라인별 고장 건수")
print(df_bad.groupby("line").size())
# A라인    16
# B라인     6
# C라인     6

# 15_01
print("=== 실습 1 ===")

import pandas as pd

df_log = pd.read_csv("data2/15_사출성형_로그.csv", encoding="utf-8")
print(df_log.describe())

# 설비 센서 데이터를 불러와 isna로 컬럼별 NaN 개수 세기
print(df_log.isna().sum())

# 조건 필터링으로 입력 0, 진동 -999 같은 위장 결측 갯수 세기
print((df_log["사출압력"] == 0.0).sum())

# ==========================================
import pandas as pd

df = pd.read_csv("data2/15_01_사출성형_공정.csv", encoding="utf-8")
print(df.shape)
df.info()

# ==========================================
# -999와 999 라는 값이 있다면 NaN으로 갯수 세기
print("======================================")
df = pd.read_csv(
    "data2/15_01_사출성형_공정.csv", encoding="utf-8", na_values=[-999, 999]
)
print(df.shape)
df.info()
print(df.describe())

print(df.isna().sum())
print(df.notna().sum())

# 각 컬럼별 NaN 갯수를 낸 Serise 대상으로 다시 합산한다면? -> 전체 NaN 갯수
print(df.isna().sum().sum())

# ===================================
print("=== 실습 2 ===")

import pandas as pd

df = pd.read_csv("data2/15_01_사출성형_공정.csv", encoding="utf-8")

# head.shape.info.describe로 결측 분위기 파악
# 처음 받은 데이터의 구조와 결측 분위기 파악

print(df.head())
print(df.shape)
df.info()

print(df.describe())

print("=== 실습 3 ===")

import pandas as pd

df = pd.read_csv("data2/15_01_사출성형_공정.csv", encoding="utf-8")

# 위장 결측이 있는 열을 조건 필터링으로 추출해 확인
print((df_log["배럴온도"] == -999.0).sum())
print((df_log["스크루속도"] == -999.0).sum())

print("=== 실습 4 ===")

import pandas as pd

df = pd.read_csv("data2/15_01_사출성형_공정.csv", encoding="utf-8")

# insa와 sum으로 컬럼별 결측 개수를 변수에 담기
counts = df.isna().sum()

ratio = (counts / len(df) * 100).round(1)
print(ratio)

# 결측이 있는 컬럼만 골라 개수와 비율을 나란히 정리
# 기존 데이터 프레임들을 합쳐서 새로운 df만들기
table = pd.DataFrame({"개수": counts, "비율": ratio})
print(table[table["개수"] > 0])

# ===========================
print("=== 실습 5 ===")

# 결측 비율을 내림차순 정렬해 가장 심한 컬럼 확인
print(ratio.sort_values(ascending=False).head(3))

# 방향을 가로(행)으로 바꿔 행마다 결측 개수 세기
# NaN합산 대상을 Y축 방향별로 컬럼별로 하는 게 아니라
# X축 방향별로 각 row마다 처리하기
df_axis = df.isna().sum(axis=1)
print(f"결측없는 행 {(df_axis == 0).sum()}개")
print(f"결측없는 행 {(df_axis > 0).sum()}개")

# 결측이 많은 부실 행만 조건으로 골라내기
print(f"결측 5개 이상있는 행 {(df_axis >= 5).sum()}개")