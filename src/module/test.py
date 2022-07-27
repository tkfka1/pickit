import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time

start = time.time()

img_rgb = cv.imread('src/static/img/temp.png')
x=0; y=0; w=320; h=250
roi = img_rgb[y:y+h, x:x+w]
img2 = roi.copy()
img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
template = cv.imread('src/static/img/myloc.png',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

print(pt, pt[0] + w, pt[1] + h , w , h)

end = time.time()
print(end - start)