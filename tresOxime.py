import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *


oximeNeutro = pd.read_csv("Sujeto16/Neutrales/oximeNeutroSujeto16.csv")
oximeRecu = pd.read_csv("Sujeto16/Recuperadoras/oximeRecuSujeto16.csv")
oximeVideo = pd.read_csv("Sujeto16/Video/oximeVideoSujeto16.csv")


tiempoOximeNeutro = oximeNeutro['Tiempo']
amplitudOximeNeutro = oximeNeutro['Oxime']

tiempoOximeRecu = oximeRecu['Tiempo']
amplitudOximeRecu = oximeRecu['Oxime']

tiempoOximeVideo = oximeVideo['Tiempo']
amplitudOximeVideo = oximeVideo['Oxime']


datosTiempoOximeNeutro = tiempoOximeNeutro.iloc[0:345088]
datosAmpliOximeNeutro = amplitudOximeNeutro.iloc[0:345088]

datosTiempoOximeRecu = tiempoOximeRecu.iloc[0:364544]
datosAmpliOximeRecu = amplitudOximeRecu.iloc[0:364544]

datosTiempoOximeVideo = tiempoOximeVideo.iloc[0:500000]
datosAmpliOximeVideo = amplitudOximeVideo.iloc[0:500000]


plt.xlabel("Hora")
plt.ylabel("Neutro/Recuperación/Video")
p1, p2,p3 = plot(datosTiempoOximeNeutro,datosAmpliOximeNeutro,datosTiempoOximeRecu,datosAmpliOximeRecu,datosTiempoOximeVideo,datosAmpliOximeVideo)
texto1 = text(120, 10, "Gráfica Oximetría Video (verde) ", fontsize=10)
texto2 = text(120, 5, "Gráfica Oximetría Recu(naranja)" , fontsize=10)
texto3 = text (120, 0, "Gráfica Oximetría Neutro (azul)", fontsize=10 )
plt.title("Gráfica Comparación Oximetría Sujeto 16")
plt.savefig("Sujeto16/Comparaciones/GraficaComparacionOximeSujeto16.jpg", bbox_inches = 'tight')

plt.show()
