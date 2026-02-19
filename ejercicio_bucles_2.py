#Adivina el numero digital


import random
intentos = 0
secret = random.randint(1, 20)

while True:
    numero = int(input("Adivina el numero: "))
    intentos = intentos + 1

    #Bloque de ganar
    if numero == secret:
        print(f"Felicidades el numeo es {secret}")
        print(f"En solo {intentos} Intentos")

    #Pistas
    if numero < secret:
        print ("Aun te falta")
    elif numero > secret:
        print("Te has pasado")
    
    #Bloque de vidas

    if intentos >= 5:
        print("Ya has perdido bro")
        break

print("---FIN DEL JUEGO--")
