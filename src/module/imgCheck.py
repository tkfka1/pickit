import cv2
import numpy as np
from matplotlib import image, pyplot as plt
import time


# 내위치 이미지 'src/static/img/myloc.png' 4x4
template = 'src/static/img/myloc.png'

# 미니맵 서치 (TM_CCOEFF_NORMED)
def minimapLoc(img , threshold , x , y , w , h): 
    img_rgb = img
    roi = img_rgb[y:y+h, x:x+w]
    img2 = roi.copy()
    img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('src/static/img/myloc.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # 높은값 좌표 출력
    if  threshold > max_val:
        result = False
        # print("없음")
    else:
        # print("좌표는" , max_loc, "정확도", max_val)
        result = max_loc
    return result

# 룬 서치 (TM_CCOEFF_NORMED)
def runeLoc(img , threshold , x , y , w , h): 
    img_rgb = img
    roi = img_rgb[y:y+h, x:x+w]
    img2 = roi.copy()
    img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('src/static/img/runeloc.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # 높은값 좌표 출력
    if  threshold > max_val:
        result = False
        # print("없음")
    else:
        # print("룬좌표는" , max_loc, "정확도", max_val)
        result = max_loc
    return result

    



def mapleTest(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # minimapLoc(image, template , 0.95)

# start = time.time()
# mapleCheck()
# end = time.time()
# print(end - start)
