# -*- coding: utf-8 -*-

# importamos funciones y / o Librerias
import funciones
""" apt-get install python-tk  O python3 -m pip install tkinter """
from tkinter import * # se usa para crear ui (en py2 es Tkinter, en py3 cambió a  tkinter, ojo)
from tkinter.ttk import * #se usa para crear la tabla
""" python3 -m pip install numpy """
import numpy as np #usamos numpy.randint() para los aleatorios 
from time import time # Usamos time() para calcular el tiempo de ejecución 
""" python3 -m pip install texttable """
from texttable import Texttable
# Codigo Principal

def testDeFunciones():
    #TEST DE FUNCIONES
    result = 1
    for x in range(20):
        a = np.random.randint(100, 10000)
        b = np.random.randint(100, 10000)
        mcdc = funciones.mcd(a, b)
        mcdf = funciones.mcdFactoresPrimos(a, b)
        mcdr = funciones.RestaSucesivas(a, b)
        x = ""
        if mcdc and mcdf == mcdr:
            # si los 3 MCDs son iguales todo esta bien
            print("Euclides: ",mcdc, "Factores primos: ",mcdf,"Resta sucesiva: ",mcdr)
        else:
            result = 0 # con que una fila no de ya tenemos un problema
            print("Euclides: ",mcdc, "Factores primos: ",mcdf,"Resta sucesiva: ",mcdr," <- X") #la 'x' señala donde no dio igual
    if result: print('\n[SUCESS]\n')
    if not result: print('\n[ERROR]\n')

def getNumerosAleatorios():
    lista = []
    for x in range(100):
        thisdict = {
        "a": np.random.randint(10000,1000000),
        "b": np.random.randint(10000,1000000), 
            # Para una prueba mas ex
        #"a": np.random.randint(1000000,10000000000), # a = Número aleatorio entre un millon y diez mil millones
        #"b": np.random.randint(1000000,10000000000), # b = Número aleatorio entre un millon y diez mil millones
        }
        lista.insert(x, thisdict)
    return lista

def calcularTiempos():
    #logica de calcular mcds y medir tiempos
    listaAleatorios = getNumerosAleatorios()
    t = Texttable(max_width=400)
    t.set_deco(Texttable.HEADER | Texttable.HLINES)
    t.set_cols_align(["c", "c", "c", "c", "c", "c"])
    t.set_cols_width([10, 10, 10, 40, 40, 40])
    t.header(["Variable a", "variable b", "mcd","tiempo euclides (ms)","tiempo factores p. (ms)","tiempo restas (ms)"])
    
    for x in range(100):
        a = listaAleatorios[x].get("a")
        b = listaAleatorios[x].get("b")
        """ millis = (time() - start_time) * 1000 """
        #euclides
        start_time = time( ) # tiempo de inicio
        # run algorithm euclides
        mcd_euclides = funciones.mcd(a, b)
        listaAleatorios[x]["euclides"] = (time() - start_time) * 1000
        listaAleatorios[x]["mcd"] = mcd_euclides
        #factorización
        start_time = time( ) # tiempo de inicio
        # run algorithm factorización
        mcd_euclides = funciones.mcdFactoresPrimos(a,b)
        listaAleatorios[x]["factorizacion"] = (time() - start_time) * 1000
       
        #resta_sus
        start_time = time( ) # tiempo de inicio
        # run algorithm resta_sus
        funciones.RestaSucesivas(a, b)
        listaAleatorios[x]["resta"] = (time() - start_time) * 1000
        t.set_cols_dtype(["t", "t", "t", "t", "t", "t"])
        t.add_row([str(a),str(b),str(mcd_euclides), "{0:.5f}".format(listaAleatorios[x]["euclides"]),"{0:.5f}".format(listaAleatorios[x]["factorizacion"]),"{0:.5f}".format(listaAleatorios[x]["resta"])])
    print (t.draw())
    return listaAleatorios
def calcularPromedios(lista):
    prom_euclides = 0
    prom_fac_pri = 0
    prom_resta_sus = 0
    n = len(lista)
    for x in range(n):
        prom_euclides += lista[x]["euclides"]
        prom_fac_pri += lista[x]["factorizacion"]
        prom_resta_sus += lista[x]["resta"]
    if n == 0: 
        print('Sin Tiempos Promedios, lista sin elementos')
        return {"euclides": 0,"factorizacion": 0,"resta": 0 }
      
    prom = {"euclides": prom_euclides/n, "factorizacion": prom_fac_pri/n,"resta":  prom_resta_sus/n }
    print("\nTiempos Promedios de ejecución para cada algoritmo: \n ")
    print("\nAlgoritmo de euclides: ", "{0:.5f}".format(prom["euclides"]))
    print("\nAlgoritmo de factorizacion en primos: ", "{0:.5f}".format(prom["factorizacion"]))
    print("\nAlgoritmo de restas sucesivas: ", "{0:.5f}".format(prom["resta"]))
    return prom

def dibujarVentana():
    top = Tk()
    top.title("MCD")
    top.overrideredirect(True)
    top.overrideredirect(False)
    top.attributes('-zoomed', True)

    
    # Code to add widgets will go here...
    frame = Frame(top)
    frame.pack(expand=YES, fill=BOTH) # .pack() administrador de geometría, organiza los widgets en bloques antes de colocarlos en el widget principal.
    
    tv = Treeview(frame)
    tv.pack(expand=YES, fill=BOTH)
    tv['columns'] = ('a', 'b', 'mcd','euc', 'fact', 'rest')
    tv.heading("#0", text='', anchor='w')
    tv.column("#0", anchor="w", width=100)
    tv.heading('a', text='Variable A')
    tv.column('a', anchor='center', width=90)
    tv.heading('b', text='Variable B')
    tv.column('b', anchor='center', width=90)
    tv.heading('mcd', text='MCD(A,B)')
    tv.column('mcd', anchor='center', width=80)
    tv.heading('euc', text='T.Euclides (ms)')
    tv.column('euc', anchor='center', width=220)    
    tv.heading('fact', text='T. Factores (ms)')
    tv.column('fact', anchor='center', width=220)   
    tv.heading('rest', text='T. Resto (ms)')
    tv.column('rest', anchor='center', width=220)  
    tv.grid(sticky = (N,S,W,E))
    frame.treeview = tv
    frame.grid_rowconfigure(0, weight = 1)
    frame.grid_columnconfigure(0, weight = 1)
    
    lista = calcularTiempos()
    for x in range(len(lista)):
        frame.treeview.insert('', 'end', text="Fila "+str(x),values=(lista[x]["a"],lista[x]["b"], lista[x]["mcd"],"{0:.5f}".format(lista[x]["euclides"]),"{0:.5f}".format(lista[x]["factorizacion"]),"{0:.5f}".format(lista[x]["resta"])))
    promedios = calcularPromedios(lista)
    frame.treeview.insert('', 'end', text="Promedios",values=("-","-", "-","{0:.5f}".format(promedios["euclides"]),"{0:.5f}".format(promedios["factorizacion"]),"{0:.5f}".format(promedios["resta"])))
    top.mainloop()
    
if __name__ == '__main__':
    testDeFunciones()
    dibujarVentana()

    
