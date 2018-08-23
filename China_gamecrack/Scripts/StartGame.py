import os
from Basis import ControlWindow
from Basis.CaptureWindow import windowsht
import subprocess
import time
import keyboard

def GameBegin():
    time.sleep(5)
    #Indicate DFO path
    GamePath = "D:\Neople\DFO\NeopleLauncher.exe"
    subprocess.Popen(GamePath)
    print "1"
    time.sleep(15)
    print 2
    ws = windowsht()
    ws.active_window(".*Dungeon Fighter Online.*")
    print 3
    time.sleep(5)
    print 4

    AccountPos = (1300,300)
    PasswordPos = (1300,333)
    LoginPos = (1300,366)
    StartPos = (1300,250)

    cl = ControlWindow.windowcl()
    cl.click(AccountPos[0],AccountPos[1])
    time.sleep(0.1)
    cl.click(AccountPos[0],AccountPos[1])
    time.sleep(0.1)
    cl.click(AccountPos[0],AccountPos[1])

    time.sleep(3)
    Account = "qijia2045579@gmail.com"
    AccountA = "5fugitive8"
    AccountB = "gmail.com"
    # cl.nomal_input(AccountA)
    # cl.nomal_press_down("shift",slp=1)
    # cl.nomal_press_keyboard("2")
    # cl.nomal_press_down("shift",slp=1)
    # cl.nomal_input(AccountB)
    keyboard.write(Account)

    time.sleep(3)
    cl = ControlWindow.windowcl()
    cl.click(PasswordPos[0],PasswordPos[1])
    time.sleep(0.1)
    cl.click(PasswordPos[0],PasswordPos[1])
    time.sleep(0.1)
    cl.click(PasswordPos[0],PasswordPos[1])
    time.sleep(3)
    Password = "Qisini2045579"
    keyboard.write(Password)

    time.sleep(3)


    cl = ControlWindow.windowcl()
    cl.click(LoginPos[0],LoginPos[1])
    time.sleep(0.1)
    cl.click(LoginPos[0],LoginPos[1])

    time.sleep(3)


    cl = ControlWindow.windowcl()
    cl.click(StartPos[0],StartPos[1])
    time.sleep(0.1)
    cl.click(StartPos[0],StartPos[1])

    print "started"