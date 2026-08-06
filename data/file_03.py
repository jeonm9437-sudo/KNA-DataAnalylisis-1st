import os
import sys
import csv

csv_path = os.path.join("data", "result.csv")

# newline값을 지정하면 윈도에서 줄바꿈이 더 들어가는 오류를 고침
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])
