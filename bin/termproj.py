#import bs
import matplotlib.pyplot as plt
from PIL import Image
import math

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
            if im.getpixel(pos) != (0,0) and im.getpixel(pos) != (255,255):
                print(im.getpixel(pos))
                return 1
    return 0



######################################
im = Image.open("holyshitUK.png")
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
            filled = filled + checkblock(x,y,pixpblo)     #[4, 10, 30, 100, 329, 1177, 4336, 16512]
            x = x + pixpblo
        x = 0
        y = y + pixpblo
    ans.append(filled)
    blocknum = 2*blocknum
    pixpblo = pixpblo/2
print(ans)

######################################

nvalues = []
indvalues = []
for i in range(0,len(ans)-1):
    n = math.log1p(((ans[i])/(ans[i+1]))-1)/math.log1p(0.5-1)
    nvalues.append(n)
    indvalues.append(i+2)

print(nvalues)
print(indvalues)
plt.plot(indvalues,nvalues)
plt.show()