""""
nro factura
nombre del cliente
cantidad
producto, 1memoria 2cpu  3 disco

se solicita.
total facturado
factura mayor importe
numero de factura con menor cantidad de productos solicitados
cual fue el producto mas vendido?
promedio de ventas de cada producto
"""
valormemo =100
valorcpu=200
valordisco= 300
totalfacturado =0
cantmemo =0
cantcpu=0
cantdisco =0
contmemo =0
contcpu =0
contdisco =0


fac = int(input("Ingresar numero de factura:   "))

while fac < 0:
    fac = int(input("Ingresar numero de factura:   "))

while fac !=0:
    prod = int(input("Ingresar producto 1-memoria, 2-cpu, 3-disco:   "))
    while prod < 1 or prod > 3 :
        prod = int(input("Ingresar producto, 1-memoria, 2-cpu, 3-disco:  "))
    nom = input("Ingresar nombre del cliente:   ")
    while nom == "":
        nom = input("Ingresar nombre del cliente:   ")
    cant = int(input("Ingresar cantidad vendida:  "))
    while cant < 1:
        cant = int(input("Ingresar cnatidad vendida:   "))

    if prod ==1:
        subtotal = valormemo * cant
        cantmemo += cant
        contmemo += 1
    elif prod ==2:
        subtotal = valorcpu * cant
        cantcpu += cant
        contcpu += 1
    else:
        subtotal = valordisco * cant
        cantdisco += cant
        contdisco += 1
    
    if totalfacturado == 0:
        maxfacturado = subtotal
        maxfactura = fac
        minfactura = fac
        mincantidad = cant

    totalfacturado += subtotal

    if maxfacturado < subtotal:
        maxfacturado = subtotal
        maxfacturado = fac
    if  mincantidad > cant:
        minfactura = fac
        mincantidad = cant

 
    fac = int(input("Ingresar numero de factura:   "))
    while fac < 0:
        fac = int(input("Ingresar numero de factura:"))


if totalfacturado !=0:
   print(f"El total facturado es {totalfacturado}")
   print(f"La maxima factura es de {maxfacturado} con un numero de factura {maxfactura}")
   print(f"La menor cantidad de productos vendidos es de {mincantidad} con numero de factura {minfactura}")
   mayorvendido = cantmemo
   mayorproducto = "memoria"
   if    mayorvendido < cantcpu:
         mayorvendido = cantcpu
         mayorproducto = "cpu"
   if mayorvendido < cantdisco:
         mayorvendido = cantdisco
         mayorproducto = "disco"
   else:
        print(f"El mayor vendido es {mayorproducto} y es con {mayorvendido}")

    if contmemo !=0:
        prommemo = cantmemo / contmemo
    else:
        prommemo = 0
    if contcpu !=0:
       prommemo = cantcpu / contcpu
    else:
        promcpu =0
    if contdisco !=0:
        promdisco = cantdisco / contdisco
    else: promdisco =0

print(f"Promedio de memoria es de {prommemo}")
print(f"Promedio de cpu es de {promcpu}")
print(f"promedio de disco es de {promdisco}")

else:
     print("No hay datos a mostrar")
