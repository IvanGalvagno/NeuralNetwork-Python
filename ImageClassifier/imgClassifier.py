import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#import image
i = Image.open('ImageClassifier/images/numbers/y0.4.png')
#Transforma a Imagem e Array, Aonde cada bloco é uma Linha da imagem
iar = np.asarray(i)
print(iar)
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

imgplot = plt.imshow(iar)
#plt.show(imgplot)
#plt.show(plt.colorbar())
print(imgplot)
plt.show(imgplot)