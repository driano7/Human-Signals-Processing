import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *


mioNeutro = pd.read_csv("Sujeto15/Neutrales/mioNeutroSujeto15.csv")
mioRecu = pd.read_csv("Sujeto15/Recuperadoras/mioRecuSujeto15.csv")
mioVideo = pd.read_csv("Sujeto15/Video/mioVideoSujeto15.csv")


tiempoMioNeutro = mioNeutro['Tiempo']
amplitudMioNeutro = mioNeutro['MyoScan-Z']

tiempoMioRecu = mioRecu['Tiempo']
amplitudMioRecu = mioRecu['MyoScan-Z']

tiempoMioVideo = mioVideo['Tiempo']
amplitudMioVideo = mioVideo['MyoScan-Z']


datosTiempoMioNeutro = tiempoMioNeutro.iloc[0:500000]
datosAmpliMioNeutro = amplitudMioNeutro.iloc[0:500000]

datosTiempoMioRecu = tiempoMioRecu.iloc[0:500000]
datosAmpliMioRecu = amplitudMioRecu.iloc[0:500000]

datosTiempoMioVideo = tiempoMioVideo.iloc[0:500000]
datosAmpliMioVideo = amplitudMioVideo.iloc[0:500000]


plt.subplot(1,3,1)
#p1, p2,p3 = plot(datosTiempoElectroNeutro,datosAmpliElectroNeutro,datosTiempoElectroRecu,datosAmpliElectroRecu,datosTiempoElectroVideo,datosAmpliElectroVideo)
p1 = plot(datosTiempoMioNeutro,datosAmpliMioNeutro, label = 'Gráfica Electro Neutro',color = 'blue')
plt.ylabel("Intensidad", fontsize=12)
plt.legend()
plt.grid(True)

plt.subplot(1,3,2)
p2 = plot(datosTiempoMioVideo,datosAmpliMioVideo, label = 'Gráfica Comparación Electro Sujeto 16',color = 'orange')
plt.legend()
plt.grid(True)

plt.xlabel("Hora\nNeutro/Video/Recuperación", fontsize=12)

plt.title("Gráfica Comparaciones Mioeléctrica Sujeto 15")

plt.subplot(1,3,3)
p3= plot (datosTiempoMioRecu,datosAmpliMioRecu,label = 'Gráfica Electro Recuperación', color = 'green')
plt.legend()
plt.grid(True)

plt.show()

