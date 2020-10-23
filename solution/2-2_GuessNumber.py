"""
숫자 맞추기 게임 프로그램
- 숫자 하나를 입력
- 맞췄는지, 안 맞췄는지 출력 (True 혹은 False)
- 랜덤 숫자와 나의 숫자 출력
"""

import random

rNumber = random.randrange(1,10)
myNumber = int(input("어떤 숫자일까요?? : "))
print(rNumber is myNumber) # print(rNumber == myNumber)도 가능합니다.
print(f"랜덤 숫자 : {rNumber}, 나의 숫자 : {myNumber}")