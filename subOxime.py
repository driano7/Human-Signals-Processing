import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *


oximeNeutro = pd.read_csv("Sujeto15/Neutrales/oximeNeutroSujeto15.csv")
oximeRecu = pd.read_csv("Sujeto15/Recuperadoras/oximeRecuSujeto15.csv")
oximeVideo = pd.read_csv("Sujeto15/Video/oximeVideoSujeto15.csv")


tiempoOximeNeutro = oximeNeutro['Tiempo']
amplitudOximeNeutro = oximeNeutro['Oxime']

tiempoOximeRecu = oximeRecu['Tiempo']
amplitudOximeRecu = oximeRecu['Oxime']

tiempoOximeVideo = oximeVideo['Tiempo']
amplitudOximeVideo = oximeVideo['Oxime']


datosTiempoOximeNeutro = tiempoOximeNeutro.iloc[0:500000]
datosAmpliOximeNeutro = amplitudOximeNeutro.iloc[0:500000]

datosTiempoOximeRecu = tiempoOximeRecu.iloc[0:500000]
datosAmpliOximeRecu = amplitudOximeRecu.iloc[0:500000]

datosTiempoOximeVideo = tiempoOximeVideo.iloc[0:500000]
datosAmpliOximeVideo = amplitudOximeVideo.iloc[0:500000]


plt.subplot(1,3,1)
#p1, p2,p3 = plot(datosTiempoElectroNeutro,datosAmpliElectroNeutro,datosTiempoElectroRecu,datosAmpliElectroRecu,datosTiempoElectroVideo,datosAmpliElectroVideo)
p1 = plot(datosTiempoOximeNeutro,datosAmpliOximeNeutro, label = 'Gráfica Electro Neutro',color = 'blue')
plt.ylabel("Intensidad", fontsize=12)
plt.legend()
plt.grid(True)

plt.subplot(1,3,2)
p2 = plot(datosTiempoOximeRecu,datosAmpliOximeRecu, label = 'Gráfica Comparación Electro Sujeto 16',color = 'orange')
plt.legend()
plt.grid(True)

plt.xlabel("Hora\nNeutro/Video/Recuperación", fontsize=12)

plt.title("Gráfica Comparaciones Oximetría Sujeto 15")

plt.subplot(1,3,3)
p3= plot (datosTiempoOximeVideo,datosAmpliOximeVideo,label = 'Gráfica Electro Recuperación', color = 'green')
plt.legend()
plt.grid(True)

plt.show()

