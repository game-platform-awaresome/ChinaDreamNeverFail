from Basis import Admin
if not Admin.isUserAdmin():
    Admin.runAsAdmin()
from Basis import ControlWindow
from Basis.CaptureWindow import windowsht
from scipy import misc
import time
import math
import datetime
from Tkinter import *
import sys

root=Tk()
root.title("GoldDragon Script Runner")
text = Text(root)
text.grid()
root.mainloop()

