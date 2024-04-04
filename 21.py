'''
En la Ciudad de Buenos Aires, Los primos María Sofía e Ignacio,
decidieron para controlar el negocio familiar y le solicitan a Ud.
que le realicen un pequeño programa para registrar y obtener
información sobre las ventas de productos
informáticos que ellos distribuyen.

Los datos a ingresar son:

-Nro de factura (Finaliza la carga cuando la factura es 0 , no puede ser negativa)
-Nombre del cliente.
-Producto puede ser : 1-Memoria 2-CPU 3-Disco
 (El producto 1 vale : 100 , El producto 2 vale : 200, El producto 3 vale : 300)
-Cantidad

Se solicita obtener la siguiente información una vez finalizada la carga
En cada venta se registra un solo producto
1-Total facturado.
2-Factura de mayor importe.
3-Número de Factura con menor cantidad de productos solicitados.
4-¿Cual fue el producto más vendido?
5-Promedio de ventas de cada producto.
6- ¿ Que te pareció el ejercicio ?
'''
valor_memo = 100
valor_cpu = 200
valor_disco = 300
total_facturado = 0
cant_memo = cant_cpu = cant_disco = 0
cont_memo = cont_cpu = cont_disco = 0

n_factura = int(input('Ingrese el numero de la factura: '))
while n_factura < 0:
    n_factura = int(input('Re-Ingrese el numero de la factura: '))

while n_factura != 0:
    nombre_cli = input('Ingrese nombre de cliente: ')
    while nombre_cli == "":
        nombre_cli = input('Re-Ingrese nombre de cliente: ')
    cod_producto = int(input('Ingrese codigo producto 1-Memoria 2-CPU 3-Disco: '))
    while cod_producto < 1 or cod_producto > 3:
        cod_producto = int(input('Re-Ingrese codigo producto 1-Memoria 2-CPU 3-Disco: '))
    cantidad = int(input('Ingrese la cantidad: '))
    while cantidad < 1:
        cantidad = int(input('Re-Ingrese la cantidad: '))
    
    if cod_producto == 1:
        sub_total = valor_memo * cantidad
        cant_memo += cantidad
        cont_memo += 1
    elif cod_producto == 2:
        sub_total = valor_cpu * cantidad
        cant_cpu += cantidad
        cont_cpu += 1
    else:
        sub_total = valor_disco * cantidad
        cant_disco += cantidad
        cont_disco += 1

    if total_facturado == 0:
        max_facturado = sub_total
        max_factura = n_factura
        min_factura = n_factura
        min_cantidad = cantidad
    else:
        if max_facturado < sub_total:
            max_facturado = sub_total
            max_factura = n_factura
        if min_cantidad > cantidad:
            min_factura = n_factura
            min_cantidad = cantidad             

    total_facturado += sub_total

    n_factura = int(input('Ingrese el numero de la factura: '))
    while n_factura < 0:
        n_factura = int(input('Re-Ingrese el numero de la factura: '))

if total_facturado != 0:
    print()
    print(f"El total facturado es de ${total_facturado}")
    print(f'La maxima factura fue de ${max_facturado} con numero {max_factura}')
    print(f'La factura de menor cantidad es {min_factura} con {min_cantidad}')
    mayor_vendido = cant_memo
    mayor_producto = "Memoria"
    if mayor_vendido < cant_cpu:
        mayor_vendido = cant_cpu
        mayor_producto = "CPU"
    if mayor_vendido < cant_disco:
        mayor_vendido = cant_disco
        mayor_producto = "Disco"
    print(f'El producto mayor vendido fue {mayor_producto} con {mayor_vendido} unidades')
    if cont_memo != 0:
        prom_memo = cant_memo/cont_memo
    else:
        prom_memo = 0
    if cont_cpu != 0:
        prom_cpu = cant_cpu/cont_cpu
    else:
        prom_cpu = 0
    if cant_disco != 0:
        prom_disco = cant_disco/cont_disco
    else:
        prom_disco = 0
    print(f'El promedio de memorias es de {prom_memo:.2f} unidades')
    print(f'El promedio de cpu es de {prom_cpu:.2f} unidades')
    print(f'El promedio de discos es de {prom_disco:.2f} unidades')
else:
    print("No hay datos a mostrar!")