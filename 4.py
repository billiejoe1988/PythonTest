'''
leer 3 notas
si el promedio es 7 o mas, aprobado
si la tercer nota es menor q 7, a diciembre
si el promedio es aplazo <4 a marzo.
mayor que 9 abanderado
'''

nota1= int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

promedio = (nota1 + nota2 + nota3) /3


if promedio < 4:
    resultado = "Vas a Marzo"
elif promedio < 7 or nota3 < 7:
        resultado = "Estas en marzo"
elif promedio < 9:
    resultado = "aprobado"
else:
    resultado = "abanderado"

print(f"Su promedio es {promedio}, usted esta {resultado}")

