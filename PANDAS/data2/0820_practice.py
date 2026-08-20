print("=== 실습 1 ===")

import pandas as pd

df = pd.read_csv("data2/14_hydraulic_qc.csv", encoding="utf-8")

print(df[["지표01", "지표02", "지표03", "지표04"]].corr().round(3))

print("=== 실습 2 ===")

import pandas as pd

df = pd.read_csv("data2/14_hydraulic_qc.csv", encoding="utf-8")

feat = ["지표%02d" % i for i in range(1, 11)]
print(feat)

cm = df[feat].corr().round(3)
print(cm)

for i in range(len(cm.columns)):
    print(f"{i}번째 컬럼 이름 {cm.columns[i]}")
    for j in range(i + 1, len(cm.columns)):
        c = cm.iloc[i, j]
        if abs(c) > 0.4:
            if abs(c) > 0.4:
                print(
                    f"[i]번째 칼럼 [com.columns[i]과 비교할 {cm.columns[j]}] : {c} -> 강한 상관계수"
                )

print("=== 실습 3 ===")

import pandas as pd

df = pd.read_csv("data2/14_hydraulic_qc.csv", encoding="utf-8")

print("전체:", df["지표07"].corr(df["지표08"]).round(3))

df_pass = df[df["검사결과"] == "합격"]
print("합격:", df_pass["지표07"].corr(df_pass["지표08"]).round(3))

df_fail = df[df["검사결과"] == "불합격"]
print("불합격:", df_fail["지표07"].corr(df_fail["지표08"]).round(3))
