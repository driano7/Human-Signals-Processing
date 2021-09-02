import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *


surveys_df = pd.read_csv("Sujeto16/Video/mioVideoSujeto16.csv")

tiempo = surveys_df['Tiempo']
amplitud = surveys_df['MyoScan-Z']

datosTiempo = tiempo.iloc[0:500000]
datosAmpli = amplitud.iloc[0:500000]

plt.xlabel("MyoScan-Z")
plt.ylabel("Hora")
plt.bar(datosAmpli,datosTiempo, color = 'yellow')
plt.title("Gráfica Video Mio Sujeto 16")
plt.savefig("Sujeto16/Video/GráficaVideoMioSujeto16.jpg", bbox_inches = 'tight')
plt.show()

