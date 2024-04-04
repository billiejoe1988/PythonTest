numero = int(input("ingrese un numero"))
maximo = numero
for i in range (10):
    numero = int(input("ingrese un numero"))
    if numero > maximo:
        maximo = numero
print("el valor maximo leido es: ", maximo)