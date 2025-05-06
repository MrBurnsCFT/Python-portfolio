letras_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letras_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["!", "@", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "¡", "*", "+", "-", "_", ".", ",", ";", ":", "<", ">"]

import random

print("Bienvenido al generador de contraseñas")
cantidad_mayusculas = int(input("Cuantas letras mayusculas quieres? "))
cantidad_minusculas = int(input("Cuantas letras minusculas quieres? "))
cantidad_numeros = int(input("Cuantos numeros quieres? "))
cantidad_simbolos = int(input("Cuantos simbolos quieres? "))

lista = []

#Eleccion de caracteres random 
for i in range(1, cantidad_mayusculas + 1):
    valor = random.choice(letras_mayusculas)
    lista.append(valor)

for i in range(1, cantidad_minusculas + 1):
    valor = random.choice(letras_minusculas)
    lista.append(valor)
    
for i in range(1, cantidad_numeros + 1):
    valor = random.choice(numeros)
    lista.append(valor)
    
for i in range(1, cantidad_simbolos + 1):
    valor = random.choice(simbolos)
    lista.append(valor)
    
#Mezcla de caracteres de la lista
print(lista)
random.shuffle(lista)
print(lista)


#Transformar la lista en una cadena
contraseña = ""
for caracter in lista:
    contraseña += caracter
print(contraseña)