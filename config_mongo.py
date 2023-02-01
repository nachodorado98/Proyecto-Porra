import pymongo
from pymongo import MongoClient

class ConfigMongo():

	def crear_conexion(self):
		#Creamos un objeto cliente de la clase MongoClient 
		cliente=MongoClient("localhost")
		#Creamos la BBDD
		bbdd=cliente["Porra"]
		#Creamos una coleccion a la que le damos un nombre
		coleccion=bbdd["ResultadosPorra"]

		return coleccion


