from itertools import cycle
import multiprocessing as mp
import queue
import threading
import time

from cv2 import imshow
from matplotlib import pyplot as plt
from module.camera import Camera
import module.handle as hd
import module.imgCheck as ic
import module.configParser as cp
import cv2
import numpy
import win32gui
from threading import Thread
import tensorflow as tf
import numpy as np
from PIL import ImageGrab

# 캡쳐 상태, 주기
global capStat
capStat = True , 0.5
# 핸들값
global hwnd
hwnd = 0
# 핸들 상태 , 주기
global handleStat
handleStat = True , 2
# 위치 상태 , 주기
global locationStat
locationStat = True , 2
# 룬 상태 , 주기
global runeStat
runeStat = True , 2
#미니맵 서치사이즈
global mapSize
mapSize = 0, 0, 320, 250
#매크로 상태
global statM1
global statM2
statM1 = False
statM2 = False
global myLoc
myLoc = (0, 0)
global runeLoc
runeLoc = (0, 0)
global onRune
onRune = False , (0, 0)
  

def init():
    global capStat
    global handleStat
    global locationStat
    global runeStat
    global mapSize
    config = cp.config_read()
    capStat = config[4] , config[5]
    handleStat = config[6] , config[7]
    locationStat = config[8] , config[9]
    runeStat = config[10] , config[11]
    mapSize = config[12] , config[13] , config[14] , config[15]


def macro():
    print("macro")

def test():
    print("asa")

def start():
    global capStat
    global handleStat
    global locationStat
    global runeStat
    global mapSize
    global statM1
    global statM2
    statM1 = True
    statM2 = True


    init()
    print("시작합니다.")
    # 프로세스 메이플 핸들 가져오기 및 켜졌나 확인
    if Camera.hwndPrint() == 0:
        print("메이플 실행 안됨")
    else:
        print("프로세스 가져오기")
        print(Camera.hwndPrint())
        Camera.startCap(capStat[0], float(capStat[1]))
        Camera.startHandle(handleStat[0], int(handleStat[1])/float(capStat[1]))
        Camera.startLoc(locationStat[0], int(locationStat[1])/float(capStat[1]))
        Camera.startRune(runeStat[0], int(runeStat[1])/float(capStat[1]))
        Camera.startMap(mapSize[0], mapSize[1], mapSize[2], mapSize[3])


        # 쓰레드
        th1 = Thread(target=work1, name='th1')
        th2 = Thread(target=work2, name='th2')
        th1.start()
        th2.start()
        th1.join()
        th2.join()

        # # 매크로 시작
        # while statM:
        #     Loc = Camera.getLoc()
        #     myLoc = Loc[0]
        #     runeLoc = Loc[1]
        #     print("내 위치 : ", myLoc)
        #     print("룬 위치 : ", runeLoc)
        #     time.sleep(1)


def stop():
    global handleStat
    global statM1
    global statM2
    # handleStat[0] = 0
    Camera.startCap(False, 1)
    print("캡쳐 끄기")
    Camera.startHandle(False, 1)
    print("핸들수정 끄기")
    Camera.startLoc(False, 1)
    print("위치 찾기 끄기")
    statM1 = False
    statM2 = False
    print("매크로 중지합니다.")

# 기본 모니터링 쓰레드 (내위치, 룬위치, 거탐 등등)
def work1():
    global statM1
    global onRune
    global myLoc
    global runeLoc
    while statM1:
        Loc = Camera.getLoc()
        myLoc = Loc[0]
        runeLoc = Loc[1]
        if myLoc != (0, 0):
            if myLoc != False:
                print("내 위치 : ", myLoc)
                if runeLoc != (0, 0):
                    if runeLoc != False:
                        onRune = True , runeLoc
                        

                if onRune[0]:
                    print("룬 위치 : ", onRune[1])

        time.sleep(int(locationStat[1]))

# 사냥 매크로 쓰레드
def work2():
    global statM2
    global myLoc
    global onRune
    while statM2:
        if onRune[0]:
            if myLoc == onRune[1]:
                print("룬 까야지")
        # print("작업2")
        time.sleep(0.5)


def test1():
    print("tes1")
    # image = cv2.imread("src/static/img/1635604669.jpg")
    bbox_screen = Camera.getRaw()
    image_array = np.array(bbox_screen)
    img2 = cv2.cvtColor(image_array, cv2.COLOR_BGRA2RGB)
    cv2.imwrite(f"src/static/img/{int(time.time())}.jpg", img2)
    pb_path = "src/Rune/saved_model"
    model = tf.saved_model.load(pb_path)
    # monitoring_screen = monitoring(bbox_screen)
    # monitoring_screen = Camera.getRaw()
    # monitoring_screen = cv2.cvtColor(monitoring_screen, cv2.COLOR_RGB2BGR)
    with tf.device('/gpu:0'):
        results = inference_from_model(model, img2)
    print(results)
    
def monitoring(rect):
    bbox = (int(rect[0]), int(rect[1]), int(rect[2]), int(rect[3]))
    image_array = np.array(ImageGrab.grab(bbox=bbox))
    return image_array

def test2():
    print("tes2")

def inference_from_model(model, image, threshold=None):
    img = image.copy()
    input_tensor = tf.convert_to_tensor(img)
    input_tensor = input_tensor[tf.newaxis,...]
    model_fn = model.signatures['serving_default']
    output_dict = model_fn(input_tensor)
    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key:value[0, :num_detections].numpy()
                    for key,value in output_dict.items()}
    output_dict['num_detections'] = num_detections
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
    if threshold is not None:
        detect_class = np.array([value for index, value in enumerate(output_dict['detection_classes'])
                                    if output_dict['detection_scores'][index] > threshold])
        detect_coord = np.array([value for index, value in enumerate(output_dict['detection_boxes'])
                                    if output_dict['detection_scores'][index] > threshold])
        if len(detect_class) == 0:
            return np.array([])
    else:
        detect_class = output_dict['detection_classes'][:4]
        detect_coord = output_dict['detection_boxes'][:4]
    return detect_class[np.argsort(detect_coord[:,1])[::-1]]

if __name__ == "__main__":
    test1()