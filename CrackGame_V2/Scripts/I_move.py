from Basis import ControlWindow
from Basis.CaptureWindow import windowsht
from scipy import misc
import time
import math
import datetime
import I_common
import I_cfight

def ScrollToTop(ws):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_up(200, 200)

def ScrollToTop2():
    cl = ControlWindow.windowcl()
    time.sleep(0.5)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.mouse_scroll_up(200, 200)

def ScrollToNextLine(ws):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_down(200, 200)
    time.sleep(0.5)
    cl.move_window(ws._handle, 0, 0)
    cl.mouse_scroll_down(200, 200)

def ScrollToNextLine2():
    cl = ControlWindow.windowcl()
    time.sleep(0.5)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.mouse_scroll_up(200, 200)
    time.sleep(0.5)
    cl.mouse_scroll_down(200, 200)
    time.sleep(0.5)
    cl.mouse_scroll_down(200, 200)

def ToSelectCharacter(ws, ith, next=False):
    selectmap = [(90, 190), (200, 190), (330, 190), (450, 190), (580, 190), (700, 190),
                 (90, 400), (200, 400), (330, 400), (450, 400), (580, 400), (700, 400)]
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    time.sleep(0.5)
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    time.sleep(1)
    cl.nomal_press_keyboard("esc", slp=0.5)
    time.sleep(2)
    cl.click(464,392)
    if next:
        time.sleep(2)
        ScrollToNextLine(ws)
    else:
        time.sleep(2)
        ScrollToTop(ws)
    time.sleep(2)
    cl.click(selectmap[ith][0], selectmap[ith][1])
    time.sleep(0.2)
    cl.click(selectmap[ith][0], selectmap[ith][1])


def ToSelectCharacter2(ith, next=False):
    selectmap = [(90, 190), (200, 190), (330, 190), (450, 190), (580, 190), (700, 190),
                 (90, 400), (200, 400), (330, 400), (450, 400), (580, 400), (700, 400)]
    cl = ControlWindow.windowcl()
    time.sleep(0.5)
    cl = ControlWindow.windowcl()
    time.sleep(1)
    cl.nomal_press_keyboard("esc", slp=0.5)
    time.sleep(2)
    cl.click(464,392)
    if next:
        time.sleep(2)
        ScrollToNextLine2()
    else:
        time.sleep(2)
        ScrollToTop2()
    time.sleep(2)
    cl.click(selectmap[ith][0], selectmap[ith][1])
    time.sleep(0.2)
    cl.click(selectmap[ith][0], selectmap[ith][1])


def MovetoPre(ws):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    print "Start Moving"
    time.sleep(3)
    cl.nomal_press_keyboard("down", slp=4)
    time.sleep(1)
    cl.two_key_together("left","up", slp=5)
    time.sleep(1)
    cl.nomal_press_keyboard("right arrow",slp=2)


def BuyTickets(ws, num, remove_pos):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    time.sleep(3)
    cl.click(202, 396)
    time.sleep(2)
    cl.click(378, 127)
    time.sleep(2)
    cl.click(500, remove_pos)
    time.sleep(2)
    cl.click(286, 152)
    time.sleep(2)

    lnum = len(str(num))
    for i in range(lnum):
        cl.nomal_press_keyboard(str(num)[i], slp=0.5)
        time.sleep(0.5)

    cl.nomal_press_keyboard("enter", slp=1)
    time.sleep(2)
    cl.nomal_press_keyboard("esc", slp=0.5)
    time.sleep(3)
    cl.nomal_press_keyboard("right", slp=3)
    time.sleep(1)
    cl.click(475,285)
    time.sleep(0.2)
    cl.click(475, 285)
    cl.two_key_together("right", "up", slp=3)
    time.sleep(1)
    cl.nomal_press_keyboard("up", slp=0.5)
    time.sleep(1)
    cl.nomal_press_keyboard("space", slp=0.5)
    time.sleep(3)
    cl.nomal_press_keyboard("right", slp=5)
    time.sleep(1)
    cl.click(580, 341)
    time.sleep(1)
    cl.click(630, 391)
    time.sleep(1)
    cl.nomal_press_down("shift", slp=1)
    cl.click(439, 172)
    cl.nomal_press_down("shift", slp=1)
    time.sleep(1)


    number = str(int(int(num)/5))
    lnumber = len(number)
    for i in range(lnumber):
        cl.nomal_press_keyboard(str(number)[i], slp=0.5)
        time.sleep(0.5)

    cl.nomal_press_keyboard("enter", slp=1)
    time.sleep(0.5)
    cl.nomal_press_keyboard("enter", slp=1)
    time.sleep(2)
    cl.nomal_press_keyboard("esc", slp=0.5)
    time.sleep(3)

def stepintomap(ws):
    InTown = True
    count = 0
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    cl.nomal_press_keyboard("down", slp=1)
    cl.nomal_press_keyboard("right", slp=4)
    while (InTown == True and count < 10):
        I_common.capture(ws)
        time.sleep(0.1)
        capimg = misc.imread("c:\\temp\\bla.bmp")
        itemempty = capimg[575, 181]
        if itemempty[0] > 15 and itemempty[0] < 25 and itemempty[1] > 15 and itemempty[1] < 25 and itemempty[
            2] > 15 and itemempty[2] < 25:
            print "MoveDown MoveRight"
            cl = ControlWindow.windowcl()
            cl.move_window(ws._handle, 0, 0)
            cl.nomal_press_keyboard("down", slp=1)
            cl.nomal_press_keyboard("right", slp=4)
        else:
            InTown = False
            print "In pick dungon screen"
        time.sleep(0.3)
        count = count + 1
    if count == 10 and InTown == True:
        print "Have tried 10 times, Failed to the Map:"
        print "We need redo again"
        return False
    else:
        return True



def startgame(ws, first):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    if first==True:
        cl.nomal_press_keyboard("space", slp=0.5)
    inselectscreen = False
    selected = False
    maxcount = 0
    while inselectscreen==False and maxcount<100:
        maxcount = maxcount+1
        I_common.capture(ws)
        time.sleep(0.1)
        capimg = misc.imread("c:\\temp\\bla.bmp")
        selectpixel1 = capimg[300, 473]
        selectpixel2 = capimg[300, 393]
        selectpixel3 = capimg[585,429]
        inselectscreen1 = selectpixel1[0] > 200 and selectpixel1[1] > 200 and selectpixel1[2] > 200
        inselectscreen2 = selectpixel2[0] > 200 and selectpixel2[1] > 200 and selectpixel2[2] > 200
        inselectscreen3 = selectpixel3[0] >200 and selectpixel3[0] < 210 and selectpixel3[1] >180 and selectpixel3[1] < 190 and selectpixel3[2] >130 and selectpixel3[2] < 140
        inselectscreen = inselectscreen1 and inselectscreen2 and inselectscreen3
        # inselectscreen = inselectscreen2
        if inselectscreen and selected==False:
            print "In select screen, press spacebar"
            cl.move_window(ws._handle, 0, 0)
            cl.nomal_press_keyboard("space", slp=0.5)
            time.sleep(2)
            selected = True
        elif inselectscreen==False and selected==True:
            print "In game now, start fight!"
            break
    if maxcount==100:
        print "Did not find select Screen in 10s, But Let it go."


def infight(ws):
    I_common.capture(ws)
    time.sleep(0.1)
    capimg = misc.imread("c:\\temp\\bla.bmp")
    ingamepixel = capimg[75, 553]
    if ingamepixel[0]<50 and ingamepixel[1]<50 and ingamepixel[2]<50:
        return False
    else:
        return True

def iamdead(ws):
    I_common.capture(ws)
    time.sleep(0.1)
    capimg = misc.imread("c:\\temp\\bla.bmp")
    ingamepixel = capimg[75, 407]
    if ingamepixel[0] < 50 and ingamepixel[1] < 50 and ingamepixel[2] < 50:
        return True
    else:
        return False

def clear(ws, character):
    notdead = True
    time.sleep(1)
    while (notdead):
        notdead = infight(ws)
        if notdead == False:
            print "Clear"
            return True

        I_cfight.characterfight(ws, character)

        notdead = infight(ws)
        if notdead == False:
            print "Clear"
            return True
        if iamdead(ws):
            return False

def pickup(ws,key):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    cl.nomal_press_keyboard(key, slp=0.3)
    atknum = 5
    for i in range(atknum):
        cl.nomal_press_keyboard("x", slp=0.3)
    print "PickupFinished"


def Click_Retry(ws):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    cl.click(806, 87)

def Click_Return_InMap(ws):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    cl.click(806, 149)

def Click_Return_ByESC(ws):
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    cl.click(395, 570)