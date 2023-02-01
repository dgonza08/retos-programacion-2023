import time

diccionario = {
    0 : "love",
    1 : "15",
    2 : "30",
    3 : "40"
}

def tenis():
    P1 = 0
    P2 = 0
    salir = False
    while salir == False:    
        entrada = input("Quien a metido punto (P1, P2): ")
        if entrada == "P1":
            P1 += 1
        elif entrada == "P2":
            P2 += 1
        else:
            print("Error, has introducido mal el nombre del jugador, vuelve a introducirlo")
            time.sleep(3)
        if P1 == 3 and P2 == 3:
            print("Deuce")
        elif P1 == 4 and P2 == 3:
            print("Ventaja P1")
        elif P1 == 3 and P2 == 4:
            print("Ventaja P2")
        elif P1 == 4 and P2 == 4:
            P1 = 3
            P2 = 3
            print("Deuce")
        elif (abs(P1 - P2) == 2 and (P1 == 4 or P2 == 4)) or (P1 == 5 or P2 == 5):
            if(P1 > P2):
                print("Ha ganado P1")
            else:
                print("Ha ganado P2")
            salir = True
        else:
            print(diccionario[P1], " - ", diccionario[P2])

tenis()