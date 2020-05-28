#1 임의로 지정한 숫자를 맞추는 게임

import random

random.seed(11)
goal = random.randint(0,100)
print(goal)

while True:
    reply = int(input("예상하시는 숫자는?"))
    if reply == goal:
        print("맞췄습니다")
        break
    else:
        if(reply > goal): print("크네요.")
        if(reply < goal): print("작아요.")

#2 극장예매시스템 (10자리 예매)


seatNum = 0
for seatNum in range(0,10):
    print(seatNum)
you = int(input("예약하고 싶은 자리 입력"))
if you == seatNum:
    print("그 자리가 예약되었습니다.")
else :
    if(you==seatNum) : print("그 자리는 예약되었습니다. 다른자리 예약좀")
