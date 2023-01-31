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


def bbdd(lista_octavos,lista_cuartos,lista_semis,lista_final,campeon,lista_consolacion,tercero, usuario, ventanita):
    pass

def rellenar(boton_click, boton_poner, e=None):
    
    equipo=boton_click.cget("text")
    
    boton_poner.config(text=equipo)

def rellenar_especial(boton_click, boton_no_click, boton_poner_final, boton_poner_no_final, e=None):
    
    final=boton_click.cget("text")
    no_final=boton_no_click.cget("text")
    
    boton_poner_final.config(text=final)
    boton_poner_no_final.config(text=no_final)

def cuadro_completo():

    global grupos_jugador
    
    path_actual=os.getcwd() 
    
    if entry_usuario.get().isalnum() and len(entry_usuario.get())>2:
    
        usuario=entry_usuario.get().upper()

        entry_usuario.delete(0,END)
        btn_aceptar.config(state=DISABLED)

        ventanita=Toplevel()
        ventanita.geometry("1350x900")
        ventanita.title("Global")
        ventanita.resizable(0,0)

        frame=Frame(ventanita, bg="#1232d5")
        frame.pack(fill="both", expand=True)

        frame_izq=Frame(frame,bg="#1232d5")
        frame_izq.grid(row=0, column=0,padx=30)

        estilo=ttk.Style()
        estilo.configure("Treeview", background="silver", foreground="black")
        estilo.map("Treeview", background=[("selected","white")])
        estilo.theme_use("alt")

        frame_boton=Frame(frame_izq,bg="#1232d5")
        frame_boton.pack(pady=5)
    
        imagen_bbdd=PhotoImage(file=os.path.join(path,"Archivos Extra\\bbdd.png"))

        boton_bbdd=Button(frame_izq,command=lambda: bbdd(lista_octavos,lista_cuartos,lista_semis,lista_final,campeon,lista_consolacion,tercero, usuario, ventanita), image=imagen_bbdd,bg="#1232d5", bd=0)
        boton_bbdd.pack(pady=5)

        frame_grupos=Frame(frame_izq,bg="#1232d5")
        frame_grupos.pack(pady=(10,5))

        label_grupos=Label(frame_grupos, text="Fase de Grupos",bg="#1232d5", fg="#ffffff",font=("Times", 15, "bold"))
        label_grupos.grid(row=0, column=0, columnspan=2,padx=10, pady=10)

        #---------------------------------------------------------GRUPO A
        grupoA=grupos_jugador["A"]

        treeA=ttk.Treeview(frame_grupos)
        treeA.grid(row=1, column=0, padx=10, pady=10)

        treeA["columns"]=("Grupo A",)
        treeA.column("Grupo A", width=80, minwidth=80)
        treeA.column("#0", width=0, stretch=NO)
        treeA.heading("Grupo A", text="Grupo A")
        for i in range(len(grupoA)):
            treeA.insert(parent="", index="end", iid=i, text="", values=(grupoA[i],))

        treeA.config(height=4)

        #---------------------------------------------------------GRUPO B

        grupoB=grupos_jugador["B"]

        treeB=ttk.Treeview(frame_grupos)
        treeB.grid(row=1, column=1, padx=10, pady=10)

        treeB["columns"]=("Grupo B",)
        treeB.column("Grupo B", width=80, minwidth=80)
        treeB.column("#0", width=0, stretch=NO)
        treeB.heading("Grupo B", text="Grupo B")
        for i in range(len(grupoB)):
            treeB.insert(parent="", index="end", iid=i, text="", values=(grupoB[i],))

        treeB.config(height=4)

        #---------------------------------------------------------GRUPO C

        grupoC=grupos_jugador["C"]

        treeC=ttk.Treeview(frame_grupos)
        treeC.grid(row=2, column=0, padx=10, pady=10)

        treeC["columns"]=("Grupo C",)
        treeC.column("Grupo C", width=80, minwidth=80)
        treeC.column("#0", width=0, stretch=NO)
        treeC.heading("Grupo C", text="Grupo C")
        for i in range(len(grupoC)):
            treeC.insert(parent="", index="end", iid=i, text="", values=(grupoC[i],))

        treeC.config(height=4)

        #---------------------------------------------------------GRUPO D

        grupoD=grupos_jugador["D"]

        treeD=ttk.Treeview(frame_grupos)
        treeD.grid(row=2, column=1, padx=10, pady=10)

        treeD["columns"]=("Grupo D",)
        treeD.column("Grupo D", width=80, minwidth=80)
        treeD.column("#0", width=0, stretch=NO)
        treeD.heading("Grupo D", text="Grupo D")
        for i in range(len(grupoD)):
            treeD.insert(parent="", index="end", iid=i, text="", values=(grupoD[i],))

        treeD.config(height=4)

        #---------------------------------------------------------GRUPO E

        grupoE=grupos_jugador["E"]

        treeE=ttk.Treeview(frame_grupos)
        treeE.grid(row=3, column=0, padx=10, pady=10)

        treeE["columns"]=("Grupo E",)
        treeE.column("Grupo E", width=80, minwidth=80)
        treeE.column("#0", width=0, stretch=NO)
        treeE.heading("Grupo E", text="Grupo E")
        for i in range(len(grupoE)):
            treeE.insert(parent="", index="end", iid=i, text="", values=(grupoE[i],))

        treeE.config(height=4)

        #---------------------------------------------------------GRUPO F

        grupoF=grupos_jugador["F"]

        treeF=ttk.Treeview(frame_grupos)
        treeF.grid(row=3, column=1, padx=10, pady=10)

        treeF["columns"]=("Grupo F",)
        treeF.column("Grupo F", width=80, minwidth=80)
        treeF.column("#0", width=0, stretch=NO)
        treeF.heading("Grupo F", text="Grupo F")
        for i in range(len(grupoF)):
            treeF.insert(parent="", index="end", iid=i, text="", values=(grupoF[i],))

        treeF.config(height=4)

        #---------------------------------------------------------GRUPO G

        grupoG=grupos_jugador["G"]

        treeG=ttk.Treeview(frame_grupos)
        treeG.grid(row=4, column=0, padx=10, pady=10)

        treeG["columns"]=("Grupo G",)
        treeG.column("Grupo G", width=80, minwidth=80)
        treeG.column("#0", width=0, stretch=NO)
        treeG.heading("Grupo G", text="Grupo G")
        for i in range(len(grupoG)):
            treeG.insert(parent="", index="end", iid=i, text="", values=(grupoG[i],))

        treeG.config(height=4)

        #---------------------------------------------------------GRUPO H

        grupoH=grupos_jugador["H"]

        treeH=ttk.Treeview(frame_grupos)
        treeH.grid(row=4, column=1, padx=10, pady=10)

        treeH["columns"]=("Grupo H",)
        treeH.column("Grupo H", width=80, minwidth=80)
        treeH.column("#0", width=0, stretch=NO)
        treeH.heading("Grupo H", text="Grupo H")
        for i in range(len(grupoH)):
            treeH.insert(parent="", index="end", iid=i, text="", values=(grupoH[i],))

        treeH.config(height=4)


        #--------------------------------------------------------ELIMINATORIAS

        frame_der=Frame(frame,bg="#1232d5")
        frame_der.grid(row=0, column=1,padx=20)

        frame_encabe=Frame(frame_der, bg="#1232d5")
        frame_encabe.pack()
        
        imagen_cabecera_2=PhotoImage(file=os.path.join(path_actual,"Archivos Extra\cabecera.png"))

        label_cabecera_foto=Label(frame_encabe, image=imagen_cabecera_2, bg="#1232d5")
        label_cabecera_foto.pack(pady=5)

        frame_eliminatorias=Frame(frame_der, bg="#1232d5")
        frame_eliminatorias.pack()

        #---------------------------------------------------------OCTAVOS 1
        label_octavos1=Label(frame_eliminatorias, text="Octavos", bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_octavos1.grid(row=0, column=0, pady=5, padx=10)

        frame_octavos1=Frame(frame_eliminatorias, bg="#1232d5")
        frame_octavos1.grid(row=1, column=0, pady=10, padx=10)

        #-----------------------------------Primero GA
        primero_gA=treeA.item(0, "values")
        oct11=Label(frame_octavos1, text=primero_gA[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct11.pack(pady=(30,3))
        oct11.bind("<Button-1>", lambda e: rellenar(oct11, cuar11, e))

        #-----------------------------------Segundo GB
        segundo_gB=treeB.item(1, "values")
        oct12=Label(frame_octavos1, text=segundo_gB[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct12.pack(pady=(3,30))
        oct12.bind("<Button-1>", lambda e: rellenar(oct12, cuar11, e))

        #-----------------------------------Primero GC
        primero_gC=treeC.item(0, "values")
        oct21=Label(frame_octavos1, text=primero_gC[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct21.pack(pady=(30,3))
        oct21.bind("<Button-1>", lambda e: rellenar(oct21, cuar12, e))

        #-----------------------------------Segundo GD
        segundo_gD=treeD.item(1, "values")
        oct22=Label(frame_octavos1, text=segundo_gD[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct22.pack(pady=(3,30))
        oct22.bind("<Button-1>", lambda e: rellenar(oct22, cuar12, e))

        #-----------------------------------Primero GE
        primero_gE=treeE.item(0, "values")
        oct31=Label(frame_octavos1, text=primero_gE[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct31.pack(pady=(30,3))
        oct31.bind("<Button-1>", lambda e: rellenar(oct31, cuar21, e))

        #-----------------------------------Segundo GF
        segundo_gF=treeF.item(1, "values")
        oct32=Label(frame_octavos1, text=segundo_gF[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct32.pack(pady=(3,30))
        oct32.bind("<Button-1>", lambda e: rellenar(oct32, cuar21, e))

        #-----------------------------------Primero GG
        primero_gG=treeG.item(0, "values")
        oct41=Label(frame_octavos1, text=primero_gG[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct41.pack(pady=(30,3))
        oct41.bind("<Button-1>", lambda e: rellenar(oct41, cuar22, e))

        #-----------------------------------Segundo GH
        segundo_gH=treeH.item(1, "values")
        oct42=Label(frame_octavos1, text=segundo_gH[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct42.pack(pady=(3,30))
        oct42.bind("<Button-1>", lambda e: rellenar(oct42, cuar22, e))


        #---------------------------------------------------------OCTAVOS 2
        label_octavos2=Label(frame_eliminatorias, text="Octavos", bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_octavos2.grid(row=0, column=6, pady=5, padx=10)

        frame_octavos2=Frame(frame_eliminatorias, bg="#1232d5")
        frame_octavos2.grid(row=1, column=6, pady=10, padx=10)

        #-----------------------------------Primero GB
        primero_gB=treeB.item(0, "values")
        oct51=Label(frame_octavos2, text=primero_gB[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct51.pack(pady=(30,3))
        oct51.bind("<Button-1>", lambda e: rellenar(oct51, cuar31, e))

        #-----------------------------------Segundo GA
        segundo_gA=treeA.item(1, "values")
        oct52=Label(frame_octavos2, text=segundo_gA[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct52.pack(pady=(3,30))
        oct52.bind("<Button-1>", lambda e: rellenar(oct52, cuar31, e))

        #-----------------------------------Primero GD
        primero_gD=treeD.item(0, "values")
        oct61=Label(frame_octavos2, text=primero_gD[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct61.pack(pady=(30,3))
        oct61.bind("<Button-1>", lambda e: rellenar(oct61, cuar32, e))

        #-----------------------------------Segundo GC
        segundo_gC=treeC.item(1, "values")
        oct62=Label(frame_octavos2, text=segundo_gC[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct62.pack(pady=(3,30))
        oct62.bind("<Button-1>", lambda e: rellenar(oct62, cuar32, e))

        #-----------------------------------Primero GF
        primero_gF=treeF.item(0, "values")
        oct71=Label(frame_octavos2, text=primero_gF[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct71.pack(pady=(30,3))
        oct71.bind("<Button-1>", lambda e: rellenar(oct71, cuar41, e))

        #-----------------------------------Segundo GE
        segundo_gE=treeE.item(1, "values")
        oct72=Label(frame_octavos2, text=segundo_gE[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct72.pack(pady=(3,30))
        oct72.bind("<Button-1>", lambda e: rellenar(oct72, cuar41, e))

        #-----------------------------------Primero GH
        primero_gH=treeH.item(0, "values")
        oct81=Label(frame_octavos2, text=primero_gH[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct81.pack(pady=(30,3))
        oct81.bind("<Button-1>", lambda e: rellenar(oct81, cuar42, e))

        #-----------------------------------Segundo GG
        segundo_gG=treeG.item(1, "values")
        oct82=Label(frame_octavos2, text=segundo_gG[0],bg="white", font=("Times", 12, "bold"), width=12)
        oct82.pack(pady=(3,30))
        oct82.bind("<Button-1>", lambda e: rellenar(oct82, cuar42, e))

        #----------------------------------------Lista Octavos
        lista_octavos=[oct11,oct12,oct21,oct22,oct31,oct32,oct41,oct42,oct51,oct52,oct61,oct62,oct71,oct72,oct81,oct82]




        #---------------------------------------------------------CUARTOS 1
        label_cuartos1=Label(frame_eliminatorias, text="Cuartos", bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_cuartos1.grid(row=0, column=1, pady=5, padx=10)

        frame_cuartos1=Frame(frame_eliminatorias, bg="#1232d5")
        frame_cuartos1.grid(row=1, column=1, pady=10, padx=10)

        #-----------------------------------Ganador Oct1
        cuar11=Label(frame_cuartos1, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        cuar11.pack(pady=(30,3))
        cuar11.bind("<Button-1>", lambda e: rellenar(cuar11, semis11, e))

        #-----------------------------------Ganador Oct2
        cuar12=Label(frame_cuartos1, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        cuar12.pack(pady=(3,70))
        cuar12.bind("<Button-1>", lambda e: rellenar(cuar12, semis11, e))

        #-----------------------------------Ganador Oct3
        cuar21=Label(frame_cuartos1, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        cuar21.pack(pady=(70,3))
        cuar21.bind("<Button-1>", lambda e: rellenar(cuar21, semis12, e))

        #-----------------------------------Ganador Oct4
        cuar22=Label(frame_cuartos1, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        cuar22.pack(pady=(3,30))
        cuar22.bind("<Button-1>", lambda e: rellenar(cuar22, semis12, e))

        #---------------------------------------------------------CUARTOS 2
        label_cuartos2=Label(frame_eliminatorias, text="Cuartos", bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_cuartos2.grid(row=0, column=5, pady=5, padx=10)

        frame_cuartos2=Frame(frame_eliminatorias, bg="#1232d5")
        frame_cuartos2.grid(row=1, column=5, pady=10, padx=10)

        #-----------------------------------Ganador Oct5
        cuar31=Label(frame_cuartos2, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        cuar31.pack(pady=(30,3))
        cuar31.bind("<Button-1>", lambda e: rellenar(cuar31, semis21, e))

        #-----------------------------------Ganador Oct6
        cuar32=Label(frame_cuartos2, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        cuar32.pack(pady=(3,70))
        cuar32.bind("<Button-1>", lambda e: rellenar(cuar32, semis21, e))

        #-----------------------------------Ganador Oct7
        cuar41=Label(frame_cuartos2, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        cuar41.pack(pady=(70,3))
        cuar41.bind("<Button-1>", lambda e: rellenar(cuar41, semis22, e))

        #-----------------------------------Ganador Oct8
        cuar42=Label(frame_cuartos2, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        cuar42.pack(pady=(3,30))
        cuar42.bind("<Button-1>", lambda e: rellenar(cuar42, semis22, e))
        
        #-----------------------------------------Lista Cuartos
        lista_cuartos=[cuar11,cuar12,cuar21,cuar22,cuar31,cuar32,cuar41,cuar42]

        
        

        #---------------------------------------------------------SEMIS 1
        label_semis1=Label(frame_eliminatorias, text="Semis", bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_semis1.grid(row=0, column=2, pady=5, padx=10)

        frame_semis1=Frame(frame_eliminatorias, bg="#1232d5")
        frame_semis1.grid(row=1, column=2, pady=10, padx=10)

        #-----------------------------------Ganador Cuar1
        semis11=Label(frame_semis1, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        semis11.pack(pady=(70,3))
        semis11.bind("<Button-1>", lambda e: rellenar_especial(semis11, semis12, final11, final21, e))

        #-----------------------------------Ganador Cuar2
        semis12=Label(frame_semis1, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        semis12.pack(pady=(3,70))
        semis12.bind("<Button-1>", lambda e: rellenar_especial(semis12, semis11, final11, final21, e))

        #---------------------------------------------------------SEMIS 2
        label_semis2=Label(frame_eliminatorias, text="Semis", bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_semis2.grid(row=0, column=4, pady=5, padx=10)

        frame_semis2=Frame(frame_eliminatorias, bg="#1232d5")
        frame_semis2.grid(row=1, column=4, pady=10, padx=10)

        #-----------------------------------Ganador Cuar3
        semis21=Label(frame_semis2, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        semis21.pack(pady=(70,3))
        semis21.bind("<Button-1>", lambda e: rellenar_especial(semis21, semis22, final12, final22, e))

        #-----------------------------------Ganador Cuar4
        semis22=Label(frame_semis2, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        semis22.pack(pady=(3,70))
        semis22.bind("<Button-1>", lambda e: rellenar_especial(semis22, semis21,final12, final22, e))
        
        #-----------------------------------Lista Semis
        lista_semis=[semis11,semis12,semis21,semis22]
        
        


        #---------------------------------------------------------FINAL
        label_jugador=Label(frame_eliminatorias, text=usuario, bg="#1232d5",font=("Times", 18, "bold"))
        label_jugador.grid(row=0, column=3, pady=5, padx=10)

        frame_final=Frame(frame_eliminatorias, bg="#1232d5")
        frame_final.grid(row=1, column=3, pady=10, padx=10)

        #-----------------------------------Campeon
        label_campeon=Label(frame_final, text="Campeon",bg="#1232d5", fg="#ffffff", font=("Times", 16, "bold"))
        label_campeon.pack(pady=(10,2))

        campeon=Label(frame_final, text=" ",bg="#C9CB23", font=("Times", 15, "bold"), width=15)
        campeon.pack(pady=(2,10))

        #-----------------------------------Ganador Semis1
        label_final=Label(frame_final, text="Final",bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_final.pack(pady=(5,2))

        final11=Label(frame_final, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        final11.pack(pady=(5,3))
        final11.bind("<Button-1>", lambda e: rellenar(final11, campeon, e))

        #-----------------------------------Ganador Semis2
        final12=Label(frame_final, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        final12.pack(pady=(3,40))
        final12.bind("<Button-1>", lambda e: rellenar(final12, campeon, e))
        
        #----------------------------------Lista Final
        lista_final=[final11,final12]
        
        
        #---------------------------------------------------------CONSOLACION
        #-----------------------------------Perdedor Semis1
        label_conso=Label(frame_final, text="Consolacion",bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_conso.pack(pady=(35,2))

        final21=Label(frame_final, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        final21.pack(pady=(3,3))
        final21.bind("<Button-1>", lambda e: rellenar(final21, tercero, e))

        #-----------------------------------Perdedor Semis2
        final22=Label(frame_final, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        final22.pack(pady=(3,10))
        final22.bind("<Button-1>", lambda e: rellenar(final22, tercero, e))
        
        #---------------------------------------Lista Consolacion
        lista_consolacion=[final21,final22]

        #-----------------------------------Tercero
        label_tercero=Label(frame_final, text="Tercero",bg="#1232d5", fg="#ffffff", font=("Times", 15, "bold"))
        label_tercero.pack(pady=(15,2))

        tercero=Label(frame_final, text=" ",bg="white", font=("Times", 12, "bold"), width=12)
        tercero.pack(pady=(2,10))



        ventanita.mainloop()

    else:
        messagebox.showwarning("ATENCIÓN!!","Debes introducir un nombre valido!!")




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

