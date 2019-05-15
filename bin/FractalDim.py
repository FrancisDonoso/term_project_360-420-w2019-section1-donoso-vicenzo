#import bs
import matplotlib.pyplot as plt
from PIL import Image
import math
import numpy as np

def checkblock(x,y,pixpblo):
    pixpblo = (int)(pixpblo)
    x = (int)(x)
    y = (int)(y)
    for a in range(0,pixpblo):
        for b in range(0,pixpblo):
            posx = x + b
            posy = y + a
            pos = (posx,posy)
            print("pixpblo: " + (str)(pixpblo) + " checked (" + (str)(posx) + ", " + (str)(posy) + ")")
            if im.getpixel(pos) != (0) and im.getpixel(pos) != (255): # put 0 and 255 for all images except
                print(im.getpixel(pos))                           # for Sierpinski Triangle, replace 0 with 1
                return 1
    return 0

######################################

im = Image.open("circle512.png")
print (im.format, im.size, im.mode)
im.show()

imasize = im.size[0]
pixpblo = (int)((imasize)//2)
blocknum = 2
ans = []

while (pixpblo >= 1):
    filled = 0
    x = 0
    y = 0
    for i in range(0,blocknum):
        for n in range(0,blocknum):
            filled = filled + checkblock(x,y,pixpblo)
            print(filled)
            x = x + pixpblo
        x = 0
        y = y + pixpblo
    ans.append(filled)
    blocknum = 2*blocknum
    pixpblo = pixpblo/2
print(ans)

######################################
double = 2
filledvalues = []
scalevalues = []
regression = []
for i in range(0,len(ans)):

    filledvalues.append(math.log1p(ans[i]-1))
    scalevalues.append(math.log1p(double-1))
    double = 2*double

print(filledvalues)
print(scalevalues)
m,b = np.polyfit(scalevalues,filledvalues,1)

for i in range(0,len(ans)):
    plt.plot(scalevalues[i],filledvalues[i],'bo')
    regression.append(m*scalevalues[i]+b)

str = (str)(m)
plt.xlabel('Log of Scaling Factor')
plt.ylabel('Log of Volume Ratio')
plt.plot(scalevalues, regression)
plt.title('Slope for Circle = ' + str)
plt.show()
