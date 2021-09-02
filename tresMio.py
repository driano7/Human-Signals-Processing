import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *


mioNeutro = pd.read_csv("Sujeto16/Neutrales/mioNeutroSujeto16.csv")
mioRecu = pd.read_csv("Sujeto16/Recuperadoras/mioRecuSujeto16.csv")
mioVideo = pd.read_csv("Sujeto16/Video/mioVideoSujeto16.csv")


tiempoMioNeutro = mioNeutro['Tiempo']
amplitudMioNeutro = mioNeutro['MyoScan-Z']

tiempoMioRecu = mioRecu['Tiempo']
amplitudMioRecu = mioRecu['MyoScan-Z']

tiempoMioVideo = mioVideo['Tiempo']
amplitudMioVideo = mioVideo['MyoScan-Z']


datosTiempoMioNeutro = tiempoMioNeutro.iloc[0:345088]
datosAmpliMioNeutro = amplitudMioNeutro.iloc[0:345088]

datosTiempoMioRecu = tiempoMioRecu.iloc[0:364544]
datosAmpliMioRecu = amplitudMioRecu.iloc[0:364544]

datosTiempoMioVideo = tiempoMioVideo.iloc[0:500000]
datosAmpliMioVideo = amplitudMioVideo.iloc[0:500000]


plt.xlabel("Hora")
plt.ylabel("Neutro/Recuperación/Video")
p1, p2,p3 = plot(datosTiempoMioNeutro,datosAmpliMioNeutro,datosTiempoMioRecu,datosAmpliMioRecu,datosTiempoMioVideo,datosAmpliMioVideo)
texto1 = text(180, 850, "Gráfica Mio Video (verde) ", fontsize=7)
texto2 = text(180, 950, "Gráfica Mio Recu(naranja)" , fontsize=7)
texto3 = text (180, 1050, "Gráfica Mio Neutro (azul)", fontsize=7 )
plt.title("Gráfica Comparación Mio Sujeto 16")
plt.savefig("Sujeto16/Comparaciones/GraficaComparacionMioSujeto16.jpg", bbox_inches = 'tight')

plt.show()
