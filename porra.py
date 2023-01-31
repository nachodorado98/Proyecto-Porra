#Importamos lo necesario de tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#Importamos os
import os
#Importamos requests
import requests
#Impotamos la clase Scrapper para realizar el web scrapping
from scrappeador import Scrapper

#Creamos la ventana inicial
root=Tk()
root.geometry("500x700")
root.title("Fase de Grupos de la Champions League")
root.resizable(0,0)

#Creamos un diccionario que alamcena los grupos introducidos por el usuario
grupos_jugador={}

def cuadro_completo():
	pass


#Funcion para confirmar las posiciones de los equipos
def confirmacion(primero, segundo, tercero, cuarto, menu, ventana_grupo, letra):
    
    global grupos_jugador
    
    #Comprobamos que estan las 4 posiciones indicadas
    if primero and segundo and tercero and cuarto:
        
        lista=[primero, segundo, tercero, cuarto]
        
        #Comprobamos que los equipos no se han repetido
        if len(list(set(lista)))==4:
            
            #Agregamos el grupo y los equipos en la posicion al diccionario de los grupos del usuario
            grupos_jugador[letra]=lista
            
            #Comprobamos si se han rellenado los 8 grupos para poder habilitar el boton de pasar al cuadro completo
            if len(grupos_jugador)==8:
                #Activamos el boton
                btn_aceptar.config(state=NORMAL)
            
            #Destruimos la ventana
            ventana_grupo.destroy()
            #Desactivamos el submenu del grupo relleno
            menu.entryconfig("Rellenar Grupo", state="disabled")

        #Si alguno esta repetido, mostramos un mensaje de warning
        else:
            messagebox.showwarning("ATENCIÓN!!","Has introducido un equipo mas de una vez!!")
    
    #Si no estan indicadas, mostramos un mensaje de warning
    else:
        messagebox.showwarning("ATENCIÓN!!","Debes introducir todos los equipos!!")

#Funcion que nos crea una ventana por cada grupo
def grupo_n(lista, letra, menu):
    
    color="#1232d5"

    #Creamos la ventana
    ventana_grupo=Toplevel()
    ventana_grupo.geometry("500x430")
    ventana_grupo.title(f"Grupo {letra}")
    ventana_grupo.resizable(0,0)
    
    #Creamos un frame
    frame=Frame(ventana_grupo, bg=color)
    frame.pack(fill="both", expand=True)
    
    #Creamos el frame de los equipos
    frame_equipos=LabelFrame(frame, text=f"Equipos Grupo {letra}", bg=color, fg="#ffffff", font=("Times", 15, "bold"))
    frame_equipos.pack(pady=15)
    #Ponemos los equipos del grupo
    label1=Label(frame_equipos, text=lista[0], bg=color, fg="#ffffff",font=("Times", 12, "bold"))
    label1.grid(row=0, column=0, padx=10, pady=10)
    label2=Label(frame_equipos, text=lista[1], bg=color, fg="#ffffff", font=("Times", 12, "bold"))
    label2.grid(row=0, column=1, padx=10, pady=10)
    label3=Label(frame_equipos, text=lista[2], bg=color, fg="#ffffff", font=("Times", 12, "bold"))
    label3.grid(row=0, column=2, padx=10, pady=10)
    label4=Label(frame_equipos, text=lista[3], bg=color, fg="#ffffff", font=("Times", 12, "bold"))
    label4.grid(row=0, column=3, padx=10, pady=10)
    
    #Creamos el frame de las posiciones
    frame_posiciones=LabelFrame(frame, text="Tabla de posiciones", bg=color, fg="#ffffff", font=("Times", 15, "bold"))
    frame_posiciones.pack(pady=15)
    #Ponemos la combobox para elegir la posicion de los equipos
    #Primero
    labelp1=Label(frame_posiciones, text="Primero", bg=color, fg="#ffffff", font=("Times", 12, "bold"))
    labelp1.grid(row=0, column=0, padx=10, pady=10)
    combop1=ttk.Combobox(frame_posiciones, value=lista)
    combop1.grid(row=0, column=1, padx=10, pady=10)
    #Segundo
    labelp2=Label(frame_posiciones, text="Segundo", bg=color, fg="#ffffff", font=("Times", 12, "bold"))
    labelp2.grid(row=1, column=0, padx=10, pady=10)
    combop2=ttk.Combobox(frame_posiciones, value=lista)
    combop2.grid(row=1, column=1, padx=10, pady=10)
    #Tercero
    labelp3=Label(frame_posiciones, text="Tercero", bg=color, fg="#ffffff", font=("Times", 12, "bold"))
    labelp3.grid(row=2, column=0, padx=10, pady=10)
    combop3=ttk.Combobox(frame_posiciones, value=lista)
    combop3.grid(row=2, column=1, padx=10, pady=10)
    #Cuarto
    labelp4=Label(frame_posiciones, text="Cuarto", bg=color, fg="#ffffff", font=("Times", 12, "bold"))
    labelp4.grid(row=3, column=0, padx=10, pady=10)
    combop4=ttk.Combobox(frame_posiciones, value=lista)
    combop4.grid(row=3, column=1, padx=10, pady=10)
    
    #Boton para confirmar las posiciones que tienen los equipos en el grupo
    btn=Button(frame, text=f"Finalizar Grupo {letra}", command=lambda: confirmacion(combop1.get(), combop2.get(), combop3.get(), combop4.get(), menu, ventana_grupo, letra),font=("Times", 15, "bold"))
    btn.pack(pady=10, padx=10)
    
    ventana_grupo.mainloop()

#Ruta del directorio actual
path=os.getcwd()  

#url a scrappear y temporada
#url="https://fbref.com/en/comps/8/2021-2022/2021-2022-Champions-League-Stats"
url="https://fbref.com/en/comps/8/Champions-League-Stats"
temporada="2022-2023"

#Creamos un objeto scrapper con la url a scrappear y le temporada
scrappeador=Scrapper(requests.get(url), temporada)
#Scrappeamos los grupos con sus equipos en la posicion real
diccionario_grupos_equipos=scrappeador.scrappeo_grupos()

#Ordenamos los equipos dentro de cada grupo por orden alfabetico
grupoA=sorted(diccionario_grupos_equipos["Group A"])
grupoB=sorted(diccionario_grupos_equipos["Group B"])
grupoC=sorted(diccionario_grupos_equipos["Group C"])
grupoD=sorted(diccionario_grupos_equipos["Group D"])
grupoE=sorted(diccionario_grupos_equipos["Group E"])
grupoF=sorted(diccionario_grupos_equipos["Group F"])
grupoG=sorted(diccionario_grupos_equipos["Group G"])
grupoH=sorted(diccionario_grupos_equipos["Group H"])

#Creamos un menu
menu=Menu(root)
root.config(menu=menu)

#Creamos el submenu del grupo A y le pasamos los equipos (ordenados) y la letra
gA=Menu(menu, tearoff=0)
menu.add_cascade(label="Grupo A", menu=gA)
gA.add_command(label="Rellenar Grupo", command=lambda: grupo_n(grupoA, "A", gA))

#Creamos el submenu del grupo B y le pasamos los equipos (ordenados) y la letra
gB=Menu(menu, tearoff=0)
menu.add_cascade(label="Grupo B", menu=gB)
gB.add_command(label="Rellenar Grupo", command=lambda: grupo_n(grupoB, "B", gB))

#Creamos el submenu del grupo C y le pasamos los equipos (ordenados) y la letra 
gC=Menu(menu, tearoff=0)
menu.add_cascade(label="Grupo C", menu=gC)
gC.add_command(label="Rellenar Grupo", command=lambda: grupo_n(grupoC, "C", gC))

#Creamos el submenu del grupo D y le pasamos los equipos (ordenados) y la letra
gD=Menu(menu, tearoff=0)
menu.add_cascade(label="Grupo D", menu=gD)
gD.add_command(label="Rellenar Grupo", command=lambda: grupo_n(grupoD, "D", gD))

#Creamos el submenu del grupo E y le pasamos los equipos (ordenados) y la letra
gE=Menu(menu, tearoff=0)
menu.add_cascade(label="Grupo E", menu=gE)
gE.add_command(label="Rellenar Grupo", command=lambda: grupo_n(grupoE, "E", gE))

#Creamos el submenu del grupo F y le pasamos los equipos (ordenados) y la letra
gF=Menu(menu, tearoff=0)
menu.add_cascade(label="Grupo F", menu=gF)
gF.add_command(label="Rellenar Grupo", command=lambda: grupo_n(grupoF, "F", gF))

#Creamos el submenu del grupo G y le pasamos los equipos (ordenados) y la letra
gG=Menu(menu, tearoff=0)
menu.add_cascade(label="Grupo G", menu=gG)
gG.add_command(label="Rellenar Grupo", command=lambda: grupo_n(grupoG, "G", gG))

#Creamos el submenu del grupo H y le pasamos los equipos (ordenados) y la letra
gH=Menu(menu, tearoff=0)
menu.add_cascade(label="Grupo H", menu=gH)
gH.add_command(label="Rellenar Grupo", command=lambda: grupo_n(grupoH, "H", gH))

#Creamos un frame
frame=Frame(root, bg="#1232d5")
frame.pack(fill="both", expand=True)

#Ponemos la imagen de la cabecera en el frame
imagen_cabecera=PhotoImage(file=os.path.join(path,"Archivos Extra\cabecera.png"))
label_cabecera=Label(frame, image=imagen_cabecera,bg="#1232d5")
label_cabecera.pack(pady=(20,5), padx=10)

#Ponemos un label nombre y un entry para introducirlo
label_usuario=Label(frame, text="Nombre", font=("Times", 20, "bold"), bg="#1232d5", fg="#ffffff")
label_usuario.pack(pady=5, padx=10)
entry_usuario=Entry(frame)
entry_usuario.pack(pady=(5,10), padx=10)

#Boton que nos permite aceptar para continuar al siguiente paso (ver el cuadro completo)
btn_aceptar=Button(frame, text="Aceptar", command=cuadro_completo, state=DISABLED,font=("Times", 15, "bold"))
btn_aceptar.pack(pady=10)

#Ponemos el boton de la copa
imagen_copa=PhotoImage(file=os.path.join(path,"Archivos Extra\copa.png"))
label_copa=Button(frame, image=imagen_copa,command="",bg="#1232d5",bd=0)
label_copa.pack(pady=(20,5), padx=10)
    

root.mainloop()

