cont = 0
acum = 0
num = int(input("ingrese un numero"))
while num %2 != 0:
    acum = acum + num
    cont = cont + 1
    num = int(input("ingrese un numero"))
if cont == 0:
    print("no se puede calcular promedio")
else:
    print ("el promedio es: %d" %(acum / cont))