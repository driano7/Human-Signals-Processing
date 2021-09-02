import pandas as pd 
import numpy as np
from scipy import stats
from pandas import ExcelWriter


electroNeutro = pd.read_csv("Sujeto14/Neutrales/electroNeutroSujeto14.csv")
electroRecu = pd.read_csv("Sujeto14/Recuperadoras/electroRecuSujeto14.csv")
electroVideo = pd.read_csv("Sujeto14/Video/electroVideoSujeto14.csv")


tiempoElectroNeutro = electroNeutro['Tiempo']
amplitudElectroNeutro = electroNeutro['RmsElectro']

tiempoElectroRecu = electroRecu['Tiempo']
amplitudElectroRecu = electroRecu['RmsElectro']

tiempoElectroVideo = electroVideo['Tiempo']
amplitudElectroVideo = electroVideo['RmsElectro']


datosTiempoElectroNeutro = tiempoElectroNeutro.iloc[0:44272]
datosAmpliElectroNeutro = amplitudElectroNeutro.iloc[0:44272]

datosTiempoElectroRecu = tiempoElectroRecu.iloc[0:42816]
datosAmpliElectroRecu = amplitudElectroRecu.iloc[0:42816]

datosTiempoElectroVideo = tiempoElectroVideo.iloc[0:79008]
datosAmpliElectroVideo = amplitudElectroVideo.iloc[0:79008]

print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoElectroNeutro))
medTimeElectroNeutro = str(np.mean(datosTiempoElectroNeutro))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliElectroNeutro)) 
medAmpliElectroNeutro = str(np.mean(datosAmpliElectroNeutro))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoElectroNeutro)) 
medianaTiempoElectroNeutro = str(np.median(datosTiempoElectroNeutro))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliElectroNeutro)) 
medianaAmpliElectroNeutro = str(np.median(datosAmpliElectroNeutro))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoElectroNeutro)) 
desTiempoElectroNeutro = str(np.std(datosTiempoElectroNeutro))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliElectroNeutro)) 
desAmpliElectroNeutro = str(np.std(datosAmpliElectroNeutro))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoElectroNeutro)) 
varTiempoElectroNeutro = str(np.var(datosTiempoElectroNeutro))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliElectroNeutro)) 
varAmpliElectroNeutro = str(np.var(datosAmpliElectroNeutro))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoElectroNeutro))
modaTiempoElectroNeutro = str(stats.mode(datosTiempoElectroNeutro))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliElectroNeutro))
modaAmpliElectroNeutro = str(stats.mode(datosAmpliElectroNeutro))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoElectroNeutro))
corTiempoElectroNeutro = str(np.corrcoef(datosTiempoElectroNeutro))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliElectroNeutro)) 
corAmpliElectroNeutro = str(np.corrcoef(datosAmpliElectroNeutro))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoElectroNeutro, datosAmpliElectroNeutro)) 
corrElectroNeutro = str(np.corrcoef(datosTiempoElectroNeutro,datosAmpliElectroNeutro))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoElectroNeutro)) 
covTiempoElectroNeutro = str(np.cov(datosTiempoElectroNeutro))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliElectroNeutro)) 
covAmpliElectroNeutro = str(np.cov(datosAmpliElectroNeutro))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoElectroNeutro, datosAmpliElectroNeutro))
covAmpliElectroNeutro = str(np.cov(datosTiempoElectroNeutro,datosAmpliElectroNeutro))





print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoElectroRecu))
medTimeElectroRecu = str(np.mean(datosTiempoElectroRecu))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliElectroRecu)) 
medAmpliElectroRecu = str(np.mean(datosAmpliElectroRecu))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoElectroRecu)) 
medianaTiempoElectroRecu = str(np.median(datosTiempoElectroRecu))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliElectroRecu)) 
medianaAmpliElectroRecu = str(np.median(datosAmpliElectroRecu))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoElectroRecu)) 
desTiempoElectroRecu = str(np.std(datosTiempoElectroRecu))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliElectroRecu)) 
desAmpliElectroRecu = str(np.std(datosAmpliElectroRecu))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoElectroRecu)) 
varTiempoElectroRecu = str(np.var(datosTiempoElectroRecu))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliElectroRecu)) 
varAmpliElectroRecu = str(np.var(datosAmpliElectroRecu))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoElectroRecu))
modaTiempoElectroRecu = str(stats.mode(datosTiempoElectroRecu))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliElectroRecu))
modaAmpliElectroRecu = str(stats.mode(datosAmpliElectroRecu))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoElectroRecu))
corTiempoElectroRecu = str(np.corrcoef(datosTiempoElectroRecu))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliElectroRecu)) 
corAmpliElectroRecu = str(np.corrcoef(datosAmpliElectroRecu))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoElectroRecu, datosAmpliElectroRecu)) 
corrElectroRecu = str(np.corrcoef(datosTiempoElectroRecu,datosAmpliElectroRecu))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoElectroRecu)) 
covTiempoElectroRecu = str(np.cov(datosTiempoElectroRecu))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliElectroRecu)) 
covAmpliElectroRecu = str(np.cov(datosAmpliElectroRecu))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoElectroRecu, datosAmpliElectroRecu))
covElectroRecu = str(np.cov(datosTiempoElectroRecu,datosAmpliElectroRecu))





print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoElectroVideo))
medTimeElectroVideo = str(np.mean(datosTiempoElectroVideo))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliElectroVideo)) 
medAmpliElectroVideo = str(np.mean(datosAmpliElectroVideo))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoElectroVideo)) 
medianaTiempoElectroVideo = str(np.median(datosTiempoElectroVideo))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliElectroVideo)) 
medianaAmpliElectroVideo = str(np.median(datosAmpliElectroVideo))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoElectroVideo)) 
desTiempoElectroVideo = str(np.std(datosTiempoElectroVideo))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliElectroVideo)) 
desAmpliElectroVideo = str(np.std(datosAmpliElectroVideo))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoElectroVideo)) 
varTiempoElectroVideo = str(np.var(datosTiempoElectroVideo))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliElectroVideo)) 
varAmpliElectroVideo = str(np.var(datosAmpliElectroVideo))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoElectroVideo))
modaTiempoElectroVideo = str(stats.mode(datosTiempoElectroVideo))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliElectroVideo))
modaAmpliElectroVideo = str(stats.mode(datosAmpliElectroVideo))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoElectroVideo))
corTiempoElectroVideo = str(np.corrcoef(datosTiempoElectroVideo))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliElectroVideo)) 
corAmpliElectroVideo = str(np.corrcoef(datosAmpliElectroVideo))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoElectroVideo, datosAmpliElectroVideo)) 
corrElectroVideo = str(np.corrcoef(datosTiempoElectroVideo,datosAmpliElectroVideo))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoElectroVideo)) 
covTiempoElectroVideo = str(np.cov(datosTiempoElectroVideo))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliElectroVideo)) 
covAmpliElectroVideo = str(np.cov(datosAmpliElectroVideo))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoElectroVideo, datosAmpliElectroVideo))
covElectroVideo = str(np.cov(datosTiempoElectroVideo,datosAmpliElectroVideo))






dataElectro = {'Datos Estadísticos':['Media','Mediana','Desviación Típica', 'Varianza', 'Moda',
	'Correlación','Covarianza'],
	
	'Valores Tiempo Electro Neutrales': [medTimeElectroNeutro,medianaTiempoElectroNeutro,desTiempoElectroNeutro,
	varTiempoElectroNeutro, modaTiempoElectroNeutro, corTiempoElectroNeutro, covTiempoElectroNeutro],
	
	'Valores Intensidad Electro Neutrales': [medAmpliElectroNeutro,medianaAmpliElectroNeutro, desAmpliElectroNeutro,
	varAmpliElectroNeutro,modaAmpliElectroNeutro,corAmpliElectroNeutro,covAmpliElectroNeutro],



	'Valores Tiempo Electro Recuperacion': [medTimeElectroRecu,medianaTiempoElectroRecu,desTiempoElectroRecu,
	  varTiempoElectroRecu,modaTiempoElectroRecu, corTiempoElectroRecu, covTiempoElectroRecu],
	
	'Valores Intensidad Electro Recuperacion': [medAmpliElectroRecu,medianaAmpliElectroRecu, desAmpliElectroRecu,
	varAmpliElectroRecu,modaAmpliElectroRecu,corAmpliElectroRecu,covAmpliElectroRecu],



	'Valores Tiempo Electro Video': [medTimeElectroVideo,medianaTiempoElectroVideo,desTiempoElectroVideo,varTiempoElectroVideo,
	 modaTiempoElectroVideo, corTiempoElectroVideo, covTiempoElectroVideo],
	
	'Valores Intensidad Electro Video': [medAmpliElectroVideo,medianaAmpliElectroVideo, desAmpliElectroVideo,
	varAmpliElectroVideo,modaAmpliElectroVideo,corAmpliElectroVideo,covAmpliElectroVideo]

	}


dfElectro = pd.DataFrame(dataElectro,columns = ['Datos Estadísticos','Valores Tiempo Electro Neutrales', 
	'Valores Intensidad Electro Neutrales','Valores Tiempo Electro Recuperacion', 'Valores Intensidad Electro Recuperacion',
 	'Valores Tiempo Electro Video', 'Valores Intensidad Electro Video'])

writer = ExcelWriter ('Sujeto14/EstadisticasElectroSujeto14Electro.xlsx')
dfElectro.to_excel(writer, 'Estadísticos Sujeto 14 Electro',index = False)
writer.save()
