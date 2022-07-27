import cv2
import mss
import numpy
import threading
import time
import win32gui, win32ui, win32con ,win32api
from ctypes import windll, wintypes, byref, sizeof

class Camera(object):
    thread = None
    frame = None
    last_access = 0



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
    def frames():
        hwndname ="MapleStory"
        hwnd = win32gui.FindWindow(None, hwndname)
        if hwnd >=1:
            left, top, right, bot = win32gui.GetWindowRect(hwnd)
            w = right - left
            h = bot - top
        print("창의 좌표는", left, top, right, bot)

        monitor = {
            'top': top+26,
            'left': left+3,
            'width': 1366,
            'height': 768
        }
        with mss.mss() as sct:
            while True:
                hwndname ="MapleStory"
                hwnd = win32gui.FindWindow(None, hwndname)
                if hwnd >=1:
                    left, top, right, bot = win32gui.GetWindowRect(hwnd)
                    w = right - left
                    h = bot - top
                print("창의 좌표는", left, top, right, bot)

                monitor = {
                    'top': top+26,
                    'left': left+3,
                    'width': 1366,
                    'height': 768
                }
                
                time.sleep(0.1)
                raw = sct.grab(monitor)
                # Use numpy and opencv to convert the data to JPEG. 
                img = cv2.imencode('.jpg', numpy.array(raw))[1].tobytes()
                img2 = cv2.cvtColor(numpy.array(raw), cv2.COLOR_BGRA2BGR)
                cv2.imwrite("src/static/img/temp.png", img2)
                yield(img)

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