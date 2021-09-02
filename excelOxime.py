import pandas as pd 
import numpy as np
from scipy import stats
from pandas import ExcelWriter


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

print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoOximeNeutro))
medTimeOximeNeutro = str(np.mean(datosTiempoOximeNeutro))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliOximeNeutro)) 
medAmpliOximeNeutro = str(np.mean(datosAmpliOximeNeutro))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoOximeNeutro)) 
medianaTiempoOximeNeutro = str(np.median(datosTiempoOximeNeutro))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliOximeNeutro)) 
medianaAmpliOximeNeutro = str(np.median(datosAmpliOximeNeutro))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoOximeNeutro)) 
desTiempoOximeNeutro = str(np.std(datosTiempoOximeNeutro))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliOximeNeutro)) 
desAmpliOximeNeutro = str(np.std(datosAmpliOximeNeutro))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoOximeNeutro)) 
varTiempoOximeNeutro = str(np.var(datosTiempoOximeNeutro))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliOximeNeutro)) 
varAmpliOximeNeutro = str(np.var(datosAmpliOximeNeutro))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoOximeNeutro))
modaTiempoOximeNeutro = str(stats.mode(datosTiempoOximeNeutro))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliOximeNeutro))
modaAmpliOximeNeutro = str(stats.mode(datosAmpliOximeNeutro))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoOximeNeutro))
corTiempoOximeNeutro = str(np.corrcoef(datosTiempoOximeNeutro))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliOximeNeutro)) 
corAmpliOximeNeutro = str(np.corrcoef(datosAmpliOximeNeutro))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoOximeNeutro, datosAmpliOximeNeutro)) 
corrOximeNeutro = str(np.corrcoef(datosTiempoOximeNeutro,datosAmpliOximeNeutro))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoOximeNeutro)) 
covTiempoOximeNeutro = str(np.cov(datosTiempoOximeNeutro))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliOximeNeutro)) 
covAmpliOximeNeutro = str(np.cov(datosAmpliOximeNeutro))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoOximeNeutro, datosAmpliOximeNeutro))
covAmpliOximeNeutro = str(np.cov(datosTiempoOximeNeutro,datosAmpliOximeNeutro))





print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoOximeRecu))
medTimeOximeRecu = str(np.mean(datosTiempoOximeRecu))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliOximeRecu)) 
medAmpliOximeRecu = str(np.mean(datosAmpliOximeRecu))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoOximeRecu)) 
medianaTiempoOximeRecu = str(np.median(datosTiempoOximeRecu))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliOximeRecu)) 
medianaAmpliOximeRecu = str(np.median(datosAmpliOximeRecu))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoOximeRecu)) 
desTiempoOximeRecu = str(np.std(datosTiempoOximeRecu))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliOximeRecu)) 
desAmpliOximeRecu = str(np.std(datosAmpliOximeRecu))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoOximeRecu)) 
varTiempoOximeRecu = str(np.var(datosTiempoOximeRecu))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliOximeRecu)) 
varAmpliOximeRecu = str(np.var(datosAmpliOximeRecu))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoOximeRecu))
modaTiempoOximeRecu = str(stats.mode(datosTiempoOximeRecu))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliOximeRecu))
modaAmpliOximeRecu = str(stats.mode(datosAmpliOximeRecu))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoOximeRecu))
corTiempoOximeRecu = str(np.corrcoef(datosTiempoOximeRecu))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliOximeRecu)) 
corAmpliOximeRecu = str(np.corrcoef(datosAmpliOximeRecu))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoOximeRecu, datosAmpliOximeRecu)) 
corrOximeRecu = str(np.corrcoef(datosTiempoOximeRecu,datosAmpliOximeRecu))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoOximeRecu)) 
covTiempoOximeRecu = str(np.cov(datosTiempoOximeRecu))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliOximeRecu)) 
covAmpliOximeRecu = str(np.cov(datosAmpliOximeRecu))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoOximeRecu, datosAmpliOximeRecu))
covOximeRecu = str(np.cov(datosTiempoOximeRecu,datosAmpliOximeRecu))





print("\n\nMedia Aritmética del Tiempo")
print(np.mean(datosTiempoOximeVideo))
medTimeOximeVideo = str(np.mean(datosTiempoOximeVideo))


print("\n\nMedia Aritmética de la Intensidad:    ")
print(np.mean(datosAmpliOximeVideo)) 
medAmpliOximeVideo = str(np.mean(datosAmpliOximeVideo))


print("\n\nMediana del Tiempo: ")
print(np.median(datosTiempoOximeVideo)) 
medianaTiempoOximeVideo = str(np.median(datosTiempoOximeVideo))


print("\n\nMediana de la Intensidad: ")
print(np.median(datosAmpliOximeVideo)) 
medianaAmpliOximeVideo = str(np.median(datosAmpliOximeVideo))


print("\n\nDesviación típica del Tiempo: ")
print(np.std(datosTiempoOximeVideo)) 
desTiempoOximeVideo = str(np.std(datosTiempoOximeVideo))


print("\n\nDesviación típica de la Intensidad: ")
print(np.std(datosAmpliOximeVideo)) 
desAmpliOximeVideo = str(np.std(datosAmpliOximeVideo))


print("\n\nVarianza del Tiempo:")
print(np.var(datosTiempoOximeVideo)) 
varTiempoOximeVideo = str(np.var(datosTiempoOximeVideo))


print("\n\nVarianza de la Intensidad:")
print(np.var(datosAmpliOximeVideo)) 
varAmpliOximeVideo = str(np.var(datosAmpliOximeVideo))


print("\n\nModa del Tiempo:")
print(stats.mode(datosTiempoOximeVideo))
modaTiempoOximeVideo = str(stats.mode(datosTiempoOximeVideo))


print("\n\nModa de la Intensidad:")
print(stats.mode(datosAmpliOximeVideo))
modaAmpliOximeVideo = str(stats.mode(datosAmpliOximeVideo))


print("\n\nCorrelación del Tiempo")
print(np.corrcoef(datosTiempoOximeVideo))
corTiempoOximeVideo = str(np.corrcoef(datosTiempoOximeVideo))


print("\n\nCorrelación de la Intensidad")
print(np.corrcoef(datosAmpliOximeVideo)) 
corAmpliOximeVideo = str(np.corrcoef(datosAmpliOximeVideo))


print("\n\nCorrelación de los Datos:")
print(np.corrcoef(datosTiempoOximeVideo, datosAmpliOximeVideo)) 
corrOximeVideo = str(np.corrcoef(datosTiempoOximeVideo,datosAmpliOximeVideo))


print("\n\nCovarianza del Tiempo:")
print(np.cov(datosTiempoOximeVideo)) 
covTiempoOximeVideo = str(np.cov(datosTiempoOximeVideo))


print("\n\nCovarianza de la Intensidad:")
print(np.cov(datosAmpliOximeVideo)) 
covAmpliOximeVideo = str(np.cov(datosAmpliOximeVideo))


print("\n\nCovarianza de los dos vectores")
print(np.cov(datosTiempoOximeVideo, datosAmpliOximeVideo))
covOximeVideo = str(np.cov(datosTiempoOximeVideo,datosAmpliOximeVideo))






dataOxime = {'Datos Estadísticos':['Media','Mediana','Desviación Típica', 'Varianza', 'Moda',
	'Correlación','Covarianza'],
	
	'Valores Tiempo Oxime Neutrales': [medTimeOximeNeutro,medianaTiempoOximeNeutro,desTiempoOximeNeutro,
	varTiempoOximeNeutro, modaTiempoOximeNeutro, corTiempoOximeNeutro, covTiempoOximeNeutro],
	
	'Valores Intensidad Oxime Neutrales': [medAmpliOximeNeutro,medianaAmpliOximeNeutro, desAmpliOximeNeutro,
	varAmpliOximeNeutro,modaAmpliOximeNeutro,corAmpliOximeNeutro,covAmpliOximeNeutro],



	'Valores Tiempo Oxime Recuperacion': [medTimeOximeRecu,medianaTiempoOximeRecu,desTiempoOximeRecu,
	  varTiempoOximeRecu,modaTiempoOximeRecu, corTiempoOximeRecu, covTiempoOximeRecu],
	
	'Valores Intensidad Oxime Recuperacion': [medAmpliOximeRecu,medianaAmpliOximeRecu, desAmpliOximeRecu,
	varAmpliOximeRecu,modaAmpliOximeRecu,corAmpliOximeRecu,covAmpliOximeRecu],



	'Valores Tiempo Oxime Video': [medTimeOximeVideo,medianaTiempoOximeVideo,desTiempoOximeVideo,varTiempoOximeVideo,
	 modaTiempoOximeVideo, corTiempoOximeVideo, covTiempoOximeVideo],
	
	'Valores Intensidad Oxime Video': [medAmpliOximeVideo,medianaAmpliOximeVideo, desAmpliOximeVideo,
	varAmpliOximeVideo,modaAmpliOximeVideo,corAmpliOximeVideo,covAmpliOximeVideo]

	}


dfOxime = pd.DataFrame(dataOxime,columns = ['Datos Estadísticos','Valores Tiempo Oxime Neutrales', 
	'Valores Intensidad Oxime Neutrales','Valores Tiempo Oxime Recuperacion', 'Valores Intensidad Oxime Recuperacion',
 	'Valores Tiempo Oxime Video', 'Valores Intensidad Oxime Video'])

writer = ExcelWriter ('Sujeto16/EstadisticasOximeSujeto16.xlsx')
dfOxime.to_excel(writer, 'Estadísticos Sujeto 16 Oxime',index = False)
writer.save()
