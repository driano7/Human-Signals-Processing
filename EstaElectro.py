import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.pyplot import *
from scipy import stats # importando scipy.stats


surveys_df = pd.read_csv("Sujeto16/Video/electroVideoSujeto16.csv")

tiempoElectro = surveys_df['Tiempo']
amplitudElectro = surveys_df['RmsElectro']

datosTiempoElectro = tiempoElectro.iloc[0:79319]
datosAmpliElectro = amplitudElectro.iloc[0:79319]

archivo = open ('Sujeto16/Esta_Electro_16.txt', 'a')

print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoElectro))
archivo.write('Media Aritmética del Tiempo:   ')
medTimeElectro = str(np.mean(datosTiempoElectro))
archivo.write(medTimeElectro)


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliElectro)) 
archivo.write('\n\nMedia Aritmética de la Intensidad:    ')
medAmpliElectro = str(np.mean(datosAmpliElectro))
archivo.write(medAmpliElectro)


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoElectro)) 
archivo.write('\n\nMediana del Tiempo:    ')
medianaTiempoElectro = str(np.median(datosTiempoElectro))
archivo.write(medianaTiempoElectro)


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliElectro)) 
archivo.write('\n\nMediana de la Intensidad:    ')
medianaAmpliElectro = str(np.median(datosAmpliElectro))
archivo.write(medianaAmpliElectro)


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoElectro)) 
archivo.write('\n\nDesviación típica del Tiempo:    ')
desTiempoElectro = str(np.std(datosTiempoElectro))
archivo.write(desTiempoElectro)


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliElectro)) 
archivo.write('\n\nDesviación típica de la Intensidad:    ')
desAmpliElectro = str(np.std(datosAmpliElectro))
archivo.write(desAmpliElectro)


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoElectro)) 
archivo.write('\n\nVarianza del Tiempo:    ')
varTiempoElectro = str(np.var(datosTiempoElectro))
archivo.write(varTiempoElectro)


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliElectro)) 
archivo.write('\n\nVarianza de la Intensidad:    ')
varAmpliElectro = str(np.var(datosAmpliElectro))
archivo.write(varAmpliElectro)


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoElectro))
archivo.write('\n\nModa del Tiempo:    ')
modaTiempoElectro = str(stats.mode(datosTiempoElectro))
archivo.write(modaTiempoElectro)


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliElectro))
archivo.write('\n\nModa de la Intensidad:    ')
modaAmpliElectro = str(stats.mode(datosAmpliElectro))
archivo.write(modaAmpliElectro)


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoElectro))
archivo.write('\n\nCorrelación del Tiempo:    ')
corTiempoElectro = str(np.corrcoef(datosTiempoElectro))
archivo.write(corTiempoElectro)


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliElectro)) 
archivo.write('\n\nCorrelaciónde la Intensidad:    ')
corAmpliElectro = str(np.corrcoef(datosAmpliElectro))
archivo.write(corAmpliElectro)


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoElectro, datosAmpliElectro)) 
archivo.write('\n\nCorrelación de los datos:    ')
corrElectro = str(np.corrcoef(datosTiempoElectro,datosAmpliElectro))
archivo.write(corrElectro)


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoElectro)) 
archivo.write('\n\nCovarianza del Tiempo:    ')
covTiempoElectro = str(np.cov(datosTiempoElectro))
archivo.write(covTiempoElectro)


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliElectro)) 
archivo.write('\n\nCovarianza de la Intensidad:    ')
covAmpliElectro = str(np.cov(datosAmpliElectro))
archivo.write(covAmpliElectro)


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoElectro, datosAmpliElectro))
archivo.write('\n\nCovarianza de los dos vectores:    ')
covElectro = str(np.cov(datosTiempoElectro,datosAmpliElectro))
archivo.write(covElectro)


archivo.close()
        