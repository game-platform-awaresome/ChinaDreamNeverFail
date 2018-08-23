# -*- coding: UTF-8 -*-
import ctypes
import win32con
import win32gui
import win32api
import win32com
import re
import time

GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW

def getWindowText(hwnd):
    length = GetWindowTextLength(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buff, length + 1)
    return buff.value


for i in range(1000):
    time.sleep(2)
    w=win32gui
    hwnd = w.GetForegroundWindow()
    ctypeww = getWindowText(hwnd)
    title_texto = w.GetWindowText(hwnd)
    title_text = title_texto.decode('gbk').encode('utf-8')
    # clsname = w.GetClassName(hwnd)
    # clsname = clsname.decode('gbk').encode('utf-8')
    print title_text + ': class: ' + 'handle: ' + str(hwnd)
    print ctypeww
    print "haha"
