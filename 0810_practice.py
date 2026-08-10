print("=== 실습 1 ===")

import numpy as np

celsius = [20, 25, 30, 35]

celsius_array = np.array(celsius)

fahrenheit_array = celsius_array * 9 / 5 + 32

print(fahrenheit_array)

print("=== 실습 2 ===")

import numpy as np

values = np.linspace(0, 100, 5)
print("배열", values)
print("간격:", values[1] - values[0])

print("=== 실습 3 ===")

import numpy as np

time = np.arange(0, 10, 2)
print(time)

print("=== 실습 4 ===")

import numpy as np

sensor_data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("차원: ", sensor_data.ndim)
print("형태: ", sensor_data.shape)
print("개수: ", sensor_data.size)

print("=== 실습 5 ===")

import numpy as np

sensor_data = np.array([10.5, 20.7, 30.2, 40.9])
print("현재 자료형:", sensor_data.dtype)

int_data = sensor_data.astype(int)
print("정수 배열:", int_data)