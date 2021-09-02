import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *
from PIL import Image

electroNeutro = pd.read_csv("Sujeto15/Neutrales/electroNeutroSujeto15.csv")
electroRecu = pd.read_csv("Sujeto15/Recuperadoras/electroRecuSujeto15.csv")
electroVideo = pd.read_csv("Sujeto15/Video/electroVideoSujeto15.csv")


tiempoElectroNeutro = electroNeutro['Tiempo']
amplitudElectroNeutro = electroNeutro['RmsElectro']

tiempoElectroRecu = electroRecu['Tiempo']
amplitudElectroRecu = electroRecu['RmsElectro']

tiempoElectroVideo = electroVideo['Tiempo']
amplitudElectroVideo = electroVideo['RmsElectro']


datosTiempoElectroNeutro = tiempoElectroNeutro.iloc[0:82000]
datosAmpliElectroNeutro = amplitudElectroNeutro.iloc[0:82000]

datosTiempoElectroRecu = tiempoElectroRecu.iloc[0:82000]
datosAmpliElectroRecu = amplitudElectroRecu.iloc[0:82000]

datosTiempoElectroVideo = tiempoElectroVideo.iloc[0:82000]
datosAmpliElectroVideo = amplitudElectroVideo.iloc[0:82000]


plt.subplot(1,3,1)
#p1, p2,p3 = plot(datosTiempoElectroNeutro,datosAmpliElectroNeutro,datosTiempoElectroRecu,datosAmpliElectroRecu,datosTiempoElectroVideo,datosAmpliElectroVideo)
p1 = plot(datosTiempoElectroNeutro,datosAmpliElectroNeutro, label = 'Gráfica Electro Neutro',color = 'blue')
plt.ylabel("Intensidad", fontsize=12)
plt.legend()
plt.grid(True)

plt.subplot(1,3,2)
p2 = plot(datosTiempoElectroVideo,datosAmpliElectroVideo, label = 'Gráfica Comparación Electro Sujeto 16',color = 'orange')
plt.legend()
plt.grid(True)

plt.xlabel("Hora\nNeutro/Video/Recuperación", fontsize=12)

plt.title("Gráfica Comparaciones Electro Sujeto 15")

plt.subplot(1,3,3)
p3= plot (datosTiempoElectroRecu,datosAmpliElectroRecu,label = 'Gráfica Electro Recuperación', color = 'green')
#plt.savefig("Sujeto16/Comparaciones/GraficaSubElectroSujeto16.jpg", bbox_inches = 'tight')

plt.legend()
plt.grid(True)

plt.show()
