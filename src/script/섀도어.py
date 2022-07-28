import time
from arduino_mk.constants import *
from arduino_mk import Arduino
# 섀도어
#1. 동아

ardu = ad.Arduino()

class 섀도어():

    # 윗점 없음
    # 
    점프 = "Alt"
    홀리심볼 = "1"
    기본공격 = "Cntrl"
    메익 = "Shift"
    범위기 = "f"

    # ardu.MOUSE_CMD

    def 동굴아랫쪽():
        while True:
            time.sleep(1)
            ad.move(300, 300)
            time.sleep(1)
            break
        print("섀도엉")

    
섀도어.동굴아랫쪽()