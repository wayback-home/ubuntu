# 객체지향 프로그래밍 1주차 예제 : 프로그램 작성, 컴퓨터공학과 2학년 1826052 최영서
# 1
print("hello")

# 2
import sys

if sys.argv[1] == "/?":
    print("이 프로그램에 대한 설명은...")
    print("이 프로그램에 대한 설명은...")
    print("이 프로그램에 대한 설명은...")
else:
    print("안녕하세요~" + sys.argv[1] + "님!!")

# 3
from datetime import datetime

print(datetime.now())
print("\n\n\n")

currenttime = datetime.now()

print("현재시간은", end=" ")
print(
    str(currenttime.hour)
    + ":"
    + str(currenttime.minute)
    + ":"
    + str(currenttime.second),
    end=" ",
)
print("입니다.")

print("\n" * 50)

import time

i = 0
while i < 5:
    currenttime = datetime.now()
    print("지금 시간은 ", end="")
    print(
        str(currenttime.hour)
        + ":"
        + str(currenttime.minute)
        + ":"
        + str(currenttime.second),
        end=" ",
    )
    print("입니다.")
    time.sleep(1)

    i += 1
