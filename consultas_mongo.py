#Impotamos la clase ConfigMongo
from config_mongo import ConfigMongo

#Clase para realizar las consultas en MongoDB
class ConsultaMongo():

	#Inicializamos la tabla llamando a la funcion crear_conexion
	tabla=ConfigMongo().crear_conexion()

	#Funcion que nos devuelve todos los registros de la tabla
	def todos(self):
		return self.tabla.find({})

	#Funcion para insertar docuementos en la tabla
	def insertar_datos(self, datos):
		
		try:
			self.tabla.insert_one(datos)
			return True
		except:
			return False

	#Funcion para saber si un usuario esta o no en la tabla
	def consulta_usuario_libre(self, usuario):
		if list(self.tabla.find({"Usuario":usuario}))!=[]:
			return False
		else:
			return True