import win32gui
import win32con
import re

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""
    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name = None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        # if str(win32gui.GetWindowText(hwnd))!="":
        #     print str(win32gui.GetWindowText(hwnd))
        #     win32gui.SetForegroundWindow(hwnd)
        #     pyautogui.press('a')
        #     print "next"
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd
            # win32gui.SetForegroundWindow(hwnd)
            # pyautogui.press('a')

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.ShowWindow(self._handle, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(self._handle)

