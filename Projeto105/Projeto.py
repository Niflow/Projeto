##importando as blibliotecas OSCV2
import os
import cv2


caminho="imagens/"
Images = [ ]

##For e um lupi que fica dando voltas
for file in os.listdir(caminho):
    name,xt= os.path.splitext(file) ##essa linha estar separando o nome do file em nome e extensao
    if xt in [".gif",".jpeg",".jpg","png"]: ##estar verificando a extensao que ta guardada na variavel xt
        filename= caminho+file    
        Images.append(filename) ##colocando dentro o nome da imagem "vetor"


frame=cv2.imread(Images[0])
print(frame)
height,width,layer=frame.shape
size=(width,height)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in  range(0,len(Images)):

    frame=cv2.imread(Images[i])

    out.write(frame)

out.release()    
