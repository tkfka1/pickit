import multiprocessing as mp
import time
import module.handdle as hd
import module.capture as cap
import cv2

statM = 1
statS = 1
hWnd = 0

def macro():
    print("macro")

def test():
    print("asa")

def start():
    print("시작합니다.")

    # 프로세스 메이플 핸들 가져오기
    print("프로세스 가져오기")
    hWnd = hd.handdle("MapleStory")
    print("메이플스토리 핸들은" + str(hWnd))
    # 켜졌나 확인
    # 기본적인 캡쳐 프로세스 P1 켜기
    p1 = mp.Process(name="CapProcess", target=CapProcess)
    p1.start()



    # p2 = mp.Process(name="SubProcess", target=worker2)
    # p3 = mp.Process(name="SubProcess", target=worker3)

    # p2.start()
    # p3.start()



def CapProcess():
    proc = mp.current_process()
    # print(proc.name)
    # print(proc.pid)

    #핸들 한번더가져오기
    hWnd = hd.handdle("MapleStory")
    
    #반복
    while True:
        # 프로세스 종료 조건
        if statM == 0:
            break
        # 항상위
        hd.force_focus(hWnd)
        
        # 시간 지연
        time.sleep(1)
        
    print("CapProcess 종료")


def worker2():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(4)
    print("SubProcess2 End")


def worker3():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(3)
    print("SubProcess3 End")
    


def stop():
    print("중지합니다.")


if __name__ == "__main__":
    start()