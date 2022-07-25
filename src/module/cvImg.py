import cv2
import numpy as np
import matplotlib.pyplot as plt



def getImg():
    image_bgr = cv2.imread('../static/Mimg', cv2.IMREAD_COLOR)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(); plt.show()