# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:16:43 2023

Licenciatura en Ingeneria de Datos e Inteligencia Artificial
@author: Gonzalez Trigueros Jesus Eduardo 

@decription: Programa en Python que simula el juego del rompecabezas dezlisante
usando varias colecciones de objetos, modulos y funciones.
Este código en Python implementa el juego del rompecabezas deslizante. 
El objetivo del juego es organizar los números del 1 al 15 en un tablero 4x4, 
deslizando los números hacia un espacio en blanco. El programa utiliza 
funciones para imprimir el tablero, validar la posibilidad de resolver el 
rompecabezas, buscar el espacio en blanco, insertar un número en el tablero y 
verificar si el tablero está ordenado correctamente. Además, el código incorpora 
aleatoriedad en la generación del tablero inicial para asegurar la 
solucionabilidad del rompecabezas. El jugador interactúa con el programa 
ingresando el número que desea mover hacia el espacio en blanco. El juego 
continúa hasta que el jugador resuelve el rompecabezas, mostrando el número 
de intentos realizados.
"""
# Imprime el tablero y tabula para que se vea todo ordenado
def imprimir_tablero(lista_tablero):
    for fila in lista_tablero:
        for elemento in fila:
            elemento_str = str(elemento)
            espacio = 2 - len(elemento_str)
            print(" " * espacio + elemento_str + " | ", end='')
        print("\n" + '-' * 18)
    return

# Valida que la configuracion del tablero se pueda solucionar, para eso recorre la lista 
# en un doble ciclo y pone un 1 si algun numero es mayor del actual, al final suma todo
# y lo agrega a una lista y lo retorna
def validacion(tablero):
    n_mayores = []
    for i, num in enumerate(tablero):
        n_may_actuales = sum(1 for numero in tablero[:i] if numero > num)
        n_mayores.append(n_may_actuales)
    return n_mayores

# Buscar el espacio en blanco en el tablero, recorriendolo en un doble ciclo, 
# y a base de condiciones retorna los valores alrededor dependiendo de los valores
def buscar_espacio_en_blanco(matriz):
    numeros_alrededor = []
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == ' ':
                if i > 0:
                    numeros_alrededor.append(matriz[i - 1][j])
                if i < 3:
                    numeros_alrededor.append(matriz[i + 1][j])
                if j > 0:
                    numeros_alrededor.append(matriz[i][j - 1])
                if j < 3:
                    numeros_alrededor.append(matriz[i][j + 1])
    return numeros_alrededor

# Este ciclo encuentra el espacio en blanco y guarda los indices donde esta al igual
# del numero que se va a insertar, luego intervambia los valores
def insertar(tablero, n):
    for i in range(4):
        for j in range(4):
            if(tablero[i][j] == " "):
                fila_vacia = i
                columna_vacia = j
    for i in range(4):
        for j in range(4):
            if(tablero[i][j] == n):
                fila_numero = i
                columna_numero = j
    tablero[fila_vacia][columna_vacia] = n
    tablero[fila_numero][columna_numero] = " "
    return tablero

# Verifica si es tablero esta ordenado o no
def orden_tablero(matrix):
    aux = 1
    for i in matrix:
        for j in i:
            if(j != " " and int(j) != aux):
                return 0
            aux += 1
    return 1
import random as rn
tablero = [[' ' for _ in range(4)] for _ in range(4)] # se genera el tablero, como una matriz de 4 x 4
n_tableros = [i for i in range(1, 16)] # Se cre una lista con los numero paa inicializar el tablero
while True: # Se ordenan de manera aleatoria la configuracion, y se valida que se pueda resolver
    rn.shuffle(n_tableros)
    val = validacion(n_tableros)
    if(sum(val) % 2 == 0):
        break
for i in range(4): # Agregamos los numero al tablero para empezar el juego
    for j in range(4):
        if n_tableros:
            tablero[i][j] = n_tableros.pop(0)
c = 0
print("Bienvenido al juego, mucha suerte !!")
imprimir_tablero(tablero)
while True: # Iniciamos el juego
    aux = buscar_espacio_en_blanco(tablero) # Buscamos el espacio para poder insertar el numero que quiera el usuario
    while True:
        entrada = input("Ingrese el número a mover en el espacio en blanco: ")
        if entrada.isdigit(): # Verificamos, que la entrada sea un numero
            n = int(entrada)
            if n in aux: # Verificamos que sea un numero que este alredrdor del espacio vacio
                break
            else:
                print(f"Por favor ingrese un número válido {aux}")
        else:
            print("Por favor ingrese un número entero válido.")
    tablero = insertar(tablero, n) # Insertamos ese numero, y reasignamos el espacio en blanco
    imprimir_tablero(tablero)
    c += 1 # aumentamos el contador de los intentos
    verificar = orden_tablero(tablero) # Verificamos si el tablero ya quedo en orden, si es asi se acabo el juego
    if(verificar == 1):
        print(f"Felicidades haz logrado completar el juego en: {c} intentos")
        break
