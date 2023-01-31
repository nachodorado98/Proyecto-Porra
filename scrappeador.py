from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import re
import json

#Clase para scrappear los grupos y las eliminatorias
class Scrapper():


    def __init__(self, link, temporada):

        self.link=link
        self.temporada=temporada

    def scrappeo_grupos(self):

        #Inicializamos el diccionario para los grupos
        grupos={}

        #Obtenemos el codigo html
        soup=bs4(self.link.text,"html.parser")

        #Letras de los grupos
        letras=["A","B", "C", "D", "E", "F", "G", "H"]

        #Iteramos por cada letra (cada grupo)
        for i in letras:
            #Cogemos el contenedor del grupo
            contenedor=soup.find("div", id=f"all_results{self.temporada}82"+i)
            #Cogemos el grupo
            grupo=contenedor.find("h3").text
            #Cogemos la tabla de ese grupo
            tabla_grupo=contenedor.find("table", id=f"results{self.temporada}82{i}_overall").find("tbody").find_all("tr")
            #Obtenemos los equipos del grupo en el orden de posicion en el que se encuentran
            equipos=[i.find("a").text for i in tabla_grupo]
            #Agregamos el grupo y los equipos (en orden de posicion) al diccionario de los grupos
            grupos[grupo]=equipos
        
        #Devolvemos el diccionario de los grupos
        return grupos
        

    



