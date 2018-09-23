from Basis import ControlWindow
from Basis.CaptureWindow import windowsht
from scipy import misc
import time
import math
import datetime
from Basis import WindowManager
import I_common
import I_move
import StartGame
import datetime
import math
import cv2
import numpy as np
import os
import subprocess
now = datetime.datetime.now()
import keyboard
# from pynput.keyboard import Key, Controller
#
# keyboard = Controller()
#
# # Press and release space
# keyboard.press(Key.space)
# keyboard.release(Key.space)



# # Type two upper case As
# keyboard.press('A')
# keyboard.release('A')
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')

# # Type 'Hello World' using the shortcut type method
# keyboard.type('Hello World')


ws = windowsht()
ws.active_window(".*Dungeon Fighter Online.*")
# ws.active_window(".*DIEmWin.*")
cl = ControlWindow.windowcl()
cl.move_window(ws._handle, 0, 0)





import pythoncom, pyHook

def OnKeyboardEvent(event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'

# return True to pass the event to other handlers
    return True


# create a hook manager
hm = pyHook.HookManager()

# hm.KeyboardSwitch(256, 77, 50, 109, 0, 1, ws._handle, 'dfo')

print "give to"
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
keyboard.unhook_all()
keyboard.send('m')
# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
# keyboard.press('m')
# keyboard.release('m')
#
# cl2 = ControlWindow.windowcl()
# print "win"
# time.sleep(3)
# cl2.nomal_press_keyboard("m")
# time.sleep(1)
# cl.two_key_together("numpad_4", "numpad_8", slp=5)
# time.sleep(1)
# cl2.nomal_press_keyboard("m",slp=1)
# time.sleep(1)
# cl2.nomal_press_keyboard("m")

# wait foreveras
# pythoncom.PumpMessages()

# # create a hook manager
# hm = pyHook.HookManager()
# # watch for all mouse events
# hm.MouseAll = OnMouseEvent
# # set the hook
# hm.HookMouse()
# # wait forever
pythoncom.PumpMessages()




characterdict = {0:"seraph", 1:"heiqiang", 2:"mudan", 3:"palading", 4:"msm", 5:"modao",
                 6:"wunv", 7:"guanyu", 8:"tegong", 9:"xukong", 10:"nvdaqiang", 11:"fsm",
                 12:"seraph", 13:"saint", 14:"zhaohuan", 15:"fnen",16:"indra",17:"andi",
                 18:"hongyan"}

BT = False
pickupkey = "/"
#
# fatiguelist = {
# 0:293,  1:293,  2:293,  3:293,  4:270,  5:293,
# 6:293,  7:293,  8:293,  9:293,  10:293, 11:250,
# 12:220, 13:293, 14:293, 15:293, 16:293, 17:293,
# 18:220
# }

fatiguelist = {
0:273,  1:273,  2:273,  3:273,  4:273,  5:273,
6:273,  7:273,  8:273,  9:273,  10:273, 11:273,
12:273, 13:273, 14:273, 15:273, 16:273, 17:273,
18:273
}

'''Here the fatigue of each character is input'''
# repeattimedict0 = {0:math.ceil(293/8.0),     1:math.ceil(95/8.0),   2:math.ceil(293/8.0),   3:math.ceil(273/8.0),   4:math.ceil(273/8.0),   5:math.ceil(273/8.0),
#                    6:math.ceil(273/8.0),   7:math.ceil(273/8.0),   8:math.ceil(273/8.0),   9:math.ceil(273/8.0),   10:math.ceil(273/8.0),  11:math.ceil(273/8.0),

rp = {0:450, 1:450, 2:450, 3:450, 4:450, 5:450, 6:450, 7:450, 8:450, 9:450, 10:450, 11:450, 12:450, 13:450, 14:450, 15:450, 16:450, 17:450, 18:450}


usinglist = [18,11,12,13,14,15,16,17,10,9,8,7,6,5,4,3,2,1,0]


print "Move Window to left upper corner, window size is constant"
ws = windowsht()
ws.active_window(".*Dungeon Fighter Online.*")
cl = ControlWindow.windowcl()
cl.move_window(ws._handle, 0, 0)
cl.click(400, 400)
time.sleep(1)
k.tap_key('m')
time.sleep(2)
ws2 = windowsht()
ws2.active_window(".*DIEmWin.*")
cl2 = ControlWindow.windowcl()
cl2.move_window(ws._handle, 0, 0)


# cl2 = ControlWindow.windowcl()
# cl2.move_window(ws._handle, 0, 0)
# print "dfo"
# time.sleep(3)
# cl2.nomal_press_keyboard("m")
# # time.sleep(1)
# # cl.two_key_together("numpad_4", "numpad_8", slp=5)
# time.sleep(1)
# cl2.nomal_press_keyboard("m",slp=1)
# time.sleep(1)
# cl2.nomal_press_keyboard("m")

cl2 = ControlWindow.windowcl()
cl2.move_window(ws2._handle, 0, 0)
print "win"
time.sleep(3)
cl2.nomal_press_keyboard("m")
# time.sleep(1)
# cl.two_key_together("numpad_4", "numpad_8", slp=5)
time.sleep(1)
cl2.nomal_press_keyboard("m",slp=1)
time.sleep(1)
cl2.nomal_press_keyboard("m")