import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *


surveys_df = pd.read_csv("Sujeto16/Video/electroVideoSujeto16.csv")

tiempo = surveys_df['Tiempo']
amplitud = surveys_df['RmsElectro']

datosTiempo = tiempo.iloc[0:79319]
datosAmpli = amplitud.iloc[0:79319]

plt.xlabel("RMS")
plt.ylabel("Hora")
plt.bar(datosAmpli,datosTiempo, color = 'yellow')
plt.title("Gráfica Video Electro Sujeto 16")
plt.savefig("Sujeto16/Video/GráficaVideoElectroSujeto16.jpg", bbox_inches = 'tight')
plt.show()

