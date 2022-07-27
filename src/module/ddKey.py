from ctypes import *

dd_dll = windll.LoadLibrary('src/DD94687.64.dll')

st = dd_dll.DD_btn(0) #classdd 초기설정
if st==1:
    print("OK")
else:
    print("Error")
    exit(101)