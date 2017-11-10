import numpy as np
from PIL import Image

#import image
i = Image.open('ImageClassifier/images/dot.png')
#Transforma a Imagem e Array, Aonde cada bloco é uma Linha da imagem
iar = np.asarray(i)
print(iar)