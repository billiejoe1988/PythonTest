cantaprobados = 0
cantalumnos = int(input("ingrese la cantidad de alunos que va ingresar"))
for i in range(cantalumnos):
    nota1= int(input("ingrese la nota del primer parcial "))
    nota2= int(input("ingrese la nota del segundo parcial"))
    if nota1>= 4 and nota2> 4:
        print("aprobo la materia")
        cantaprobados +=1
    elif (nota2 >= 4 and nota2 < 4) or (nota1 <4 and nota2 >=4):
        print("recupera un parcial")
    else:
        print("recursa")
print("la cantida de alumnos aprobados es: ", cantaprobados)