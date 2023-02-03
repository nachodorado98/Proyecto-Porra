from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import re
import json

#Clase para scrappear los grupos y las eliminatorias
class Scrapper():

    #Inicializamos con el link y la temporada
    def __init__(self, link, temporada):

        self.link=link
        self.temporada=temporada

    #Funcion para obtener la tabla de los grupos
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
            grupo=contenedor.find("h3").text.split(" ")[1]
            #Cogemos la tabla de ese grupo
            tabla_grupo=contenedor.find("table", id=f"results{self.temporada}82{i}_overall").find("tbody").find_all("tr")
            #Obtenemos los equipos del grupo en el orden de posicion en el que se encuentran
            equipos=[i.find("a").text for i in tabla_grupo]
            #Agregamos el grupo y los equipos (en orden de posicion) al diccionario de los grupos
            grupos[grupo]=equipos
        
        #Devolvemos el diccionario de los grupos
        return grupos


    def scrappeo_eliminatorias(self):

        #Inicializamos el diccionario para las eliminatorias
        eliminatorias={}

        #Obtenemos el codigo html
        soup=bs4(self.link.text,"html.parser")

        #Cogemos la tabla de las eliminatorias
        tabla_eliminatorias=soup.find("table", id=f"results{self.temporada}80_overall").find("tbody").find_all("tr")
        #Obtenemos los equipos (que seran los mismos que en octavos)
        equipos=[i.find("td").find("a").text for i in tabla_eliminatorias if i.find("td").find("a")!=None][:-16]
        #Obtenemos la ronda
        ronda=[i.find("th").text for i in tabla_eliminatorias if i.find("th").text!=""][:-16]
        #Juntamos la ronda con el equipo
        equipos_partidos_jugados=list(zip(ronda,equipos))

        cuartos=[]
        semis=[]
        final=[]
        campeon=""
        #Iteramos por los equipos dentro de los octavos minimo
        for i in equipos_partidos_jugados:
            #Si cumple es que ha estado minimo en cuartos
            if i[0]=="QF" or i[0]=="SF" or i[0]=="2" or i[0]=="1":
                cuartos.append(i[1])
            #Si cumple es que ha estado minimo en semis
            if i[0]=="SF" or i[0]=="2" or i[0]=="1":
                semis.append(i[1])
            #Si cumple es que ha estado minimo en la final
            if i[0]=="2" or i[0]=="1":
                final.append(i[1])
            #Si cumple es el campeon
            if i[0]=="1":
                campeon=i[1]

        #Añadimos los equipos al diccionario segun la ronda
        eliminatorias["Octavos"]=equipos
        eliminatorias["Cuartos"]=cuartos
        eliminatorias["Semis"]=semis
        eliminatorias["Final"]=final
        eliminatorias["Campeon"]=campeon

        #Devolvemos el diccionario
        return eliminatorias

    



