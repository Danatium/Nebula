# ==========================================
# TUTORIAL DE BUCLES EN PYTHON
# ==========================================
import time

def imprimir_titulo(titulo):
    print(f"\n{'-'*40}")
    print(f"   {titulo.upper()}")
    print(f"{'-'*40}")

# ------------------------------------------
# 1. EL BUCLE FOR (Para)
# ------------------------------------------
# El bucle 'for' se usa cuando sabemos cuántas veces queremos repetir algo
# o cuando queremos recorrer una colección de elementos (una lista, texto, etc.)

imprimir_titulo("1. Bucle FOR: Recorriendo una lista")

videojuegos = ["Mario", "Zelda", "Minecraft", "Halo"]

# Aquí le decimos: "Para cada 'juego' dentro de la lista 'videojuegos'..."
for juego in videojuegos:
    print(f" -> Jugando a: {juego}")
    # time.sleep(0.5) # Pausa opcional para efecto dramático

print(" -> Fin de la lista de juegos.")


# ------------------------------------------# ==========================================
# TUTORIAL DE BUCLES EN PYTHON
# ==========================================
import time

def imprimir_titulo(titulo):
    print(f"\n{'-'*40}")
    print(f"   {titulo.upper()}")
    print(f"{'-'*40}")

# ------------------------------------------
# 1. EL BUCLE FOR (Para)
# ------------------------------------------
# El bucle 'for' se usa cuando sabemos cuántas veces queremos repetir algo
# o cuando queremos recorrer una colección de elementos (una lista, texto, etc.)

imprimir_titulo("1. Bucle FOR: Recorriendo una lista")

videojuegos = ["Mario", "Zelda", "Minecraft", "Halo"]

# Aquí le decimos: "Para cada 'juego' dentro de la lista 'videojuegos'..."
for juego in videojuegos:
    print(f" -> Jugando a: {juego}")
    # time.sleep(0.5) # Pausa opcional para efecto dramático

print(" -> Fin de la lista de juegos.")


# ------------------------------------------
# 2. LA FUNCIÓN RANGE()
# ------------------------------------------
# A menudo queremos repetir algo un número específico de veces (ej. 5 veces).
# Para eso usamos range().

imprimir_titulo("2. Bucle FOR con range()")

print("Contando del 0 al 4 (Python empieza en 0):")
for numero in range(5):
    print(f" -> Número: {numero}")

print("\nContando en un rango específico (del 1 al 10, saltando de 2 en 2):")
# range(inicio, fin_sin_incluir, paso)
for impar in range(1, 10, 2):
    print(f" -> Número impar: {impar}")


# ------------------------------------------
# 3. EL BUCLE WHILE (Mientras)
# ------------------------------------------
# El bucle 'while' se usa cuando NO sabemos cuántas veces se repetirá el código.
# Se repite MIENTRAS una condición sea Verdadera (True).

imprimir_titulo("3. Bucle WHILE")

bateria = 3
print("Iniciando dispositivo...")

while bateria > 0:
    print(f" -> Batería al {bateria * 10}%. El dispositivo sigue encendido.")
    bateria = bateria - 1  # ¡IMPORTANTE! Debemos cambiar la variable o el bucle será infinito.

print(" -> Batería agotada. Dispositivo apagado.")


# ------------------------------------------
# 4. CONTROL DE FLUJO: BREAK y CONTINUE
# ------------------------------------------
# A veces necesitamos alterar el comportamiento normal del bucle.
# - break: Rompe el bucle por completo y sale.
# - continue: Salta la vuelta actual y pasa a la siguiente.

imprimir_titulo("4. Break y Continue")

print("Ejemplo de BREAK (Buscando un tesoro):")
objetos = ["roca", "basura", "tesoro", "roca", "agua"]

for objeto in objetos:
    if objeto == "tesoro":
        print(f" -> ¡ENCONTRADO! Hay un {objeto}. Dejo de buscar.")
        break  # Sale del bucle inmediatamente, ignora lo que queda.
    print(f" -> Revisando: {objeto} (no es lo que busco)")

print("\nEjemplo de CONTINUE (Saltando números pares):")
for i in range(1, 6):
    if i % 2 == 0: # Si el número es divisible por 2 (par)
        print(f" -> Saltando el número {i}...")
        continue # Vuelve arriba al inicio del bucle, ignorando el print de abajo.
    
    print(f" -> Procesando número impar: {i}")

imprimir_titulo("FIN DEL TUTORIAL")
# 2. LA FUNCIÓN RANGE()
# ------------------------------------------
# A menudo queremos repetir algo un número específico de veces (ej. 5 veces).
# Para eso usamos range().

imprimir_titulo("2. Bucle FOR con range()")

print("Contando del 0 al 4 (Python empieza en 0):")
for numero in range(5):
    print(f" -> Número: {numero}")

print("\nContando en un rango específico (del 1 al 10, saltando de 2 en 2):")
# range(inicio, fin_sin_incluir, paso)
for impar in range(1, 10, 2):
    print(f" -> Número impar: {impar}")


# ------------------------------------------
# 3. EL BUCLE WHILE (Mientras)
# ------------------------------------------
# El bucle 'while' se usa cuando NO sabemos cuántas veces se repetirá el código.
# Se repite MIENTRAS una condición sea Verdadera (True).

imprimir_titulo("3. Bucle WHILE")

bateria = 3
print("Iniciando dispositivo...")

while bateria > 0:
    print(f" -> Batería al {bateria * 10}%. El dispositivo sigue encendido.")
    bateria = bateria - 1  # ¡IMPORTANTE! Debemos cambiar la variable o el bucle será infinito.

print(" -> Batería agotada. Dispositivo apagado.")


# ------------------------------------------
# 4. CONTROL DE FLUJO: BREAK y CONTINUE
# ------------------------------------------
# A veces necesitamos alterar el comportamiento normal del bucle.
# - break: Rompe el bucle por completo y sale.
# - continue: Salta la vuelta actual y pasa a la siguiente.

imprimir_titulo("4. Break y Continue")

print("Ejemplo de BREAK (Buscando un tesoro):")
objetos = ["roca", "basura", "tesoro", "roca", "agua"]

for objeto in objetos:
    if objeto == "tesoro":
        print(f" -> ¡ENCONTRADO! Hay un {objeto}. Dejo de buscar.")
        break  # Sale del bucle inmediatamente, ignora lo que queda.
    print(f" -> Revisando: {objeto} (no es lo que busco)")

print("\nEjemplo de CONTINUE (Saltando números pares):")
for i in range(1, 6):
    if i % 2 == 0: # Si el número es divisible por 2 (par)
        print(f" -> Saltando el número {i}...")
        continue # Vuelve arriba al inicio del bucle, ignorando el print de abajo.
    
    print(f" -> Procesando número impar: {i}")

imprimir_titulo("FIN DEL TUTORIAL")
