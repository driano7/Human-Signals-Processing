import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *


surveys_df = pd.read_csv("Sujeto16/Video/oximeVideoSujeto16.csv")

tiempo = surveys_df['Tiempo']
amplitud = surveys_df['Oxime']

datosTiempo = tiempo.iloc[0:500000]
datosAmpli = amplitud.iloc[0:500000]

plt.xlabel("Oxime")
plt.ylabel("Hora")
plt.bar(datosAmpli,datosTiempo, color = 'yellow')
plt.title("Gráfica Video Oximetría Sujeto 16")
plt.savefig("Sujeto16/Video/GráficaVideoOximeSujeto16.jpg", bbox_inches = 'tight')
plt.show()


