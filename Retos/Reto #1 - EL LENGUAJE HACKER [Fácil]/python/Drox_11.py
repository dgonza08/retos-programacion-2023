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

def traducir(texto):
    texto = texto.lower()
    traduccion = ""
    for letra in texto:
        if letra in diccionario:
            traduccion += diccionario[letra]
        else:
            traduccion += letra
    return traduccion

texto = input("Ingresa el texto a traducir: ")
print(traducir(texto))