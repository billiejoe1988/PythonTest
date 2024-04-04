totalhuesped = 0
cantidadfiliales = 0
cantidadhotellleno= 0

nombrefilial = input("ingrese la ciudad: ").upper ()
while nombrefilial != "FIN":
    capacidad= int(input("Ingrese capacidad de hotel: "))
    while capacidad < 1:
        capacidad = int(input("Integrese la capacidad del hotel"))
    cantidadhab = int(input("Ingrese la cantidad de habitaciones: "))
    while cantidadhab < 1:
        cantidadhab = int(input("ingrese la cantidad de habitaciones: "))
    cantidadhues= int(input("ingrese cantida de huespedes"))
    while cantidadhues < 0 or cantidadhues > capacidad :
        cantidadhues = int(input("ingrese cantidad de huesped: "))

    totalhuesped += capacidad
    porcentajeocupacion = (cantidadhues *100)//capacidad
    print(f"el porcentaje ocupacional de {nombrefilial} es {porcentajeocupacion}")
    cont_filiales =+ 1
    if porcentajeocupacion == 100:
        cantidadhotellleno += 1

    nombrefilial = input("nombre de ciudad:  ").upper ()

if cont_filiales == 0:
    print("no se encontraron datos")
else:
    print(f"La capacidad total de la cadena es: {totalhuesped}")
    print(f"el porcentaje de filiales al 100% es {cantidadhotellleno / cantidadfiliales *100}")

