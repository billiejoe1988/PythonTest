# #el while se usa para iterar y tambien para validar
# #ejemplo

i=0
while (i<=10):
    print("Con while camino: ",i)
i=i+1
    
#importante colocar el contador dentro del ciclo while y colocar un i=0 para inicializar.
#para validar.
#si la edad es negativa o mayor que 60 que me la vuelva a pedir

edad = int(input("Ingrese una edad: "))
while (edad<=0 or edad>=60):
     edad = int(input("Ingrese una edad VALIDA: "))
print("LA EDAD ES : ",edad)