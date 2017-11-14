import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import functools

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

def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numberWeHave = range(1,10)
    versionsWeHave = range(1,10)
    for eachNum in numberWeHave:
        for eachVer in versionsWeHave:
            imgFilePath = 'images/numbers/'+ str(eachNum)+ "." + str(eachVer)+ '.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())
            lineToWrite = str(eachNum)+'::'+eiar1+'\n'
            numberArrayExamples.write(lineToWrite)


#TRANSFOR IMAGE IN BLACK AND WHITE
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            # print(eachPix)
            # time.sleep(1)
            avgNum = functools.reduce(lambda x,y: x+y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = functools.reduce(lambda x,y: x+y, balanceAr) / len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if( functools.reduce(lambda x,y: x+y, eachPix[:3]) / len(eachPix[:3]) > balance):
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

threshold(iar)
threshold(iar2)
threshold(iar3)
threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)
ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()

createExamples()

