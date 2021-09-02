import pandas as pd 
import numpy as np
from scipy import stats
from pandas import ExcelWriter


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

print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoMioNeutro))
medTimeMioNeutro = str(np.mean(datosTiempoMioNeutro))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliMioNeutro)) 
medAmpliMioNeutro = str(np.mean(datosAmpliMioNeutro))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoMioNeutro)) 
medianaTiempoMioNeutro = str(np.median(datosTiempoMioNeutro))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliMioNeutro)) 
medianaAmpliMioNeutro = str(np.median(datosAmpliMioNeutro))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoMioNeutro)) 
desTiempoMioNeutro = str(np.std(datosTiempoMioNeutro))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliMioNeutro)) 
desAmpliMioNeutro = str(np.std(datosAmpliMioNeutro))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoMioNeutro)) 
varTiempoMioNeutro = str(np.var(datosTiempoMioNeutro))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliMioNeutro)) 
varAmpliMioNeutro = str(np.var(datosAmpliMioNeutro))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoMioNeutro))
modaTiempoMioNeutro = str(stats.mode(datosTiempoMioNeutro))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliMioNeutro))
modaAmpliMioNeutro = str(stats.mode(datosAmpliMioNeutro))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoMioNeutro))
corTiempoMioNeutro = str(np.corrcoef(datosTiempoMioNeutro))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliMioNeutro)) 
corAmpliMioNeutro = str(np.corrcoef(datosAmpliMioNeutro))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoMioNeutro, datosAmpliMioNeutro)) 
corrMioNeutro = str(np.corrcoef(datosTiempoMioNeutro,datosAmpliMioNeutro))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoMioNeutro)) 
covTiempoMioNeutro = str(np.cov(datosTiempoMioNeutro))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliMioNeutro)) 
covAmpliMioNeutro = str(np.cov(datosAmpliMioNeutro))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoMioNeutro, datosAmpliMioNeutro))
covAmpliMioNeutro = str(np.cov(datosTiempoMioNeutro,datosAmpliMioNeutro))





print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoMioRecu))
medTimeMioRecu = str(np.mean(datosTiempoMioRecu))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliMioRecu)) 
medAmpliMioRecu = str(np.mean(datosAmpliMioRecu))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoMioRecu)) 
medianaTiempoMioRecu = str(np.median(datosTiempoMioRecu))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliMioRecu)) 
medianaAmpliMioRecu = str(np.median(datosAmpliMioRecu))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoMioRecu)) 
desTiempoMioRecu = str(np.std(datosTiempoMioRecu))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliMioRecu)) 
desAmpliMioRecu = str(np.std(datosAmpliMioRecu))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoMioRecu)) 
varTiempoMioRecu = str(np.var(datosTiempoMioRecu))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliMioRecu)) 
varAmpliMioRecu = str(np.var(datosAmpliMioRecu))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoMioRecu))
modaTiempoMioRecu = str(stats.mode(datosTiempoMioRecu))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliMioRecu))
modaAmpliMioRecu = str(stats.mode(datosAmpliMioRecu))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoMioRecu))
corTiempoMioRecu = str(np.corrcoef(datosTiempoMioRecu))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliMioRecu)) 
corAmpliMioRecu = str(np.corrcoef(datosAmpliMioRecu))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoMioRecu, datosAmpliMioRecu)) 
corrMioRecu = str(np.corrcoef(datosTiempoMioRecu,datosAmpliMioRecu))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoMioRecu)) 
covTiempoMioRecu = str(np.cov(datosTiempoMioRecu))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliMioRecu)) 
covAmpliMioRecu = str(np.cov(datosAmpliMioRecu))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoMioRecu, datosAmpliMioRecu))
covMioRecu = str(np.cov(datosTiempoMioRecu,datosAmpliMioRecu))





print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoMioVideo))
medTimeMioVideo = str(np.mean(datosTiempoMioVideo))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliMioVideo)) 
medAmpliMioVideo = str(np.mean(datosAmpliMioVideo))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoMioVideo)) 
medianaTiempoMioVideo = str(np.median(datosTiempoMioVideo))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliMioVideo)) 
medianaAmpliMioVideo = str(np.median(datosAmpliMioVideo))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoMioVideo)) 
desTiempoMioVideo = str(np.std(datosTiempoMioVideo))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliMioVideo)) 
desAmpliMioVideo = str(np.std(datosAmpliMioVideo))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoMioVideo)) 
varTiempoMioVideo = str(np.var(datosTiempoMioVideo))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliMioVideo)) 
varAmpliMioVideo = str(np.var(datosAmpliMioVideo))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoMioVideo))
modaTiempoMioVideo = str(stats.mode(datosTiempoMioVideo))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliMioVideo))
modaAmpliMioVideo = str(stats.mode(datosAmpliMioVideo))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoMioVideo))
corTiempoMioVideo = str(np.corrcoef(datosTiempoMioVideo))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliMioVideo)) 
corAmpliMioVideo = str(np.corrcoef(datosAmpliMioVideo))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoMioVideo, datosAmpliMioVideo)) 
corrMioVideo = str(np.corrcoef(datosTiempoMioVideo,datosAmpliMioVideo))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoMioVideo)) 
covTiempoMioVideo = str(np.cov(datosTiempoMioVideo))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliMioVideo)) 
covAmpliMioVideo = str(np.cov(datosAmpliMioVideo))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoMioVideo, datosAmpliMioVideo))
covMioVideo = str(np.cov(datosTiempoMioVideo,datosAmpliMioVideo))






dataMio = {'Datos Estadísticos':['Media','Mediana','Desviación Típica', 'Varianza', 'Moda',
	'Correlación','Covarianza'],
	
	'Valores Tiempo Mio Neutrales': [medTimeMioNeutro,medianaTiempoMioNeutro,desTiempoMioNeutro,
	varTiempoMioNeutro, modaTiempoMioNeutro, corTiempoMioNeutro, covTiempoMioNeutro],
	
	'Valores Intensidad Mio Neutrales': [medAmpliMioNeutro,medianaAmpliMioNeutro, desAmpliMioNeutro,
	varAmpliMioNeutro,modaAmpliMioNeutro,corAmpliMioNeutro,covAmpliMioNeutro],



	'Valores Tiempo Mio Recuperacion': [medTimeMioRecu,medianaTiempoMioRecu,desTiempoMioRecu,
	  varTiempoMioRecu,modaTiempoMioRecu, corTiempoMioRecu, covTiempoMioRecu],
	
	'Valores Intensidad Mio Recuperacion': [medAmpliMioRecu,medianaAmpliMioRecu, desAmpliMioRecu,
	varAmpliMioRecu,modaAmpliMioRecu,corAmpliMioRecu,covAmpliMioRecu],



	'Valores Tiempo Mio Video': [medTimeMioVideo,medianaTiempoMioVideo,desTiempoMioVideo,varTiempoMioVideo,
	 modaTiempoMioVideo, corTiempoMioVideo, covTiempoMioVideo],
	
	'Valores Intensidad Mio Video': [medAmpliMioVideo,medianaAmpliMioVideo, desAmpliMioVideo,
	varAmpliMioVideo,modaAmpliMioVideo,corAmpliMioVideo,covAmpliMioVideo]

	}


dfMio = pd.DataFrame(dataMio,columns = ['Datos Estadísticos','Valores Tiempo Mio Neutrales', 
	'Valores Intensidad Mio Neutrales','Valores Tiempo Mio Recuperacion', 'Valores Intensidad Mio Recuperacion',
 	'Valores Tiempo Mio Video', 'Valores Intensidad Mio Video'])

writer = ExcelWriter ('Sujeto16/EstadisticasMioSujeto16.xlsx')
dfMio.to_excel(writer, 'Estadísticos Sujeto 16 Mio',index = False)
writer.save()
