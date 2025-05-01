from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")
ventana.resizable(False, False)
ventana.configure(background="#79d8d5")

#Funciones
operacion = ""
resultado = StringVar()

def borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0, END)

def pulsar(valor):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0, END)
    pantalla.insert(0, operacion)
    
def calcular():
    global operacion
    global resultado
    try:
        resultado = str(eval(operacion))
    except:
        resultado = "Error"
    finally:
        pantalla.delete(0, END)
        pantalla.insert(0, resultado)

#Display / pantalla
pantalla = Entry(ventana, font=("Arial", 20, "bold"), borderwidth=2)
pantalla.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

#Boton Reset / AC
borderradius = 5

boton_reset = Button(ventana, text="AC", font=("Arial", 15), width=5, height=2, background= "#07801b", borderwidth=borderradius, command=lambda:borrar())
boton_reset.grid(row=0, column=3, pady=10)

#Botones por fila
#Fila 1
ancho = 8
alto = 3
borderradius = 5

boton_reset.grid(row=0, column=3, pady=10)
boton_1 = Button(ventana, text="1", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(1))
boton_1.grid(row=1, column=0, padx=0, pady=0)
boton_2 = Button(ventana, text="2", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(2))
boton_2.grid(row=1, column=1, padx=0, pady=0)
boton_3 = Button(ventana, text="3", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(3))
boton_3.grid(row=1, column=2, padx=0, pady=0)
boton_suma = Button(ventana, text="+", width=ancho, height=alto, background="yellow", borderwidth=borderradius, command=lambda:pulsar("+"))
boton_suma.grid(row=1, column=3, padx=0, pady=0)

#Fila 2
boton_4 = Button(ventana, text="4", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(4))
boton_4.grid(row=2, column=0, padx=0, pady=3)
boton_5 = Button(ventana, text="5", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(5))
boton_5.grid(row=2, column=1, padx=0, pady=0)
boton_6 = Button(ventana, text="6", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(6))
boton_6.grid(row=2, column=2, padx=0, pady=0)
boton_resta = Button(ventana, text="-", width=ancho, height=alto, background="yellow", borderwidth=borderradius, command=lambda:pulsar("-"))
boton_resta.grid(row=2, column=3, padx=0, pady=0)

#Fila 3
boton_7 = Button(ventana, text="7", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(7))
boton_7.grid(row=3, column=0, padx=0, pady=0)
boton_8 = Button(ventana, text="8", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(8))
boton_8.grid(row=3, column=1, padx=0, pady=0)
boton_9 = Button(ventana, text="9", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(9))
boton_9.grid(row=3, column=2, padx=0, pady=0)
boton_multiplicacion = Button(ventana, text="*", width=ancho, height=alto, background="yellow", borderwidth=borderradius, command=lambda:pulsar("*"))
boton_multiplicacion.grid(row=3, column=3, padx=0, pady=0)

#Fila 4
boton_punto = Button(ventana, text=".", width=ancho, height=alto,background="yellow", borderwidth=borderradius, command=lambda:pulsar("."))
boton_punto.grid(row=4, column=0, padx=0, pady=3)
boton_0 = Button(ventana, text="0", width=ancho, height=alto, background="#a0c183", borderwidth=borderradius, command=lambda:pulsar(0))
boton_0.grid(row=4, column=1, padx=0, pady=0)
boton_igual = Button(ventana, text="=", width=ancho, height=alto, background="yellow", borderwidth=borderradius, command=lambda:calcular())
boton_igual.grid(row=4, column=2, padx=0, pady=0)
boton_division = Button(ventana, text="/", width=ancho, height=alto, background="yellow", borderwidth=borderradius, command=lambda:pulsar("/"))
boton_division.grid(row=4, column=3, padx=0, pady=0)




ventana.mainloop()
