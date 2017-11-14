import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

#import image
# i = Image.open('ImageClassifier/images/numbers/y0.4.png')
#Transforma a Imagem e Array, Aonde cada bloco é uma Linha da imagem
# iar = np.asarray(i)
# print(iar)
# UM PIXEL DA IMAGEM .DOT que é 8x8
#    R    G   B  Alpha
#   [  0   0   0 255]
#   [255 255 255 255]
#   [255 255 255 255]
#   [255 255 255 255]
#   [255 255 255 255]
#   [255 255 255 255]
#   [255 255 255 255]
#   [255 255 255 255]
#  Os numeros representam uma colocarao em determinado pixel

# imgplot = plt.imshow(iar)
#plt.show(imgplot)
#plt.show(plt.colorbar())
# print(imgplot)
# plt.show(imgplot)

def threshold(imageArray):
    blanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            # print(eachPix)
            # time.sleep(1)
            avgNum = reduce(lambda x,y: x+y, eachPix[:3]) / len(eachPix[:3])
            blanceAr.append(avgNum)
    balance = reduce(lambda x,y: x+y, blanceAr) / len(blanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if( reduce(lambda x,y: x+y, eachPix[:3]) / len(eachPix[:3]) > balance):
                eachPix[0] = 255  #RED
                eachPix[1] = 255  #GREEN
                eachPix[2] = 255  #BLUE
                eachPix[3] = 255  #alpha
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr
                

i = Image.open('ImageClassifier/images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('ImageClassifier/images/numbers/y0.5.png')
iar2 = np.array(i2)

i3 = Image.open('ImageClassifier/images/numbers/y0.4.png')
iar3 = np.array(i3)

i4 = Image.open('ImageClassifier/images/sentdex.png')
iar4 = np.array(i4)


threshold(iar3)

# fig = plt.figure()
# ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
# ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
# ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
# ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

# ax1.imshow(iar)
# ax2.imshow(iar2)
# ax3.imshow(iar3)
# ax4.imshow(iar4)

# plt.show()


