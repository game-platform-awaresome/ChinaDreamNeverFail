# -*- coding: UTF-8 -*-
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

#All Settings



characterdict = {0:"seraph", 1:"heiqiang", 2:"mudan", 3:"palading", 4:"msm", 5:"modao",
                 6:"wunv", 7:"guanyu", 8:"tegong", 9:"xukong", 10:"nvdaqiang", 11:"fsm",
                 12:"seraph", 13:"saint", 14:"zhaohuan", 15:"fnen",16:"indra",17:"andi",
                 18:"hongyan"}

BT = False
pickupkey = "/"


fatiguelist = {
0:273,  1:273,  2:273,  3:273,  4:170,  5:273,
6:273,  7:273,  8:273,  9:273,  10:273, 11:240,
12:200, 13:273, 14:273, 15:273, 16:273, 17:200,
18:240
}

'''Here the fatigue of each character is input'''
# repeattimedict0 = {0:math.ceil(293/8.0),     1:math.ceil(95/8.0),   2:math.ceil(293/8.0),   3:math.ceil(273/8.0),   4:math.ceil(273/8.0),   5:math.ceil(273/8.0),
#                    6:math.ceil(273/8.0),   7:math.ceil(273/8.0),   8:math.ceil(273/8.0),   9:math.ceil(273/8.0),   10:math.ceil(273/8.0),  11:math.ceil(273/8.0),

rp = {0:450, 1:450, 2:450, 3:450, 4:450, 5:450, 6:450, 7:450, 8:450, 9:450, 10:450, 11:450, 12:450, 13:450, 14:450, 15:450, 16:450, 17:450, 18:450}

'''Here we decide which characters to use'''
usinglist = [0]
# usinglist = [6,5,2,1,0]
# usinglist = [13,14]



def RobotCheck(ws):
    img_rgb = cv2.imread('c:\\temp\\bla.bmp')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('c:\\temp\\cut.bmp', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)

    if all(loc)==True:
        detectrect = (loc[0][0] + 225 - 62, loc[1][0] + 123 - 91)
        detectrect1 = (detectrect[0] + 284 - 225, detectrect[1] + 342 - 123)

        detect = img_gray[detectrect[0]:detectrect1[0], detectrect[1]:detectrect1[1]]

        # 91,62 123,225 342,284
        now = datetime.datetime.now()

        cv2.imwrite("c:\\temp\\train\\detect" + str(now.strftime("%m%d%H%M%S")) + ".bmp", detect)

    return all(loc)
    # return True

RenjiCheck = False
while(RenjiCheck == False):
    # print "Script for Gold Dragon, Start!:"
    #
    # StartGame.GameBegin()
    # time.sleep(45)
    #
    # '''Here we start the Script'''
    #
    # time.sleep(5)
    # print "OKay. Start Then--------------------------------------------------------------------------------"
    # try:
    #     I_common.closeDIE()
    # except:
    #     print "Close DIE"
    # time.sleep(10)
    #
    # for i in range(5):
    #     ws = windowsht()
    #     ws.active_window(".*Dungeon Fighter Online.*")
    #     cl = ControlWindow.windowcl()
    #     cl.move_window(ws._handle, 0, 0)
    #     time.sleep(2)
    #
    # for i in range(10):
    #     try:
    #         I_common.closeDIE()
    #     except:
    #         print "Close DIE"
    #     time.sleep(2)


    print "Move Window to left upper corner, window size is constant"
    ws = windowsht()
    ws.active_window(u"地下城与勇士")
    cl = ControlWindow.windowcl()
    cl.move_window(ws._handle, 0, 0)
    cl.click(400, 400)


    TimeUp = False

    cindex = 0
    f = open("timelog_"+str(now.day)+".txt",'w')

    repeattimedict0 = {0: math.ceil(fatiguelist[0] / 8.0), 1: math.ceil(fatiguelist[1] / 8.0),
                       2: math.ceil(fatiguelist[2] / 8.0), 3: math.ceil(fatiguelist[3] / 8.0),
                       4: math.ceil(fatiguelist[4] / 8.0), 5: math.ceil(fatiguelist[5] / 8.0),
                       6: math.ceil(fatiguelist[6] / 8.0), 7: math.ceil(fatiguelist[7] / 8.0),
                       8: math.ceil(fatiguelist[8] / 8.0), 9: math.ceil(fatiguelist[9] / 8.0),
                       10: math.ceil(fatiguelist[10] / 8.0), 11: math.ceil(fatiguelist[11] / 8.0),
                       12: math.ceil(fatiguelist[12] / 8.0), 13: math.ceil(fatiguelist[13] / 8.0),
                       14: math.ceil(fatiguelist[14] / 8.0), 15: math.ceil(fatiguelist[15] / 8.0),
                       16: math.ceil(fatiguelist[16] / 8.0), 17: math.ceil(fatiguelist[17] / 8.0),
                       18: math.ceil(fatiguelist[18] / 8.0)}

    print "The characters that will be used:"
    for c in usinglist:
        print characterdict[c] + "Timesa:" + str(int(repeattimedict0[c]))

    while cindex<len(usinglist):
        startime = time.time()
        onecharacter = usinglist[cindex]
        oc = onecharacter
        cindex = cindex+1
        repeattimes = int(repeattimedict0[onecharacter]) if int(repeattimedict0[onecharacter])>0 else 0
        print "Repeat Times:" + str(repeattimes)
        if repeattimes<5:
            print "Repeat Time smaller than 5, skip to next"
            continue
        character = characterdict[onecharacter]
        remove_pos = rp[onecharacter]

        if onecharacter>11:
            onecharacter = onecharacter-12
            print "Return to the Select Page and turn to the one we want:"
            I_move.ToSelectCharacter(ws, onecharacter, oc>=12)
            # I_move.ToSelectCharacter2(onecharacter, oc >= 12)
        else:
            print "Return to the Select Page and turn to the one we want:"
            I_move.ToSelectCharacter(ws,onecharacter)
            # I_move.ToSelectCharacter2(onecharacter)
        time.sleep(5)

        for i in range(2):
            try:
                subprocess.call('python CloseDIE.py')
                clt = ControlWindow.windowcl()
                clt.click(102, 53)
            except:
                print "closeDIE except"
            time.sleep(1)
        # if BT == True:
        #     print "Buying Tickets"
        #     endless_num = int(repeattimedict0[onecharacter]*5)
        #     I_move.BuyTickets(ws,endless_num,remove_pos)
        #     time.sleep(2)
        #     I_move.ToSelectCharacter(ws, onecharacter)

        time.sleep(4)
        print "Change to Pycharm"
        ws = windowsht()
        ws.active_window(".*PyCharm.*")
        cl = ControlWindow.windowcl()
        cl.move_window(ws._handle,0,0)
        time.sleep(4)
        print "change back to DFO"
        ws = windowsht()
        ws.active_window(u"地下城与勇士")
        cl = ControlWindow.windowcl()
        cl.move_window(ws._handle, 0, 0)


        I_move.MovetoPre(ws)

        print "Move to Map"
        inmap = I_move.stepintomap(ws)
        if inmap==False:

            for i in range(2):
                try:
                    subprocess.call('python CloseDIE.py')
                    clt = ControlWindow.windowcl()
                    clt.click(102, 53)
                except:
                    print "closeDIE except"
                time.sleep(1)
            time.sleep(1)
            ws = windowsht()
            ws.active_window(u"地下城与勇士")
            cl = ControlWindow.windowcl()
            cl.move_window(ws._handle, 0, 0)

            cindex = cindex-1
            continue

        '''Start the fight, Notice, '''
        EndDead = False
        dead = False
        for i in range(repeattimes):
            fatiguelist[oc] = fatiguelist[oc]-8

            if i==0 or dead:
                dead = False
                I_move.startgame(ws, True)
            else:
                dead = False
                I_move.startgame(ws, False)
            # if ingame(ws):
            print "Start One Map"
            count = 0
            incase = 0
            while(True):
                if I_move.infight(ws) or incase>30:
                    if incase>300:
                        print "Incase Happened"
                    incase = 0
                    print "In fight"
                    time.sleep(1.5)
                    RenjiCheck = RobotCheck(ws)
                    if RenjiCheck == True:
                        break
                    # clear_nen(ws)clear_guanyu(ws)
                    # result = clear_fswordmaster(ws)
                    result = I_move.clear(ws, character)
                    if result:
                        print "start pick"
                    else:
                        print "character dead"
                        time.sleep(25)
                        I_move.Click_Return_InMap(ws)
                        time.sleep(0.1)
                        I_move.Click_Return_InMap(ws)
                        time.sleep(5)
                        dead = True
                        if i==repeattimes-1:
                            EndDead = True
                            print "This is the DEAD END."
                            break
                        else:
                            I_move.stepintomap(ws)
                            break
                    time.sleep(0.5)
                    I_move.pickup(ws,pickupkey)
                    count = count+1
                    print "Cleared " + str(count)
                    time.sleep(0.5)
                    cl = ControlWindow.windowcl()
                    cl.move_window(ws._handle, 0, 0)
                    cl.nomal_press_keyboard("spacebar", slp=0.5)
                    if count >= 4:
                        break
                else:
                    incase = incase+1
                    time.sleep(0.1)

            if RenjiCheck==True:
                break

            time.sleep(18)
            print "Finished, Star Over"
            if datetime.datetime.now().hour == 3 and datetime.datetime.now().minute>50:
                TimeUp = True
                print "Time is UP"
                break

            if i!=repeattimes-1:
                I_move.Click_Retry(ws)
                time.sleep(0.1)
                I_move.Click_Retry(ws)
                time.sleep(0.1)
                I_move.Click_Retry(ws)
                print "Click Redo: Left Times:"+str(repeattimes-i-1)
                time.sleep(2)

        if RenjiCheck==True:
            break

        if TimeUp==True:
            print "Time is UP, approaching tommorow, so STOP."
            break

        # if EndDead==True and infight(ws) and iamdead(ws):
        #     print("DEAD AND END")
        #     time.sleep(5)
        #     cl.nomal_press_keyboard("spacebar")
        #     time.sleep(5)
        #     cl.move_window(ws._handle, 0, 0)
        #     cl.nomal_press_keyboard("esc")
        #     Click_Return_ByESC(ws)
        #     time.sleep(0.1)
        #     Click_Return_ByESC(ws)
        #     time.sleep(0.1)
        #     Click_Return_ByESC(ws)
        #     time.sleep(5)

        time.sleep(10)
        stoptime = time.time()
        f.write("Total Time for "+ character + " is: " + str(stoptime-startime) + '\n')
        print "Total Time"
        print "Finished One Character, Quit---------------------------------------------------------------"
        I_move.Click_Return_InMap(ws)
        time.sleep(0.1)
        I_move.Click_Return_InMap(ws)
        time.sleep(0.1)
        I_move.Click_Return_InMap(ws)
        time.sleep(10)

    if RenjiCheck==True:
        print "Robot Check Happened, will restart the game"
        for i in range(3):
            try:
                cl.close_window(ws._handle)
                time.sleep(5)
                cl.nomal_press_keyboard("enter")
                cl.nomal_press_keyboard("enter")
                print "game closed, wait 5 min"
                time.sleep(300)
            except:
                print "close window wrong"
        RenjiCheck = False
        continue

    print "Finished All!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "Close the game."
    cl.move_window(ws._handle, 0, 0)
    cl.nomal_press_keyboard("esc", slp=0.5)
    time.sleep(1)
    cl.click(624,392)
    time.sleep(1)
    cl.click(442,326)
    RenjiCheck = True
    time.sleep(10)
    print "Closed"

print("Finished")
