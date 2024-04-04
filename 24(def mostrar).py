def mostrar(vector):
    for i in range(len(vector)):
        print(vector [i], end= " ")

def promedio (vector):
    acumulador = 0
    for i in range(0, len(vector)):
        acumulador += vector[i]
    promedio = acumulador / len(vector)
    return promedio 
# se pone len(vector) para definir la cantidad del vector

def cargar(vector, tope):
    for i in range (tope):
        vector.append(leer_numero())
# vector.append(int(input("Ingresar un valor:   "))) y listo.

def leer_numero():
    return int(input("Ingrese un valor:  "))
#las funciones puede anidarse


vec =[]
vec1 = []
print("Cargando primer vector")
cargar(vec, 5)
# 5 elementos
print("Cargando segundo vector")
cargar(vec1, 7)
#7 elementos
#vec = [1, 5, 3, 6, 5]
#vec1 =[ -5, -5, -54, -654, 9]
#solo usamos para testear se cargan manualmente.

mostrar (vec)
print()
mostrar (vec1)
print()

#guardo el retorno en una variable
promedio_vec = promedio(vec)
print(f"El promedio del vector es de :{promedio_vec}")

#atrapo el retorno en el print
print(f"El promedio del vector es de :{promedio(vec1)}")

#def f_de_x(x):
#    x = (2 *x) + 3
#    print (x)

#3x = 4
#f_de_x(x)
#x = 5
#f_de_x(x)