#Caja Registradora

total = 0

while True:
    precios = float(input("Dame el precio del producto: "))

    if precios == 0:
        print("-> Finalizando comopra")
        break

    if precios < 0:
        print("Valor invalidop, favor de dar otro numero")
        continue

    total = total + precios
    print(f" [SUBTOTAL: ${total} ]")

print(f"-" * 30)
print(f"Total FINAL: ${total} ")

        



