from Basis import Admin

if not Admin.isUserAdmin():
    Admin.runAsAdmin()

from Basis.CaptureWindow import windowsht
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


ws = windowsht()
ws.active_window(".*Dungeon Fighter Online.*")
ws.capture_window(960,600)



import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('c:\\temp\\bbb.bmp')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('c:\\temp\\cut.bmp',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('c:\\temp\\res.png',img_rgb)

# # capimg = misc.imread("c:\\temp\\bla.bmp",flatten=True)
# cl = ControlWindow.windowcl()
# cl.move_window(ws._handle, 0, 0)
# cl.nomal_press_keyboard("/", slp=1)
#
# def rgb2gray(rgb):
#     return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
# capimg = misc.imread("c:\\temp\\bla.bmp")
# cutcapimg = capimg[563:590]
# skill = capimg[563:590,613:639]
# skillyellow = skill.copy()
# skillgray = rgb2gray(skill)
# zeros = np.count_nonzero(skillgray==255)
# # If smaller than 5, means avaliable
# skillyellow[:,:,2] = 0
# meanskill = np.mean(skill)
# meanskillyellow = np.mean(skillyellow)

# leftitem = misc.imread("leftitem.bmp",flatten=True)
# rightitem = misc.imread("rightitem.bmp",flatten=True)
gold = misc.imread("gold.bmp",flatten=True)
# capimg = misc.imread("c:\\temp\\bla.bmp", flatten=True)
# leftitem = capimg[374:399,466:474]
# rightitem = capimg[374:399,578:587]
# character = capimg[250:372,200:250]



# plt.imshow(capimg)
plt.show()

# charactermatrix = misc.imread("character1.bmp", flatten=True)
# grad = signal.convolve2d(capimg, charactermatrix, boundary='symm', mode='same')
# np.unravel_index(grad.argmax(),grad.shape)

# leftmatrix = signal.convolve2d(capimg,leftitem, boundary='symm', mode='same')
# leftpos = np.unravel_index(leftmatrix.argmax(),leftmatrix.shape)
# rightmatrix = signal.convolve2d(capimg,rightitem, boundary='symm', mode='same')
# rightpos = np.unravel_index(rightmatrix.argmax(),rightmatrix.shape)
goldmatrix = signal.convolve2d(cutcapimg,gold, boundary='symm', mode='same')
goldpos = np.unravel_index(goldmatrix.argmax(),goldmatrix.shape)

print "finished"