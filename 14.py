for i in range(10):
    numero = int(input("ingrese un numero "))
    if i ==0:
        maximo = numero
    else:
        if numero > maximo:
            maximo = numero
print("el valor maximo leido es: ", maximo)