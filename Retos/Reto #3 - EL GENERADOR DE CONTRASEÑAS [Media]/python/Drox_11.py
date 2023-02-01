'''
 Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 Podrás configurar generar contraseñas con los siguientes parámetros:
 - Longitud: Entre 8 y 16.
 - Con o sin letras mayúsculas.
 - Con o sin números.
 - Con o sin símbolos.
 (Pudiendo combinar todos estos parámetros entre ellos)
'''
import time

diccionarioLetras = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
    8 : "i",
    9 : "j",
    10 : "k",
    11 : "l",
    12 : "m",
    13 : "n",
    14 : "ñ",
    15 : "o",
    16 : "p",
    17 : "q",
    18 : "r",
    19 : "s",
    20 : "t",
    21 : "v",
    22 : "w",
    23 : "x",
    24 : "y",
    25 : "z",
    26 : "A",
    27 : "B",
    28 : "C",
    29 : "D",
    30 : "E",
    31 : "F",
    32 : "G",
    33 : "H",
    34 : "I",
    35 : "J",
    36 : "K",
    37 : "L",
    38 : "M",
    39 : "N",
    40 : "Ñ",
    41 : "O",
    42 : "P",
    43 : "Q",
    44 : "R",
    45 : "S",
    46 : "T",
    47 : "V",
    48 : "W",
    49 : "X",
    50 : "Y",
    51 : "Z",
}

diccionarioCaracteres = {
    1 : "-",
    2 : "_",
    3 : ",",
    4 : ";",
    5 : ".",
    6 : ":",
    7 : "{",
    8 : "Ç",
    9 : "}",
    10 : "^",
    11 : "[",
    12 : "+",
    13 : "*",
    14 : "]",
    15 : "º",
    16 : "!",
    17 : "|",
    18 : "·",
    19 : "#",
    20 : "$",
    21 : "%",
    22 : "&",
    23 : "¬",
    24 : "/",
    25 : "(",
    26 : ")",
    27 : "=",
    28 : "'",
    29 : "?",
    30 : "¡",
    31 : "¿",
    32 : "@",
    33 : "<",
    34 : ">"
}

siLongitud = False
siMayusculas = False
siNumeros = False
siSimbolos = False

while siLongitud == False:
    longitud = input("Introduce de cuantos caracteres quieres la contraseña: ")
    longitud = int(longitud)
    if longitud >= 8 and longitud <= 16:
        print("Se generará una contraseña de " + str(longitud) + " caracteres")
        siLongitud = True
    else:
        print("Esa longitud no entra dentro del rango establecido de 8-16 caracteres")
        time.sleep(2)

while siMayusculas == False:
    mayusculas = input("Introduce si quieres incluir mayusculas o no (si o no): ")
    if mayusculas != "si" and mayusculas != "no":
        print("Esa respuesta no es valida, por favor introduzca si o no")
        time.sleep(2)
    else:
        if mayusculas == "si":
            mayusculas = True
        elif mayusculas == "no":
            mayusculas = False
        siMayusculas = True
        if mayusculas == True:
            print("Se generara una contraseña con mayusculas")
        elif mayusculas == False:
            print("Se generara una contraseña sin mayusculas")
        else:
            print("Error inesperado :(")
            time.sleep(2)

while siNumeros == False:
    numeros = input("Introduce si quieres incluir numeros o no (si o no): ")
    if numeros != "si" and numeros != "no":
        print("Esa respuesta no es valida, por favor introduzca si o no")
        time.sleep(2)
    else:
        if numeros == "si":
            numeros = True
        elif numeros == "no":
            numeros = False
        siNumeros = True
        if numeros == True:
            print("Se generara una contraseña con numeros")
        elif numeros == False:
            print("Se generara una contraseña sin numeros")
        else:
            print("Error inesperado :(")
            time.sleep(2)

while siSimbolos == False:
    simbolos = input("Introduce si quieres incluir simbolos o no (si o no): ")
    if simbolos != "si" and simbolos != "no":
        print("Esa respuesta no es valida, por favor introduzca si o no")
        time.sleep(2)
    else:
        if simbolos == "si":
            simbolos = True
        elif simbolos == "no":
            simbolos = False
        siSimbolos = True
        if simbolos == True:
            print("Se generara una contraseña con simbolos")
        elif simbolos == False:
            print("Se generara una contraseña sin simbolos")
        else:
            print("Error inesperado :(")
            time.sleep(2)

def generadorContrasenyas(longitud, mayusculas, numeros, simbolos):
    for i in range(0, longitud):
        return 0
