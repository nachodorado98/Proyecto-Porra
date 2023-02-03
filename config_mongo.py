#Importamos lo necesario para trabajar con MongoDB
import pymongo
from pymongo import MongoClient

#Clase para configurar la conexion con MongoDB
class ConfigMongo():

	#Funcion para crear la conexion
	def crear_conexion(self):
		#Creamos un objeto cliente de la clase MongoClient 
		cliente=MongoClient("localhost")
		#Creamos la BBDD
		bbdd=cliente["Porra"]
		#Creamos una coleccion a la que le damos un nombre
		coleccion=bbdd["ResultadosPorra"]
		#Devolvemos la tabla
		return coleccion


