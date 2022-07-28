import cv2
from flask import g
import mss
import numpy
import threading
import time
import module.handle as hd
import module.imgCheck as ic
import tensorflow as tf
import numpy as np

class Camera(object):
    #######################################
    #건들 ㄴㄴ
    thread = None
    frame = None
    last_access = 0
    # 캡쳐 상태, 주기
    global capStat
    capStat = True , 0.5
    # 핸들값
    global hwnd
    hwnd = hd.handdle("MapleStory")
    # 핸들 상태 , 주기
    global handleStat
    handleStat = False , 2
    # 위치 상태 , 주기
    global locationStat
    locationStat = False , 2
    # 위치 미니맵 크기
    global mapSize
    mapSize = (0, 0, 320, 250)
    # 룬 상태 , 주기
    global runeStat
    runeStat = False , 2
    #######################################
    global myLoc
    myLoc = (0, 0)
    global runeLoc
    runeLoc = (0, 0)
    global raw

    # 최상위로
    # hd.force_focus(hwnd[0])

    def __init__(self):
        if Camera.thread is None:
            Camera.last_access = time.time()
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()


            while self.get_frame() is None:
                time.sleep(0)

    def get_frame(self):
        '''Get the current frame.'''
        Camera.last_access = time.time()

        return Camera.frame

    @staticmethod
    def transpose():
        print("transpose")

    @staticmethod
    def frames():
        global hwnd
        global capStat  
        global handleStat
        global locationStat
        global mapSize
        global myLoc
        global runeLoc
        global raw

        top = hwnd[2]
        left = hwnd[1]
        monitor = {
            'top': top+26,
            'left': left+3,
            'width': 1366,
            'height': 768
        }

        with mss.mss() as sct:
            i = 0
            while True:
                i += 1
                # cycles초마다 반복하는 코드
                time.sleep(capStat[1])
                # 캡쳐 웹 보내기
                if capStat[0]:
                    raw = sct.grab(monitor)
                    img = cv2.imencode('.jpg', numpy.array(raw))[1].tobytes()
                    yield(img)
                # 핸들 재수정
                if handleStat[0]:  
                    if i%int(handleStat[1]) == 0: 
                        hwnd = hd.handdle("MapleStory")
                        top = hwnd[2]
                        left = hwnd[1]
                        monitor = {
                            'top': top+26,
                            'left': left+3,
                            'width': 1366,
                            'height': 768
                        }
                if locationStat[0]:
                    if i%int(locationStat[1]) == 0:
                        img2 = cv2.cvtColor(numpy.array(raw), cv2.COLOR_BGRA2BGR)
                        x=mapSize[0]; y=mapSize[1]; w=mapSize[2]; h=mapSize[3]
                        myLoc = ic.minimapLoc(img2 , 0.99 , x , y , w , h)
                        if runeStat[0]:
                            if i%int(runeStat[1]) == 0:
                                runeLoc = ic.runeLoc(img2 , 0.99 , x , y , w , h)
               
                                
                # print(i)
                # 이미지 전송
                # img2 = cv2.cvtColor(numpy.array(raw), cv2.COLOR_BGRA2BGR)
                # cv2.imwrite("src/static/img/temp.png", img2)

    @classmethod
    def _thread(cls):
        '''As long as there is a connection and the thread is running, reassign the current frame.'''
        print('Starting camera thread.')
        frames_iter = cls.frames()
        for frame in frames_iter:
            Camera.frame = frame
            if time.time() - cls.last_access > 10:
                frames_iter.close()
                print('Stopping camera thread due to inactivity.')
                break
        cls.thread = None

    def startCap(stat , time):
        global capStat
        capStat = stat , float(time)

    def startHandle(stat , time):
        global handleStat
        handleStat = stat , float(time)

    def startLoc(stat , time):
        global locationStat
        locationStat = stat , float(time)

    def startRune(stat , time):
        global runeStat
        runeStat = stat , float(time)

    def startMap(x, y, w, h):
        global mapSize
        mapSize = int(x) , int(y) , int(w) , int(h)

    def hwndPrint():
        global hwnd
        return hwnd

    def getRaw():
        global raw
        return raw

    def force_focus():
        hd.force_focus(hwnd[0])
    
    def getLoc():
        global myLoc
        global runeLoc
        return myLoc , runeLoc
    
    def getP1():
        global capStat
        if capStat[0]:
            return True
        else:
            return False
            

    def iTimeChange( H , L , R):
        global iTime
        global iHandle
        global iLocation
        global iRune
        iHandle = H
        iLocation = L
        iRune = R
        iHandleI = iHandle/cycles
        iLocationI = iHandle/cycles
        iRuneI = iHandle/cycles
        iTime= iHandleI, iLocationI, iRuneI
        print(iTime)
