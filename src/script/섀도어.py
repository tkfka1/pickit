import re
import time
from script.arduino import Arduino
from script.constants import *
# from arduino import Arduino
# from constants import *
from random import random
# 섀도어
#1. 동아



# ad = Arduino()
# 섀도어
#1. 동아

# # 윗점 없음



# 섀도어


class 섀도어():
    global ad
    global myLoc
    global onRune
    global ad
    ad = 0
    myLoc = (0, 0)
    onRune = [False, (0, 0)]

    # 공격눌 = ad.press(LEFT_CTRL)
    # 공격떼 = ad.release(LEFT_CTRL)
    # 점프 = LEFT_ALT
    # 홀리심볼 = "1"
    # 기본공격 = "Cntrl"
    # 메익 = "Shift"
    # 범위기 = "f"


            


    # 잠푸잠푸공격
    def 잠푸잠푸공격(ad):
        # ad.점프
        ad.press(LEFT_ALT)
        time.sleep((0.1*random()))
        ad.release(LEFT_ALT)
        time.sleep(0.3*random())
        ad.press(LEFT_ALT)
        time.sleep(0.1*random())
        ad.release(LEFT_ALT)
        time.sleep(0.3*random())
        ad.press(LEFT_CTRL)
        time.sleep(0.1*random())
        ad.release(LEFT_CTRL)
        print(0.1*random())
        print("잠푸잠푸공격 1회차")


    def 동굴아랫쪽(arduino , myLoc, onRune , timer):  
        while True:
            time.sleep(2)
            섀도어.잠푸잠푸공격(arduino)
            break
        print("섀도엉" , myLoc, onRune ,timer)