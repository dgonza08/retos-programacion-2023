diccionario = {
    "a": "4",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "|=",
    "g": "6",
    "h": "|-|",
    "i": "1",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "|v|",
    "n": "|\\|",
    "o": "0",
    "p": "|*",
    "q": "0,",
    "r": "|2",
    "s": "5",
    "t": "7",
    "u": "|_|",
    "v": "\/",
    "w": "\/\/",
    "x": "><",
    "y": "`/",
    "z": "2"
}

def leet(frase):
    frase = frase.lower()
    textoFinal = ""
    for i in frase:
        if i in diccionario:
            textoFinal += diccionario[i]
        else:
            textoFinal += i
    return textoFinal

entrada = input("Introduce el texto para convertir en leet: ")
print(leet(entrada))