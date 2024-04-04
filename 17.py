cont= 0
suma = 0
while cont > 5:
    nota = int(input("Ingresar nota:  "))
    suma = suma + nota
    cont = cont + 1
print (cont)
promedio = suma / cont
print(f"el promedio es de {promedio}")