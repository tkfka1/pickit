from pyduino_mk.arduino import Arduino
from pyduino_mk.arduino import *
import time

ardu = Arduino()
time.sleep(1)
ardu.move(300, 300)
time.sleep(3)
# ardu.type('https://github.com/nelsontran/PyDuino-MK/', accuracy=85)
ardu.write('A')
ardu.write(65)
ardu.press(LEFT_ALT)

# Hit Ctrl+Alt+Delete
# arduino.press(LEFT_CTRL)
# arduino.press(LEFT_ALT)
# arduino.press(DELETE)
# arduino.releaseAll()

# Drag the left mouse button to (500, 500)
# arduino.press()
# arduino.bezier_move(500, 500)
# arduino.release()