import win32gui, win32ui, win32con ,win32api

def handdle(win_name):
    hWnd = win32gui.FindWindow(None, win_name)
    hwnd=win32gui.GetDesktopWindow()
    l,t,r,b=win32gui.GetWindowRect(hwnd)
    h=b-t
    w=r-l
    return hWnd , h , w