##importando as blibliotecas OSCV2
import os
import cv2


caminho="/imagens/imagens"
Images = [ ]
for file in os.listdir(caminho):
    name,xt= os.path.splitext(file)
    print(name)
