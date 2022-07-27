import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time

# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']


def TM_CCOEFF():
    img_rgb = cv.imread('src/static/img/temp.png')
    x=0; y=0; w=320; h=250
    roi = img_rgb[y:y+h, x:x+w]
    img2 = roi.copy()
    img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    template = cv.imread('src/static/img/myloc.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF)
    threshold = 0.9
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    loc = np.where( res < threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    print(pt, pt[0] + w, pt[1] + h , w , h)
    cv.imshow('img_rgb', img_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()

def TM_CCOEFF_NORMED():
    img_rgb = cv.imread('src/static/img/temp.png')
    x=0; y=0; w=320; h=250
    roi = img_rgb[y:y+h, x:x+w]
    img2 = roi.copy()
    img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    template = cv.imread('src/static/img/myloc.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    # 임계값 설정
    threshold = 0.95
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    
    # 높은값 좌표 출력
    if  threshold > max_val:
        print("없음")
    else:
        print("좌표는" , max_loc, "정확도", max_val)
    # loc = np.where( res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #     print(pt)
    # print(pt, pt[0] + w, pt[1] + h , w , h)
    # print(loc)
    # cv.imshow('img_rgb', img_rgb)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

def TM_CCORR():
    img_rgb = cv.imread('src/static/img/temp.png')
    x=0; y=0; w=320; h=250
    roi = img_rgb[y:y+h, x:x+w]
    img2 = roi.copy()
    img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    template = cv.imread('src/static/img/myloc.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCORR)
    threshold = 0.9
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    # loc = np.where( res < threshold)
    # for pt in zip(*loc[::-1]):
    #     cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    # print(pt, pt[0] + w, pt[1] + h , w , h)
    # cv.imshow('img_rgb', img_rgb)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

def TM_CCORR_NORMED():
    img_rgb = cv.imread('src/static/img/temp.png')
    x=0; y=0; w=320; h=250
    roi = img_rgb[y:y+h, x:x+w]
    img2 = roi.copy()
    img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    template = cv.imread('src/static/img/myloc.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCORR_NORMED)
    threshold = 0.9999
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    loc = np.where( res > threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print(pt, pt[0] + w, pt[1] + h , w , h)
    cv.imshow('img_rgb', img_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()

def TM_SQDIFF():
    img_rgb = cv.imread('src/static/img/temp.png')
    x=0; y=0; w=320; h=250
    roi = img_rgb[y:y+h, x:x+w]
    img2 = roi.copy()
    img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    template = cv.imread('src/static/img/myloc.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_SQDIFF)
    threshold = 0.9
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    loc = np.where( res < threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print(pt, pt[0] + w, pt[1] + h , w , h)
    cv.imshow('img_rgb', img_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()

def TM_SQDIFF_NORMED():
    img_rgb = cv.imread('src/static/img/temp.png')
    x=0; y=0; w=320; h=250
    roi = img_rgb[y:y+h, x:x+w]
    img2 = roi.copy()
    img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    template = cv.imread('src/static/img/myloc.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_SQDIFF_NORMED)
    threshold = 0.001
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    loc = np.where( res < threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print(pt, pt[0] + w, pt[1] + h , w , h)
    cv.imshow('img_rgb', img_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()

start = time.time()
TM_CCOEFF_NORMED()
# TM_CCORR_NORMED()
end = time.time()
print(end - start)