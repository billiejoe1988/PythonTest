"""
Una cadena de hoteles cuenta con varias filiales alrededor del planeta y necesita obtener algunas estadísticas para mejorar sus servicios.
ingresan:
Nombre de la ciudad de la filial
Capacidad total del hotel (en cuanto a huéspedes)
Cantidad de habitaciones
Cantidad de huéspedes alojados en un mes.
La carga de datos finaliza cuando en el nombre del hotel se lee "FIN"

Se pide calcular y mostrar las siguientes estadísticas:

Cantidad de huéspedes que puede alojar toda la cadena de hoteles
Porcentaje de ocupación de cada hotel.
Porcentaje de hoteles que tiene todas sus plazas completas
"""

ciudad = 0
capatotal = 0
habitaciones= 0
huesmes = 0
cadenatotal = 0
prom =0
hotelfull =0
hotel =0
promfull= 0
#usar .upper() en nombre ciudades
ciudad = input("Ingresar Nombre de la ciudad filial: - FIN finaliza la carga de datos")

while ciudad != "FIN":
        captotal = int(input("Ingresar Capacidad total del hotel:  -FIN finaliza la carga de datos"))
        habitaciones = int(input("Ingresar Cantidad de habitaciones:  -FIN finaliza la carga de datos"))
        huesmes = int(input("Ingresar Cantidad de huespedes alojados en un mes: -FIN finaliza carga de datos"))
        if captotal > 0:
          cadenatotal = cadenatotal + captotal
          captotal += 1
          hotel += 1      
        if habitaciones and huesmes > 0:
          prom = (huesmes * 100) // habitaciones
          print(f"el porcentaje de ocupacion de este hotel es {prom}%")
        if prom == 100:
           hotelfull += 1

        ciudad = input("Ingrese Nombre de la ciudad filial: - Fin Finaliza carga de datos")
else :
        ciudad == "FIN"
        promfull = hotelfull *100 // hotel
        print(f"El promedio de hoteles completos es: {promfull}%")
        print(f"La cantidad de huspedes que puede alojar la cadena es: {cadenatotal}")