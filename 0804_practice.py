print("=== 실습 2 ===")


def sensor_data(motor, pump):
    print("모터:", motor, "도")
    print("펌프:", pump, "도")


sensor_data(65, 35)
print()
sensor_data(35, 65)

print("=== 실습 3 ===")


def sensor_data(motor, pump):
    print("모터", motor)
    print("펌프", pump)


sensor_data(pump=45, motor=82)

sensor_data(45, 82)

sensor_data(pump=45, motor=82)

print("=== 실습 5 ===")


def sensor_stat(values):
    min_value = min(values)
    max_value = max(values)
    total = sum(values)
    average = total / len(values)

    return min_value, max_value, total, average


sensor_values = [65, 80, 75, 90, 70]

min_value, max_value, total, average = sensor_stat(sensor_values)

print(min_value, max_value, average)
