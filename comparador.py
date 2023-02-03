#Importamos pandas
import pandas as pd


#Clase Comparador para comparar los resultados de dos jugadores (siempre se compararan con los resultados reales, jugador especial)
class Comparador():

	#Funcion para combinar los grupos de ambos jugadores a comparar
	def junta_grupos(self, grupos_usuario:list, grupos_real:list):

		return list(zip(grupos_usuario,grupos_real))

	#Funcion que nos devuelve los puntos tras comparar los grupos de los jugadores (siempre con el jugador especial) 
	def puntos_grupos(self, grupos:list):

		#Puntos segun la distancia de los puestos acertados (DiferenciaPuestos:Puntos)
		bonificacion={0:3,1:2,2:1,3:0}
		#Lista para agregar los puntos obtenidos de cada uno de los grupos
		lista_puntos_bonificados_grupos=[]

		#Iteramos a traves de los grupos 
		for i in grupos:

			#Creamos un diccionario con los equipos del grupo y el puesto que tienen para ambos jugadores
			puestos_usuario={"Equipos":i[0],"Puesto":[1,2,3,4]}
			puestos_real={"Equipos":i[1],"Puesto":[-1,-2,-3,-4]}

			#Creamos un dataframe con cada dicccionario y los concatenamos para poder agruparlos por equipo y sumar los puestos
			df=pd.concat([pd.DataFrame(puestos_usuario), pd.DataFrame(puestos_real)]).groupby(["Equipos"]).sum()

			#Agregamos la suma de los puestos en valor absoluto a una lista
			lista_puestos=[abs(i) for i in df["Puesto"]]

			#Asignamos los puntos de bonificacion segun la diferencia de puestos obtenida
			lista_puntos_bonificados=[bonificacion[i] for i in lista_puestos]

			#Agregamos la suma de los puntos del grupo a la lista total de puntos
			lista_puntos_bonificados_grupos.append(sum(lista_puntos_bonificados))

		#Devolvemos la suma total de los puntos de los grupos y tambien los puntos de cada grupo
		return sum(lista_puntos_bonificados_grupos), lista_puntos_bonificados_grupos

#Clase Jugador para agregar los datos de cada uno de ellos
class Jugador():

	#Lo inicializamos con un nombre
	def __init__(self, nombre):
		self.nombre=nombre

	#Funcion para obtener los grupos en una lista viniendo de un diccionario
	def grupos_jugador(self, resultados:dict):

		letras=["A","B","C","D","E","F","G","H"]

		return [resultados[i] for i in letras]

    
