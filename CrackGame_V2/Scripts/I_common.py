from Basis import ControlWindow
from Basis.CaptureWindow import windowsht
from scipy import misc
import time
import math
import datetime
from Basis import WindowManager


def capture(ws):
    while True:
        try:
            ws.capture_window(960, 600)
            break
        except:
            print "Write File Failed, do it again"
            continue

def closeDIE():
    try:
        w = WindowManager.WindowManager()
        w.find_and_set(".*DIEmWin.*")
        w.close_window()
        print "Close DIEWin"
    except:
        print "Cannot Close DIEWin"
