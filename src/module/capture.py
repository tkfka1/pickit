import win32gui, win32ui, win32con ,win32api

win_name='MapleStory' # 창이름
hWnd = win32gui.FindWindow(None, win_name)
print("창의 좌표는", hWnd)

def screenshot(hwnd = None):
    if not hwnd:
        hwnd=win32gui.GetDesktopWindow()
    l,t,r,b=win32gui.GetWindowRect(hwnd)
    h=b-t
    w=r-l
    hDC = win32gui.GetWindowDC(hwnd)
    myDC=win32ui.CreateDCFromHandle(hDC)
    newDC=myDC.CreateCompatibleDC()

    myBitMap = win32ui.CreateBitmap()
    #myBitMap.CreateCompatibleBitmap(myDC, w, h)
    myBitMap.CreateCompatibleBitmap(myDC, 1366, 768)
    newDC.SelectObject(myBitMap)

    # win32gui.SetForegroundWindow(hwnd)
    # sleep(.2)
    newDC.BitBlt((-3,-26),(w, h) , myDC, (0,0), win32con.SRCCOPY)
    myBitMap.Paint(newDC)
    myBitMap.SaveBitmapFile(newDC,'src/static/img/temp.bmp')

screenshot(hWnd)
