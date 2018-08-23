import win32con
import win32gui
import win32api
import win32com
import re
import ctypes


GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW

def getWindowText(hwnd):
    length = GetWindowTextLength(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buff, length + 1)
    return buff.value

class WindowManager:
    def __init__(self):
        self._handle = None

    def _window_enum_callback( self, hwnd, wildcard ):
        title_text = getWindowText(hwnd)
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None or wildcard==title_text:
            self._handle = hwnd
            print title_text

    #CASE SENSITIVE
    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        win32gui.ShowWindow(self._handle, win32con.SW_RESTORE)
        # win32gui.SetWindowPos(self._handle,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
        # win32gui.SetWindowPos(self._handle,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
        # win32gui.SetWindowPos(self._handle,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
        # shell = win32com.client.Dispatch("WScript.Shell")
        # shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._handle)

    def find_and_set(self, search):
        self.find_window_wildcard(search)
        self.set_foreground()

    def move_window(self,x,y):
        rect = win32gui.GetWindowRect(self._handle)
        x1 = rect[0]
        y1 = rect[1]
        w = rect[2] - x1
        h = rect[3] - y1
        win32gui.SetWindowPos(self._handle, win32con.HWND_NOTOPMOST, x, y, w, h, 0)

    def close_window(self):
        win32gui.PostMessage(self._handle, win32con.WM_CLOSE, 0, 0)
