import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *


electroNeutro = pd.read_csv("Sujeto16/Neutrales/electroNeutroSujeto16.csv")
electroRecu = pd.read_csv("Sujeto16/Recuperadoras/electroRecuSujeto16.csv")
electroVideo = pd.read_csv("Sujeto16/Video/electroVideoSujeto16.csv")


tiempoElectroNeutro = electroNeutro['Tiempo']
amplitudElectroNeutro = electroNeutro['RmsElectro']

tiempoElectroRecu = electroRecu['Tiempo']
amplitudElectroRecu = electroRecu['RmsElectro']

tiempoElectroVideo = electroVideo['Tiempo']
amplitudElectroVideo = electroVideo['RmsElectro']


datosTiempoElectroNeutro = tiempoElectroNeutro.iloc[0:43127]
datosAmpliElectroNeutro = amplitudElectroNeutro.iloc[0:43127]

datosTiempoElectroRecu = tiempoElectroRecu.iloc[0:45559]
datosAmpliElectroRecu = amplitudElectroRecu.iloc[0:45559]

datosTiempoElectroVideo = tiempoElectroVideo.iloc[0:79319]
datosAmpliElectroVideo = amplitudElectroVideo.iloc[0:79319]


plt.xlabel("Hora")
plt.ylabel("Neutro/Recuperación/Video")
p1, p2,p3 = plot(datosTiempoElectroNeutro,datosAmpliElectroNeutro,datosTiempoElectroRecu,datosAmpliElectroRecu,datosTiempoElectroVideo,datosAmpliElectroVideo)
texto1 = text(175, 2.25, "Gráfica Electro Video(verde) ", fontsize=8)
texto2 = text(175, 2.125, "Gráfica Electro Recuperación(naranja)" , fontsize=8)
texto3 = text (175,2, "Gráfica Electro Neutro(azul)", fontsize=8 )
plt.title("Gráfica Comparación Electro Sujeto 16")
plt.savefig("Sujeto16/Comparaciones/GraficaComparacionElectroSujeto16.jpg", bbox_inches = 'tight')

plt.show()

