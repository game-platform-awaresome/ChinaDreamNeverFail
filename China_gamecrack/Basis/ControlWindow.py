import Admin
if not Admin.isUserAdmin():
    Admin.runAsAdmin()
import win32con
import win32gui
import win32api
import time
import KeyboardDict
from scipy import misc
import numpy as np
'''Shutdown the DIEmWin to control the keyboard'''


# ws = windowsht()
# ws.active_window(".*Dungeon Fighter Online.*")
# ws.active_window(".*test.*")
# ws.capture_window(960,600)
# image = misc.imread("tmp.bmp")
# plt.imshow(image)
# plt.show()
# test_point = image[23][60]
# test_color = np.array([255,255,255])
#
# if np.array_equal(test_point,test_color):
#     print "true"
#     win32gui.SetForegroundWindow(ws._handle)
#     shell = comclt.Dispatch("WScript.Shell")
#     shell.SendKeys("a")
#     shell.SendKeys("a")

# win32gui.SetForegroundWindow(ws._handle)
# shell = comclt.Dispatch("WScript.Shell")
# shell.SendKeys("a")
# shell.SendKeys("a")

# w = WindowManager.WindowManager()
# # w.find_and_set(".*DIEmWin.*")
# w.find_and_set(".*Dungeon Fighter Online.*")
# w.move_window(0,0)
# shell = comclt.Dispatch("WScript.Shell")
# shell.SendKeys('%')
# win32gui.ShowWindow(ws._handle, win32con.SW_SHOW)
# win32gui.SetForegroundWindow(ws._handle)

def capture(ws):
    while True:
        try:
            ws.capture_window(960, 600)
            break
        except:
            print "Write File Failed, do it again"
            continue

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

class windowcl:
    def click(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    def right_click(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

    def mouse_scroll_down(self,x,y):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, -1, 0)

    def mouse_scroll_up(self,x,y):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, 1, 0)

    def avaliable_press_keyboard(self, ws, key, slp=0.1):
        capture(ws)
        time.sleep(0.1)
        capimg = misc.imread("c:\\temp\\bla.bmp")
        keydict = {"a":[(613,563),(639,590)], "s":[(643,563),(669,590)], "d":[(673,563),(699,590)],
                   "f":[(703,563),(729,590)], "g":[(733,563),(759,590)], "h":[(763,563),(789,590)],
                   "q":[(613,533),(639,560)], "w":[(643,533),(669,560)], "e":[(673,533),(699,560)],
                   "r":[(703,533),(729,560)], "t":[(733,533),(759,560)], "y":[(763,533),(759,560)]}
        skill = capimg[keydict[key][0][1]:keydict[key][1][1],keydict[key][0][0]:keydict[key][1][0]]
        skillgray = rgb2gray(skill)
        cding = np.count_nonzero(skillgray == 255)
        if cding<5:
            self.nomal_press_keyboard(key,slp)
        else:
            pass

    def nomal_input(self,str):
        for c in str:
            self.nomal_press_keyboard(c)

    def nomal_press_keyboard(self,key,slp=0.1):
        KeyboardDict.pressAndHold(key)
        time.sleep(slp)
        KeyboardDict.release(key)

    def nomal_press_down(self,key,slp=0.1):
        KeyboardDict.pressAndHold(key)
        time.sleep(slp)
        KeyboardDict.release(key)

    def nomal_press_up(self,key,slp=0.1):
        time.sleep(slp)
        KeyboardDict.release(key)

    def two_key_together(self,key1, key2, slp=0.1):
        KeyboardDict.pressAndHold(key1)
        time.sleep(0.1)
        KeyboardDict.pressAndHold(key2)
        time.sleep(slp)
        KeyboardDict.release(key1)
        KeyboardDict.release(key2)

    def move_window(self,hwnd,x,y):
        rect = win32gui.GetWindowRect(hwnd)
        x1 = rect[0]
        y1 = rect[1]
        w = rect[2] - x1
        h = rect[3] - y1
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, x, y, w, h, 0)

    def close_window(self,hwnd):
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

# nomal_press_keyboard('down_arrow',slp=0.5)


# def move_window(x,y):
#     win32gui.MoveWindow()

# click(15,15)
# time.sleep(0.5)
# # w.find_and_set(".*Dungeon Fighter Online.*")
# click(16,16)
# win32gui.SetActiveWindow(w._handle)
# win32gui.SetFocus(w._handle)
# win32gui.SetForegroundWindow(w._handle)
# win32gui.SetActiveWindow(w._handle)
# wc = windowcl()
# wc.move_window(w._handle,0,0)
# KeyboardDict.pressAndHold('s')
# time.sleep(0.2)
# KeyboardDict.release('s')

# print "1"
# shell = comclt.Dispatch("WScript.Shell")
# shell.SendKeys("{DOWN}")
# print "2"
# pyautogui.keyDown('down')
# time.sleep(0.5)
# pyautogui.keyUp('down')
# print "3"
# keyboard.press_and_release('down')
# print "4"


# right_click(800,500)
# pyautogui.moveTo(15, 15)
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
# pyautogui.click(x=800,y=500,button='right')
# pyautogui.keyDown('right')
# pyautogui.PAUSE = 2
# pyautogui.keyUp('right')
# pyautogui.hotkey('ctrl', 'shift', 'esc')
# pyautogui.hotkey('ctrl', 'alt', 'delete')
# pyautogui.PAUSE = 2
# pyautogui.press('a')
# pyautogui.PAUSE = 2
# pyautogui.press('s')
# pyautogui.PAUSE = 2
# pyautogui.press('d')
# pyautogui.hotkey('ctrl', 'shift', 'esc')
# pyautogui.keyDown('a')
# pyautogui.PAUSE = 6
# pyautogui.keyUp('a')


# win32gui.ShowWindow(ws._handle, win32con.SW_SHOW)
# win32gui.SetForegroundWindow(ws._handle)
# win32gui.SetActiveWindow(ws._handle)
# keyboard = Controller()
#
# keyboard.press(Key.space)
# keyboard.release(Key.space)
#
# # Type a lower case A; this will work even if no key on the
# # physical keyboard is labelled 'A'
# keyboard.press('a')
# keyboard.release('a')
# keyboard.write('The quick brown fox jumps over the lazy dog.')



# print "finish"
