import win32gui, win32ui, win32con ,win32api

def handdle(win_name):
    # hWnd = win32gui.FindWindow(None, win_name)
    # hwnd=win32gui.GetDesktopWindow()
    # l,t,r,b=win32gui.GetWindowRect(hwnd)
    # h=b-t
    # w=r-l
    hwnd = win32gui.FindWindow(None, win_name)
    if hwnd >=1:
        left, top, right, bot = win32gui.GetWindowRect(hwnd)
        # w = right - left
        # h = bot - top
        # print("창의 좌표는", left, top, right, bot , w , h)
        result = hwnd , left , top , right , bot
        # force_focus(hwnd)
    else:
        # print("창이 없습니다.")
        result = 0 , 0 , 0 , 0 , 0
    return result
def force_focus(hwnd):
    if hwnd >=1:
        win32gui.SetForegroundWindow(hwnd)
        print("창이 포커스되었습니다.")
    else:
        print("창이 없습니다.")