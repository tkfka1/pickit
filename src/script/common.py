from script.arduino import Arduino
from script.constants import *
import time
from random import random


# 기본 연결
def 연결():
    global ad
    ad = Arduino()
    print("아두이노 연결완료")
    return ad

# 룬찾으러 가기
def 룬찾기(arduino ,myLoc , onRune ,timer):
    if onRune[0] == True:
        print("룬까러가장")
        if myLoc[0] == onRune[1][0]:
            arduino.releaseAll()
            # 위쪽
            if myLoc[1] == onRune[1][1]:
                arduino.releaseAll()
                arduino.press(" ")
                time.sleep(0.3*random())
                arduino.release(" ")
            else:
                if myLoc[1] > onRune[1][1]:
                    arduino.press(UP_ARROW)
                    time.sleep(0.1*random())
                    arduino.release(UP_ARROW)
                else:
                    arduino.press(DOWN_ARROW)
                    time.sleep(0.1*random())
                    arduino.release(DOWN_ARROW)
        else:
            if myLoc[0] > onRune[1][0]:
                arduino.release(RIGHT_ARROW)
                arduino.press(LEFT_ARROW)
            else :
                arduino.release(LEFT_ARROW)
                arduino.press(RIGHT_ARROW)

# 클릭