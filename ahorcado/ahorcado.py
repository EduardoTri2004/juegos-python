# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:20:58 2023

Licenciatura en Ingeneria de Datos e Inteligencia Artificial
@author: Gonzalez Trigueros Jesus Eduardo 

@decription: Programa en Python que simula el juego del ahorcado usando varias
colecciones de objetos, modulos y funciones.
Este programa es una versión del clásico juego del ahorcado, donde se genera un 
conjunto de palabras en minúsculas, cada una con definiciones breves. De manera
aleatoria, el programa elige una palabra y exhibe una serie de guiones bajos 
para representar las letras de la palabra oculta. La tarea del usuario consiste 
en intentar adivinar la palabra ingresando letras de manera individual. Si la 
letra propuesta forma parte de la palabra, el programa revela sus posiciones. 
Por otro lado, si la letra no está en la palabra, se registra como un error. 
La partida continúa hasta que el jugador logra adivinar la palabra o alcanza un
máximo de 8 errores. En caso de que el usuario acierte, se muestra la definición 
de la palabra junto con un mensaje de felicitación. Al concluir cada juego, 
se le pregunta al usuario si desea participar nuevamente
"""
# Funcion que crea una lista de separadores con el tamaño de la palabra seleccionada
def separadores(s):
    separadores = ["_" for i in range(len(s))]
    return separadores

# Funcion que muestra en forma de string cualquier lista mandada
def mostrar(l):
    m = " ".join(l)
    return m

# Funcion que encuntra los indices de la ocurrencia de una letra dada
def indices(palabra, lista):
    indices =[i for i in range(len(lista)) if(palabra == lista[i])]
    return indices

# Funcion que inserta una palabra en una lista dados los indices 
def insertar(palabra, l_indices, l_palabra):
    for i in l_indices:
        l_palabra[i] = palabra
    return l_palabra

#Funcion que elimina las vocales acentuadas de una palabra
def acentos(palabra):
    vocales = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
    palabra = list(palabra)
    for i in range(len(palabra)):
        if palabra[i] in vocales:
            palabra[i] = vocales[palabra[i]]
    return "".join(palabra)

import random as rn
d = {"casa":"Edificio para habitar", "músico":"Persona que conoce el arte de la musica o lo ejerce",
     "perro":"Animal doméstico", "gato":"Animal felino", "sol":"Estrella que ilumina la tierra",
     "luna":"Satélite natural de la tierra", "mar":"Gran cuerpo de agua salada", "río":"Corriente de agua natural",
     "flor":"Parte reproductiva de las plantas", "manzana":"Fruta de árbol", "mesa":"Mueble para poner objetos",
     "silla":"Asiento con respaldo", "libro":"Obra escrita encuadernada", "tren":"Medio de transporte sobre rieles",
     "lago":"Gran cuerpo de agua dulce", "pájaro":"Ave voladora", "niño":"Persona joven", 
     "juego":"Lo que estamos haciendo ahorita", "zapato":"Calzado para el pie", "diente":"Todos los tenemos en la boca",
     'elefante': 'Animal mamífero de gran tamaño, con trompa y grandes orejas.',
    'mariposa': 'Insecto volador con alas delicadas y colores brillantes.',
    'computadora': 'Dispositivo electrónico para procesar y almacenar información.',
    'escalera': 'Conjunto de peldaños que sirven para subir o bajar de un lugar a otro.',
    'bicicleta': 'Vehículo de dos ruedas impulsado por pedales.',
    'paraguas': 'Objeto que se utiliza para protegerse de la lluvia.',
    'sandalias': 'Calzado ligero que deja los dedos y parte del pie al descubierto.',
    'globoterraqueo': 'Representación tridimensional de la Tierra.',
    'telescopio': 'Instrumento óptico que permite observar objetos distantes.',
    'heladero': 'Persona que vende helados.'}
vocales = {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú"} # Diccionario de vocales acentuadas para verificar si estan en la palabra
keys = list(d.keys()) # Se crea una lista solo con las llaves del diccionario
while True:
    print("Bienvenido al juego del ahorcado!\n")
    print("Adivina la palabra que estoy pensando")
    palabra = rn.choice(keys) # Se elige una palabra aleatoria de la lista de llaves
    p_aux = acentos(palabra) # Se crea una palabra aux sin acentos
    aux = list(palabra) # La plabra se transforma en lista
    aux_list = [] # aux para agregar las letras ingresadas
    c = 8 # Contador para los intentos (prederterminadamente solo se tiene 8)
    s = separadores(palabra) # se crean los guiones, del tamaño de la letra seleccionada
    print(mostrar(s)) 
    while True:
        p = input("Adivina una letra: ")
        p = p.lower()
        if(p in aux_list): # Caso en el que se ingresa la misma palabra dos veces o mas
            print("Esa palabra ya la ingresaste!")
            continue
        if(p in p_aux): # Preguntamos si la palabra ingresada pertenece a la palabra seleccionada
            if(vocales.get(p) in aux): # Si esa palabra esta acentuada, que ponga la vocal acentuada
                p_a= vocales.get(p)
                aux_list.append(p_a)
                ind = indices(p_a, aux)
                p_encontrada = insertar(p_a, ind, s)
            if(p in aux): # Caso en que la palabra es normal, se inserta
                aux_list.append(p)
                ind = indices(p, aux)
                p_encontrada = insertar(p, ind, s)
        else: # En caso de que la palabra no pertnezca, se disminuye el contador de intentos
            print("Esa letra no forma parte de la palabra intenta con otra!")
            c -= 1
            print(f"Te quedan {c} intentos")
            if(c == 0):
                print("Se te acabaron los intentos, suerte para la proxima")
                print(f"La palabra era {palabra} ")
                break
            continue
        p_e = "".join(p_encontrada) # Se crea una version temporal de la lista en string para poder compararla con la palabra original
        if(p_e == palabra): # si esa version temporal es igual a la palabra seleccionada, se adivino la palabra
            print(f"Felicidades haz adivinado la palabra, la definicion de '{palabra}' es '{d[palabra]}' ")
            break
        print(mostrar(p_encontrada)) # Se muestra la palabra para ver el progreso
    while True: # Blucle para preguntar si quiere seguir jugando
        r = input("Quieres seguirn jugando (s/n)? ")
        if(r == "s" or r == "n"):
            break
    if(r == "n"): # Si no quiere jugar se sale del cilo y termina el juego
        print("Muchas gracias por jugar, hasta luego!!")
        break
