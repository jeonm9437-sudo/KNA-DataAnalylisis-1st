# 표준 라이브러리의 os 모듈 활용
import os

current_working_directory = os.getcwd()
print(current_working_directory)

# 현재 작업디렉토리의 파일 목록 가져오기
file_list = os.listdir()
for file_name in file_list:
    print(file_name)

# 파일이 존재하는지 알아보기
# 운영체제(윈도/맥/리녹스)마다 경로를 나타내는 방법이 달라서
# 상황에 맞게 경로문자열을 만들어주는 os 함수 만들기
path = os.path.join("data", "08_press.csv")


# 실제로 경로문자열을 따라서 찾아가면
# 해당 파일이 있는지 알아보기: True/False
if os.path.exists(path):
    print(f"파일 있음: {path}")
