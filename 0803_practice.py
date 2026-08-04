print("=== 실습 2 ===")


sensor = {"온도": 30, "습도": 80}

new_data = {"온도": 45, "압력": 150}

sensor.update(new_data)

del sensor["습도"]

print("갱신된 딕셔너리")

print("센서 수:", len(sensor))


print("=== 실습 3 ===")

sensor = {"온도": 80, "습도": 40, "압력": 100}

average = sum(sensor.values()) / len(sensor)

print("평균:", round(average, 1))

max_value = 0
max_sensor = ""

for name, value in sensor.items():
    if value > max_value:
        max_value = value
        max_sensor = name

print("최댓값 센서:", max_sensor, max_value)


print("=== 실습 6 ===")

equipment = {
    "1번 펌프": {"온도": 68, "압력": 82, "상태": "정상"},
    "2번 펌프": {"온도": 73, "압력": 91, "상태": "정상"},
    "3번 펌프": {"온도": 79, "압력": 87, "상태": "점검"},
}

print(equipment["2번 펌프"]["압력"])

for name, info in equipment.items():
    if info["상태"] == "점검":
        print(name, "점검필요")
