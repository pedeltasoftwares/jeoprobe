import sys
import os
sys.path.append(os.getcwd())
from customtkinter import *
from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog
import re
import numpy as np
import shutil

def ventana_senales_peer():

    global senales_peer,textbox_ruta_carpeta_senales_peer,boton_siguiente_senales_peer,seleccionar_sismos

    """
    SELECCIONAR CARPETA DONDE ESTÁN LAS SEÑALES DEL PEER
    """
    try:
        seleccionar_sismos.destroy()
    except:
        pass

    #Ventana top level
    senales_peer = CTkToplevel()
    #Nombre de la ventana
    senales_peer.title("Examinar")
    #Resizable
    senales_peer.resizable(False,False)
    senales_peer.transient(menu_window)
    senales_peer.grab_set()
    #Tema de la ventana
    set_appearance_mode("light")
    #Geometría
    width = 400
    height = 130
    screen_width = senales_peer.winfo_screenwidth()
    screen_height = senales_peer.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    senales_peer.geometry(f"{width}x{height}+{x}+{y}")
    #Ícono ventana
    senales_peer.after(201, lambda :senales_peer.iconbitmap("icono_principal.ico"))
    #Label
    label = CTkLabel(master=senales_peer,text=f"Ruta de almacenamiento señales PEER: ",font=('Gothic A1',13))
    label.place(x=20,y=5)
    #Textbox de la ruta de carpeta
    textbox_ruta_carpeta_senales_peer = CTkTextbox(master=senales_peer,font=('Gothic A1',12), text_color=("gray10", "gray90"),width=270,height=10,state=DISABLED,activate_scrollbars=False)
    textbox_ruta_carpeta_senales_peer.place(x=20,y=40)
    #Boton examinar
    boton_examinar_ruta = CTkButton(master= senales_peer, text="Examinar", width=80, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75,command=seleccionar_ruta_senales_peer)
    boton_examinar_ruta.place(x=300,y=40)
    #Boton siguiente señales peer
    boton_siguiente_senales_peer = CTkButton(master= senales_peer, text="Siguiente", width=80, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75,state=tkinter.DISABLED,command=verificar_sismos_peer)
    boton_siguiente_senales_peer.place(x=160,y=85)

def seleccionar_ruta_senales_peer():

    global textbox_ruta_carpeta_senales_peer, carpeta_senales,boton_siguiente_senales_peer

    carpeta_senales = filedialog.askdirectory()

    if carpeta_senales:

        # Muestra la ruta del archivo en el textbox
        textbox_ruta_carpeta_senales_peer.configure(state=NORMAL)
        textbox_ruta_carpeta_senales_peer.delete(0.0,"end")
        textbox_ruta_carpeta_senales_peer.insert(0.0,carpeta_senales)
        textbox_ruta_carpeta_senales_peer.configure(state=DISABLED)

        #Habilita el botón de siguiente
        boton_siguiente_senales_peer.configure(state=NORMAL)

def verificar_sismos_peer():

    global textbox_ruta_carpeta_senales_peer,senales_peer

    #Warning si la carpeta está vacía
    if len(os.listdir(carpeta_senales)) == 0:

        window_logs = CTkToplevel()
        window_logs.title("Error")
        window_logs.resizable(False,False)
        window_logs.transient(senales_peer)
        window_logs.grab_set()
        width = 200
        height = 100
        screen_width = window_logs.winfo_screenwidth()
        screen_height = window_logs.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window_logs.geometry(f"{width}x{height}+{x}+{y}")
        #Ícono ventana
        window_logs.after(201, lambda :window_logs.iconbitmap("error.ico"))
        #Label
        label_log = CTkLabel(master=window_logs,text=f"Carpeta vacía. \nPor favor seleccione otra.",font=('Gothic A1',13))
        label_log.place(x=30,y=18)
        #Botón de ok
        OKBoton_window_log = CTkButton(master= window_logs,text="OK", width=50, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75, command=window_logs.destroy)
        OKBoton_window_log.place(x=80,y=65)
        
    else:
        contiene_AT2 = False
        #Warning si no hay extensiones correspondientes a .AT2
        for archivo in os.listdir(carpeta_senales):
            if archivo.endswith(".AT2"):
                contiene_AT2 = True
                break
        
        if contiene_AT2:
            # Cerrar la ventana actual
            senales_peer.destroy()
            seleccionar_sismos_peer()

        else:
            window_logs = CTkToplevel()
            window_logs.title("Error")
            window_logs.resizable(False,False)
            window_logs.transient(senales_peer)
            window_logs.grab_set()
            width = 200
            height = 100
            screen_width = window_logs.winfo_screenwidth()
            screen_height = window_logs.winfo_screenheight()
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            window_logs.geometry(f"{width}x{height}+{x}+{y}")
            #Ícono ventana
            window_logs.after(201, lambda :window_logs.iconbitmap("error.ico"))
            #Label
            label_log = CTkLabel(master=window_logs,text=f"Archivos no válidos.",font=('Gothic A1',13))
            label_log.place(x=45,y=18)
            #Botón de ok
            OKBoton_window_log = CTkButton(master= window_logs,text="OK", width=50, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75, command=window_logs.destroy)
            OKBoton_window_log.place(x=80,y=55)

def seleccionar_sismos_peer():

    global seleccionar_sismos,file_listbox

    #Abrir la ventana para seleccionar sismos
    seleccionar_sismos = CTkToplevel()
    seleccionar_sismos.title("Seleccionar sismos")
    seleccionar_sismos.resizable(False,False)
    seleccionar_sismos.transient(menu_window)
    seleccionar_sismos.grab_set()
    set_appearance_mode("light")
    width = 350
    height = 300
    screen_width = seleccionar_sismos.winfo_screenwidth()
    screen_height = seleccionar_sismos.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    seleccionar_sismos.geometry(f"{width}x{height}+{x}+{y}")
    #Ícono ventana
    seleccionar_sismos.after(201, lambda :seleccionar_sismos.iconbitmap("icono_principal.ico"))
    #Listbox
    file_listbox = tkinter.Listbox(seleccionar_sismos, selectmode=tkinter.MULTIPLE, width=50, height=15)
    file_listbox.place(x=22,y=10)
    files = list_files(carpeta_senales)
    file_listbox.delete(0, tkinter.END)
    for file in files:
        file_listbox.insert(tkinter.END, file)
    #Boton de volver
    boton_volver = CTkButton(master= seleccionar_sismos,text="Volver", width=50, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75, command=ventana_senales_peer)
    boton_volver.place(x=80,y=265)
    #Boton de seleccionar
    boton_seleccionar = CTkButton(master= seleccionar_sismos,text="Escalar sismos", width=50, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75, command=escalar_sismos)
    boton_seleccionar.place(x=190,y=265)

def list_files(directory):

    global earthquak_names

    #lee todos los archivos del directorio
    files = [file for file in os.listdir(directory) if file.endswith(".AT2")]
    #Extrae únicamente los nombres de los sismos
    earthquak_names = []
    for name in files:
        rgx = name.split("_")
        rgx = f"{rgx[0]}_{rgx[1]}"
        if rgx not in earthquak_names:
            earthquak_names.append(rgx)
        
    return earthquak_names

def escalar_sismos():

    global input_factor_escala,escalar_sismos,boton_escalar,sismos_seleccionados

    sismos_seleccionados = [file_listbox.get(idx) for idx in file_listbox.curselection()]

    if len(sismos_seleccionados) == 0:
        window_logs = CTkToplevel()
        window_logs.title("Error")
        window_logs.resizable(False,False)
        window_logs.transient(seleccionar_sismos)
        window_logs.grab_set()
        width = 200
        height = 100
        screen_width = window_logs.winfo_screenwidth()
        screen_height = window_logs.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window_logs.geometry(f"{width}x{height}+{x}+{y}")
        #Ícono ventana
        window_logs.after(201, lambda :window_logs.iconbitmap("error.ico"))
        #Label
        label_log = CTkLabel(master=window_logs,text=f"Debe seleccionar \nal menos un sismo.",font=('Gothic A1',13))
        label_log.place(x=45,y=18)
        #Botón de ok
        OKBoton_window_log = CTkButton(master= window_logs,text="OK", width=50, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75, command=window_logs.destroy)
        OKBoton_window_log.place(x=80,y=60)

    else:

        #destruye la ventana de seleccion de sismos
        seleccionar_sismos.destroy()

        #Abre la ventana para ingresar el factor para escalar sismos
        escalar_sismos = CTkToplevel()
        escalar_sismos.title("Escalar sismos")
        escalar_sismos.resizable(False,False)
        escalar_sismos.transient(menu_window)
        escalar_sismos.grab_set()
        set_appearance_mode("light")
        width = 200
        height = 120
        screen_width = escalar_sismos.winfo_screenwidth()
        screen_height = escalar_sismos.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        escalar_sismos.geometry(f"{width}x{height}+{x}+{y}")
        #Ícono ventana
        escalar_sismos.after(201, lambda :escalar_sismos.iconbitmap("icono_principal.ico"))
        #Label
        label = CTkLabel(master=escalar_sismos,text=f"Factor de escala:",font=('Gothic A1',13))
        label.place(x=50,y=8)
        #entry factor de escala
        factor_escala = ""
        input_factor_escala=CTkEntry(master=escalar_sismos, width=100, placeholder_text='Ej: 1.5')
        input_factor_escala.place(x=50, y=40)
        input_factor_escala.bind("<Leave>", lambda event: verificar_factor_escala())
        #Botón de escalar sismos
        boton_escalar = CTkButton(master= escalar_sismos,text="OK", width=50, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75, state=tkinter.DISABLED, command=funcion_escalar_sismos)
        boton_escalar.place(x=75,y=80)

def verificar_factor_escala():
    global factor_escala

    factor_escala = input_factor_escala.get()

    try:
        if factor_escala != "":
            factor_escala = float(factor_escala)
            boton_escalar.configure(state=tkinter.NORMAL)

    except ValueError:
        window_logs = CTkToplevel()
        window_logs.title("Error")
        window_logs.resizable(False,False)
        window_logs.transient(escalar_sismos)
        window_logs.grab_set()
        width = 200
        height = 100
        screen_width = window_logs.winfo_screenwidth()
        screen_height = window_logs.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window_logs.geometry(f"{width}x{height}+{x}+{y}")
        #Ícono ventana
        window_logs.after(201, lambda :window_logs.iconbitmap("error.ico"))
        #Label
        label_log = CTkLabel(master=window_logs,text=f"El factor de escala debe ser\nun valor número.",font=('Gothic A1',13))
        label_log.place(x=20,y=18)
        #Botón de ok
        OKBoton_window_log = CTkButton(master= window_logs,text="OK", width=50, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75, command=window_logs.destroy)
        OKBoton_window_log.place(x=80,y=60)
        input_factor_escala.delete(0,"end")

def funcion_escalar_sismos():

    #Ruta de almacenamiento
    ruta_documentos = os.path.expanduser("~\\Documents")

    #Destruye la ventana del factor
    escalar_sismos.destroy()

    if "log.log" in os.listdir(ruta_documentos):
        os.remove(f"{ruta_documentos}/log.log")

    def ejecutar_funcion_escalar_sismos():

        #inicializa el diccionario
        sismos = {}
        #Archivos en el directorio
        files_fullPath = os.listdir(carpeta_senales)
        #Lee los archivos seleccionados y los compila todos en un diccionario
        for file_name in sismos_seleccionados:
            sismos[file_name] = {} #inicializa el nombre del sisms
            for rooth_file in files_fullPath:
                if file_name in rooth_file and ".AT2" in rooth_file:
                    #lee el archivo
                    lines = read_earthquakefile(carpeta_senales,rooth_file)
                    #Formatea el archivo de sismo
                    vector, tiempo = format_earthquakefile(lines)
                    #Escala el sismo"
                    vector_escalado = [format(float(valor) * factor_escala, '.7E') for valor in vector]
                    #Almacena las aceleraciones
                    sismos[file_name][lines[1].split(",")[-1].split(" ")[1].split("\n")[0]] = {"vector":vector,"tiempo":tiempo,"vector_escalado":vector_escalado,"name_file": rooth_file.split(".AT2")[0]}
        
        #Escribe los archivos
        write_files(sismos)
        #Genera el log de terminación
        with open(f"{ruta_documentos}/log.log","w") as f:
            pass
        f.close()

    menu_window.after(100,ejecutar_funcion_escalar_sismos)
    generar_ventana_progreso_escalar_sismos()
        
def generar_ventana_progreso_escalar_sismos():

    window_logs_1 = CTkToplevel()
    window_logs_1.title("En progreso")
    window_logs_1.resizable(False,False)
    window_logs_1.transient(menu_window)
    window_logs_1.grab_set()
    width = 200
    height = 80
    screen_width = window_logs_1.winfo_screenwidth()
    screen_height = window_logs_1.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window_logs_1.geometry(f"{width}x{height}+{x}+{y}")
    #Ícono ventana
    window_logs_1.after(1, lambda :window_logs_1.iconbitmap("progreso.ico"))
    #Label
    label_log = CTkLabel(master=window_logs_1,text=f"Escalando sismos...",font=('Gothic A1',13))
    label_log.place(x=45,y=20)

    def destruir_ventana_progreso_escalar_sismos():

        # Ruta del archivo de log
        ruta_documentos = os.path.expanduser("~\\Documents")
        ruta_log = os.path.join(ruta_documentos, "log.log")

        if os.path.exists(ruta_log):

            window_logs_1.after(1000, window_logs_1.destroy)

            window_logs = CTkToplevel()
            window_logs.title("Éxito")
            window_logs.resizable(False,False)
            window_logs.transient(menu_window)
            window_logs.grab_set()
            width = 250
            height = 100
            screen_width = window_logs.winfo_screenwidth()
            screen_height = window_logs.winfo_screenheight()
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            window_logs.geometry(f"{width}x{height}+{x}+{y}")
            #Ícono ventana
            window_logs.after(201, lambda :window_logs.iconbitmap("exito.ico"))
            #Label
            label_log = CTkLabel(master=window_logs,text=f"Sismos escalados correctamente",font=('Gothic A1',13))
            label_log.place(x=28,y=18)
            #Botón de ok
            OKBoton_window_log = CTkButton(master= window_logs,text="OK", width=50, height=12, compound="left",font=('Gothic A1',12),corner_radius=5, border_spacing=6,text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"),hover_color=("gray75", "gray25"),border_color="black",border_width=0.75, command=window_logs.destroy)
            OKBoton_window_log.place(x=100,y=60)
        
        else:
            window_logs_1.after(1000, destruir_ventana_progreso_escalar_sismos)

    destruir_ventana_progreso_escalar_sismos()
    

def write_files(sismos:dict):

    #Ruta de almacenamiento
    ruta_documentos = os.path.expanduser("~\\Documents")

    #verifica si existe una carpeta llamada "input_deepsoil"
    for file in os.listdir(ruta_documentos):
        if "input_deepsoil" in file:
            shutil.rmtree(f"{ruta_documentos}\input_deepsoil")
    
    #Crea la carpeta que almacena el input de deep soil
    os.mkdir(f"{ruta_documentos}\input_deepsoil")
    os.mkdir(f"{ruta_documentos}\input_deepsoil/01_input")
    os.mkdir(f"{ruta_documentos}\input_deepsoil/02_consolidado")

    #Escribe los archivos de entrada para deepsoil
    for sismo in list(sismos.keys()):
        #vector consolidado
        vector_consolidado = []
        for componente in list(sismos[sismo].keys()):
            nombre_archivo = sismos[sismo][componente]["name_file"] + ".txt"
            n_puntos = len(sismos[sismo][componente]["vector_escalado"])
            dt = sismos[sismo][componente]["tiempo"][1]
            cifras_decimales = contar_digitos_despues_del_punto(dt)
            with open(f"{ruta_documentos}\input_deepsoil/01_input/{nombre_archivo}","w") as f:
                #En la primera linea escribe el número de datos y el delta
                f.write(f"{n_puntos}\t{dt}\n")
                #Escribe la aceleración
                for i in range(len(sismos[sismo][componente]["vector_escalado"])):
                    t = round(float(sismos[sismo][componente]['tiempo'][i]),cifras_decimales)
                    a = sismos[sismo][componente]['vector_escalado'][i]
                    f.write(f"{t}\t{a}\n")
            f.close()
            vector_consolidado.append(sismos[sismo][componente]["vector_escalado"])
        
        #Escribe el vector consolidado
        lines = formatear_consolidado(sismos[sismo])

        with open(f"{ruta_documentos}\input_deepsoil/02_consolidado/{sismo}.txt", 'w') as f:
            f.write(f"t (s)\t{list(sismos[sismo].keys())[0]}\t{list(sismos[sismo].keys())[1]}\t{list(sismos[sismo].keys())[2]}\n")
            for line in lines:
                for value in line:
                    f.write(value)
                f.write("\n")

        f.close()
    
    
        
def formatear_consolidado(sismo:dict):
    #Obtiene la longitud del vector de tiempo para cada componente
    n_vector_tiempo = [len(sismo[componente]["tiempo"]) for componente in list(sismo.keys())]
    n_max = max(n_vector_tiempo)

    #nombres de las tres componentes
    componentes = list(sismo.keys())

    #delta de tiempo para redondear
    dt = sismo[componentes[0]]["tiempo"][1]
    cifras_decimales = contar_digitos_despues_del_punto(dt)

    #obtiene los tiempos y las aceleraciones de las tres componentes
    t1,a1 = sismo[componentes[0]]["tiempo"], sismo[componentes[0]]["vector_escalado"]
    t2,a2 = sismo[componentes[1]]["tiempo"], sismo[componentes[1]]["vector_escalado"]
    t3 ,a3 = sismo[componentes[2]]["tiempo"], sismo[componentes[2]]["vector_escalado"]

    #Genera el cuerpo del archivo
    lines = []
    for i in range(n_max):

        tmp_list = []

        #Agrega el tiempo
        try:
            tmp_list.append(f"{round(float(t1[i]),cifras_decimales)}\t")
        except IndexError:
            try:
               tmp_list.append(f"{round(float(t2[i]),cifras_decimales)}\t") 
            except IndexError:
                tmp_list.append(f"{round(float(t3[i]),cifras_decimales)}\t") 
        
        #Agrega las aceleraciones
        try:
            tmp_list.append(f"{a1[i]}\t")
        except IndexError:
            tmp_list.append(f" \t")
        
        try:
            tmp_list.append(f"{a2[i]}\t")
        except IndexError:
            tmp_list.append(f" \t")

        try:
            tmp_list.append(f"{a3[i]}\t")
        except IndexError:
            tmp_list.append(f" \t")

        lines.append(tmp_list)
        
    return lines

def read_earthquakefile(carpeta_senales:str,rooth_file:str):
    #Abre el archivo y lo lee
    with open(f"{carpeta_senales}/{rooth_file}","r") as f:
        lines = f.readlines()
    f.close()

    return lines

def format_earthquakefile(lines:str):

    file_info = lines[4:]

    #Lee las aceleraciones
    tmp_list,vector,tiempo = [], [], []
    for line in file_info:
        numeros = re.findall(r'[-+]?\d*\.?\d+E[+-]?\d+', line)
        tmp_list.append(numeros)
    
    for j in range(len(tmp_list[0])):
        for i in range(len(tmp_list)):
            try:
                vector.append(tmp_list[i][j])
            except IndexError:
                pass
    
    #Hace el vector de tiempo
    numeros = re.findall(r'[-+]?\d*\.\d+|\d+', lines[3])
    numeros = [int(numeros[0]),float(numeros[1])]
    vector_tiempo = np.arange(0, numeros[0] * numeros[1], numeros[1])
    tiempo = [str(valor) for valor in vector_tiempo]
    #elimina el último valor del tiempo siempre y cuando el tamaño del vector de aceleraciones no concuerde con el tamaño del vector de tiempo
    if len(vector) != len(tiempo):
        del tiempo[-1]
        
    return vector, tiempo

def contar_digitos_despues_del_punto(numero_str):
    # Buscar el índice del punto decimal en la cadena
    indice_punto = numero_str.find('.')
    
    # Si no se encuentra el punto decimal o está al final de la cadena, retornar 0
    if indice_punto == -1 or indice_punto == len(numero_str) - 1:
        return 0
    
    # Contar los dígitos después del punto
    digitos_despues_del_punto = len(numero_str) - indice_punto - 1
    return digitos_despues_del_punto

"""
MAIN
"""
#Inicializa la ventana
menu_window = CTk()
#Geometría
width = 300
height = 300
screen_width = menu_window.winfo_screenwidth()
screen_height = menu_window.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
menu_window.geometry(f"{width}x{height}+{x}+{y}")
#Nombre de la ventana
menu_window.title("Procesamiento señales")
#Resizable
menu_window.resizable(False,False)
#Tema de la ventana
set_appearance_mode("light")
#Ícono ventana
menu_window.after(201, lambda :menu_window.iconbitmap("icono_principal.ico"))
#Botón principal
scale_signals_button = CTkButton(master= menu_window, corner_radius=5, height=40, border_spacing=10, text="Escalar señales",text_color=("gray10", "gray90"),fg_color=("gray85", "gray15"), image= CTkImage(Image.open("icono_escalar.png"), size=(30, 30)), anchor="w",font=('Gothic A1',13),command=ventana_senales_peer,hover_color=("gray75", "gray25"),border_color="black",border_width=0.75)
scale_signals_button.place(x=70, y=25)
#Ejecuta la ventana
menu_window.mainloop()

