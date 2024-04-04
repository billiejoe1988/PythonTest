suma= 0
cantidad =0
producto =1
for i in range (10):
    nro = int(input("ingrese un numero: "))
    if nro >= 6:
        cantidad += 1
        suma += nro
    else:
        producto = producto * nro
if cantidad != 0:
    print("el promedio de los numeros mayores o iguales a 6 es: %f "%(suma/cantidad))
else:
    print("no se puede calcular el promedio")
print("el producto de los numeros menores que 6: ", producto)