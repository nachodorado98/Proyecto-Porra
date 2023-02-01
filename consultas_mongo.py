from config_mongo import ConfigMongo

class ConsultaMongo():
	tabla=ConfigMongo().crear_conexion()

	def todos(self):
		return self.tabla.find({})

	def insertar_datos(self, datos):
		
		try:
			self.tabla.insert_one(datos)
			return True
		except:
			return False

	def consulta_usuario_libre(self, usuario):
		if list(self.tabla.find({"Usuario":usuario}))!=[]:
			return False
		else:
			return True