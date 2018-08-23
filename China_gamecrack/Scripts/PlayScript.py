if not Admin.isUserAdmin():
    Admin.runAsAdmin()

from Basis import ControlWindow
from Basis.CaptureWindow import windowsht
from scipy import misc
import numpy as np
import time
from scipy import signal


def ifmap(ws):
    im = False


def if1clear(ws, th):
    ic = False
    ws.capture_window(960, 600)
    capimg = misc.imread("c:\\temp\\bla.bmp", flatten=True)
    dic = {1:(56,907), 2:(56,925), 3:(74,925), 4:(92,925), 5:(92, 943), 6:(92,925)}
    dic2 = {1:(60, 907), 2:(60,925), 3:(78,925), 4:(96,925), 5:(96, 943), 6:(96,925)}
    # if ((capimg[dic[th]]  > 50)  & (capimg[dic[th]] <110)) & ( (capimg[dic2[th]]  > 50) &  (capimg[dic2[th]]  < 90 ) ):
    if th!=6:
        if ((capimg[dic[th]] > 50)  & ((capimg[dic2[th]] > 50)) ):
            ic = True
        return ic
    else:
        c1 = capimg[dic[th]]
        time.sleep(0.4)
        ws.capture_window(960, 600)
        capimg2 = misc.imread("c:\\temp\\bla.bmp", flatten=True)
        c2 = capimg2[dic[th]]
        if c1!=c2:
            return True
        else:
            return False

def characterpos(ws):
    ws.capture_window(960, 600)
    capimg = misc.imread("c:\\temp\\bla.bmp", flatten=True)
    # plt.imshow(capimg)
    # plt.show()
    # misc.imsave("character.bmp",capimg[250:372,200:250])
    charactermatrix = misc.imread("character1.bmp", flatten=True)
    grad = signal.convolve2d(capimg, charactermatrix, boundary='symm', mode='same')
    pos = np.unravel_index(grad.argmax(), grad.shape)
    return pos

def findtime(ws):
    return 0

def stepintomap(ws):
    InTown = True
    while (InTown == True):
        ws.capture_window(960, 600)
        capimg = misc.imread("c:\\temp\\bla.bmp")
        if np.array_equal(np.array(capimg[575, 181]), np.array([17, 17, 17])):
            cl.move_window(ws._handle, 0, 0)
            cl.nomal_press_keyboard("right_arrow", slp=3)
        else:
            InTown = False
        print "MoveRight"
        time.sleep(0.3)

def choosemap(ws):
    cl.move_window(ws._handle, 0, 0)
    cl.nomal_press_keyboard("down_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("down_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("left_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("left_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("left_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("left_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("right_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("right_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("right_arrow", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("spacebar", slp=0.3)

    InMap = False
    while (InMap == False):
        ws.capture_window(960, 600)
        capimg = misc.imread("c:\\temp\\bla.bmp")
        if np.array_equal(np.array(capimg[10, 947]), np.array([201, 201, 201])):
            InMap = True
        else:
            time.sleep(0.3)
            pass

    print "In Map"
    return InMap

def clear1(ws):
    cl.move_window(ws._handle, 0, 0)
    # cl.nomal_press_keyboard("up_arrow",slp=3)
    # cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("s", slp=2)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("c", slp=1)
    cl.nomal_press_keyboard("right_arrow", slp=4)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("down_arrow", slp=2)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("f", slp=1)
    time.sleep(1)
    IfClear = if1clear(ws,1)
    while (IfClear == False):
        cl.nomal_press_keyboard("0", slp=0.3)
        cl.nomal_press_keyboard("d", slp=0.5)
        atknum = 15
        for i in range(atknum):
            cl.nomal_press_keyboard("0", slp=0.1)
            cl.nomal_press_keyboard("a", slp=0.2)
        IfClear = if1clear(ws, 1)
        continue
    # manpos = characterpos(ws)
    # findtime(ws)
    print "1st Cleared, wait CD then move to 2nd."
    time.sleep(22)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("up_arrow", slp=1)
    print "Moving to 2nd."

def clear2(ws):
    cl.move_window(ws._handle, 0, 0)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("f", slp=1)
    time.sleep(1)
    IfClear = if1clear(ws, 2)
    while (IfClear == False):
        cl.nomal_press_keyboard("0", slp=0.3)
        cl.nomal_press_keyboard("d", slp=0.5)
        atknum = 15
        for i in range(atknum):
            cl.nomal_press_keyboard("0", slp=0.1)
            cl.nomal_press_keyboard("a", slp=0.2)
        IfClear = if1clear(ws, 2)
        continue
    print "2nd Cleared, wait CD then move to 3rd."
    time.sleep(20)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("right_arrow", slp=5)
    print "Moving to 3rd."

def clear3(ws):
    cl.move_window(ws._handle, 0, 0)
    cl.nomal_press_keyboard("right_arrow", slp=2)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("f", slp=1)
    time.sleep(1)
    IfClear = if1clear(ws, 3)
    while (IfClear == False):
        cl.nomal_press_keyboard("0", slp=0.3)
        cl.nomal_press_keyboard("d", slp=0.5)
        atknum = 15
        for i in range(atknum):
            cl.nomal_press_keyboard("0", slp=0.1)
            cl.nomal_press_keyboard("a", slp=0.2)
        IfClear = if1clear(ws, 3)
        continue
    print "3rd Cleared, wait CD then move to 4th."
    time.sleep(20)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("down_arrow", slp=2)
    cl.nomal_press_keyboard("left_arrow", slp=2)
    print "Moving to 4th."

def clear4(ws):
    cl.move_window(ws._handle, 0, 0)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("f", slp=1)
    time.sleep(1)
    IfClear = if1clear(ws, 4)
    while (IfClear == False):
        cl.nomal_press_keyboard("0", slp=0.3)
        cl.nomal_press_keyboard("d", slp=0.5)
        atknum = 5
        for i in range(atknum):
            cl.nomal_press_keyboard("0", slp=0.1)
            cl.nomal_press_keyboard("a", slp=0.2)
        IfClear = if1clear(ws, 4)
        continue
    print "4th Cleared, wait CD then move to 5th."
    time.sleep(20)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("s", slp=2)
    cl.nomal_press_keyboard("down_arrow", slp=2)
    cl.nomal_press_keyboard("right_arrow", slp=1)
    print "Moving to 5th."

def clear5(ws):
    cl.move_window(ws._handle, 0, 0)
    cl.nomal_press_keyboard("down_arrow", slp=0.5)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("left_arrow", slp=0.5)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("g", slp=1)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("f", slp=1)
    time.sleep(1)
    IfClear = if1clear(ws, 5)
    while (IfClear == False):
        cl.nomal_press_keyboard("0", slp=0.3)
        cl.nomal_press_keyboard("d", slp=0.5)
        atknum = 15
        for i in range(atknum):
            cl.nomal_press_keyboard("0", slp=0.1)
            cl.nomal_press_keyboard("a", slp=0.2)
        IfClear = if1clear(ws, 5)
        continue
    print "5th Cleared, wait CD then move to 6th."
    time.sleep(20)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("down_arrow", slp=4)
    cl.nomal_press_keyboard("right_arrow", slp=3)
    cl.nomal_press_keyboard("up_arrow", slp=1)
    cl.nomal_press_keyboard("right_arrow", slp=1)
    print "Moving to 6th."

def clear6(ws):
    cl.move_window(ws._handle, 0, 0)
    time.sleep(0.5)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("f", slp=1)
    cl.nomal_press_keyboard("right_arrow", slp=2)
    time.sleep(1)
    IfClear = if1clear(ws, 6)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("d", slp=0.5)
    atknum = 15
    for i in range(atknum):
        cl.nomal_press_keyboard("0", slp=0.1)
        cl.nomal_press_keyboard("a", slp=0.2)

    print "6th Cleared, wait CD then move to final."
    time.sleep(15)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("right_arrow", slp=3)
    cl.nomal_press_keyboard("up_arrow", slp=3)
    cl.nomal_press_keyboard("left_arrow", slp=1)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("y", slp=0.2)
    time.sleep(5)
    cl.nomal_press_keyboard("up_arrow", slp=1)
    print "Moving to final."

def clearfinal(ws):
    cl.move_window(ws._handle, 0, 0)
    time.sleep(0.5)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("y", slp=0.2)
    cl.nomal_press_keyboard("up_arrow", slp=0.3)
    cl.nomal_press_keyboard("right_arrow", slp=2)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("g", slp=1)
    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("f", slp=1)
    time.sleep(1)

    cl.nomal_press_keyboard("0", slp=0.3)
    cl.nomal_press_keyboard("d", slp=0.5)
    atknum = 15
    for i in range(atknum):
        cl.nomal_press_keyboard("0", slp=0.1)
        cl.nomal_press_keyboard("a", slp=0.2)
    print "final Cleared, wait finish."

def startover(ws):
    InMap = False
    while (InMap == False):
        ws.capture_window(960, 600)
        capimg = misc.imread("c:\\temp\\bla.bmp")
        if np.array_equal(np.array(capimg[10, 947]), np.array([201, 201, 201])):
            InMap = True
        else:
            time.sleep(0.3)
            pass
    return InMap


'''This is the game-playing script for different goals'''
# capimg = misc.imread("c:\\temp\\bla.bmp", flatten=True)
ws = windowsht()
ws.active_window(".*Dungeon Fighter Online.*")
# w = WindowManager.WindowManager()
# w.find_and_set(".*Dungeon Fighter Online.*")
cl = ControlWindow.windowcl()
cl.move_window(ws._handle,0,0)

# KeyboardDict.pressAndHold("right_arrow")
# time.sleep(0.5)
# KeyboardDict.release("right_arrow")
#28,119,184          44,96,141

'''Check if in town'''
stepintomap(ws)

# plt.imshow(capimg)
# plt.show()


'''Step into Map'''
InMap = choosemap(ws)
i=0
for i in range(2):
    if InMap == True:
        '''Start Fight'''
        '''1st map'''
        print "In the Map, Start 1st Clear"
        clear1(ws)


        '''2nd map'''
        print "Start 2nd Clear"
        clear2(ws)

        print "Start 3rd Clear"
        clear3(ws)

        print "Start 4rd Clear"
        clear4(ws)

        print "Start 5rd Clear"
        clear5(ws)

        print "Start 6rd Clear"
        clear6(ws)

        print "Start final Clear"
        clearfinal(ws)

        time.sleep(15)
        print "Picking"

        cl.nomal_press_keyboard("enter", slp=0.5)
        cl.nomal_press_keyboard("/", slp=0.3)
        cl.nomal_press_keyboard("/", slp=0.3)
        cl.nomal_press_keyboard("s", slp=0.3)
        cl.nomal_press_keyboard("e", slp=0.3)
        cl.nomal_press_keyboard("t", slp=0.3)
        cl.nomal_press_keyboard("i", slp=0.3)
        cl.nomal_press_keyboard("t", slp=0.3)
        cl.nomal_press_keyboard("e", slp=0.3)
        cl.nomal_press_keyboard("m", slp=0.3)
        cl.nomal_press_keyboard("enter", slp=0.5)
        atknum = 15
        for i in range(atknum):
            cl.nomal_press_keyboard("x", slp=0.3)


        cl.nomal_press_keyboard("ecs", slp=0.3)

        print "Start Over Again"
        cl.nomal_press_keyboard("8", slp=0.5)
        time.sleep(1)
        InMap = startover(ws)


print "finish"
