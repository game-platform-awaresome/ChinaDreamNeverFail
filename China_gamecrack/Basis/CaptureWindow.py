import win32ui
import win32gui
import win32con
import WindowManager

class windowsht:
    def __init__ (self):
        """Constructor"""
        self._handle = None

    def active_window(self, name):
        w = WindowManager.WindowManager()
        w.find_and_set(name)
        # window.set_foreground()
        self._handle = w._handle

    def capture_window(self, size_w, size_h):
        hwnd = self._handle
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, size_w, size_h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (size_w, size_h), dcObj, (0, 0), win32con.SRCCOPY)

        dataBitMap.SaveBitmapFile(cDC, "c:\\temp\\bla.bmp")
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())


