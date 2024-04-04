totalencestados =0
canthombres = 0
cantmujeres =0

edad= int(input("ingresar la edad del encuestado - 0 finaliza la carga"))
while edad < 0 :
    print("error en el ingreso de datos. no puede ingresar valor negativo")
    edad = int(input('ingrese la edad del encuestado - 0 finaliza la carga'))
while edad != 0:
    sexo = input("ingrese el sexo del encuestado (m/f) ")
    while sexo.upper () != "M" and sexo.upper () != "F":
        print("error en el ingreso de datos. debe ingresar M o F")
        sexo = input("ingrese el sexo del encuestado (M/F)")
    totalencestados += 1
    if sexo.upper()== "M":
        canthombres += 1
    else:
        cantmujeres +=1
    edad = int(input('ingrese la edad del encuestado - 0 finaliza la carga'))
    while edad <0:
        print("error en el ingreso de datos. nopuede ingresar un valor negativo")
        edad = int(input("ingresa la edad del encuestado - finaliza la carga"))
    totalencuestados = canthombres + cantmujeres 
    if totalencuestados != 0:
        print("total de encuestados: ", totalencuestados)
        print("total de encuestados hombres: ", canthombres)
        print("total de encuestados mujeres: ", cantmujeres)
        print("porcentaje de encuestados hombres: %.2f" %(canthombres * 100 / totalencuestados))
        print("porcentaje de encuestados mujeres: %.2f " %(cantmujeres * 100 / totalencuestados))