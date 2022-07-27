import cv2
import numpy as np

def imgLocation(img):
    x=0; y=0; w=320; h=250
    roi = img[y:y+h, x:x+w]
    img2 = roi.copy()

    template = cv2.imread('src/static/img/myloc.png')
    res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    threshold = 0.8
    loc = np.where(res>threshold)
    print(min_val, max_val, min_loc, max_loc)   # 이미지 위치 출력
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img2, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv2.imwrite('res.png',img2)

def mapleCheck():
    img = cv2.imread('src/static/img/temp.png')
    imgLocation(img)

mapleCheck()