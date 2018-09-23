from Basis import ControlWindow
from Basis.CaptureWindow import windowsht
import time
'''Here we start the Script'''

print "OKay. Start Then--------------------------------------------------------------------------------"

# print "Move Window to left upper corner, window size is constant"
ws = windowsht()
ws.active_window(".*Dungeon Fighter Online.*")
cl = ControlWindow.windowcl()
cl.move_window(ws._handle,0,0)


cl.move_window(ws._handle, 0, 0)
# cl.nomal_press_keyboard("numpad_1", slp=0.5)
time.sleep(0.5)
cl.move_window(ws._handle, 0, 0)

cl.mouse_scroll_up(200,200)
time.sleep(0.5)
cl.move_window(ws._handle, 0, 0)

cl.mouse_scroll_down(200,200)