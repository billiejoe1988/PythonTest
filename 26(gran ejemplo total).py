"""
diseñar las siguientes programa:
a se carga a con 10 numeros pares y b con 10 numeros multiplos de 5.
b carga arreglo c con la suma de cada elemento a con cada elemebto de b
c carga el elemento d con  todosl os elementos de a y a continuacion los elementos b
d invirtir el arreglo a sobre si mismo
e buscar posicion del maximo de b
  mostrar la posicion del maximo y el valor del maximo
  poner enceros los valores a la derecha del mismo
f encontrar el promedio de c
  contar cuantos valores de c hay por encima del promedio
"""
def promediar (vec):
    acum =0
    for elemento in vec:
        acum += elemento
    return acum / len(vec)

def contar_arriba_promedio(vec, promedio):
    cont =0
    for valor in vec:
        if valor >promedio :
            cont += 1
            #se puede usasr el for normal


def poner_en_0(vec, desde):
    for i in range(desde, len(vec)):
        vec [i] =0

def buscar_maximo (vec):
    #siempre calcular la posicion
    pos_max = 0
    #asumo q la posicion 0 esta
    for i in range (len(vec)):
        #recorro vector
        if vec[pos_max] < vec [i]:
            pos_max = i
            #compara todas las posiciones
    return pos_max
    #se queda con la posicion

def invertir_vector(vec):
    for i in range(len(vec)/2):
        intercambiar(vec, i, len(vec)-1-i)

def intercambiar (vec, i , j):
    auxiliar = vec[i]
    vec[i] = vec[j]
    vec[j] = auxiliar

def concatenar_vectores(vec, vec1, vec2):
    """concatenamos vectores"""
    agregar (vec, vec1)
    agregar (vec, vec2)

def agregar(vec, vec1):
    """a un vector le agrega lo del otro"""
    for i in range (len(vec1)):
        vec.append(vec1[i])

def sumar_elementos(vec, vec1, vec2):
    """suma"""
    for i in range(len(vec)):
        vec2[i] = vec[i] + vec1[i]

def cargar (vec, cantidad, multiplo):
    """funcion para mostrar un vector"""
    for i in range (cantidad):
        numero = int(input("Ingrese numero:   "))
        while numero % multiplo !=0:
            numero = int(input("Ingresar nuemero:   "))
        vec.append(numero)

def mostrar(vec, leyenda):
    for i in range (len(vec)):
        print(vec[i], end= " ")

longitud = 10
a= []
b= []
c=[0]*longitud
d=[]
cargar(a, longitud, 2)
cargar(b, longitud, 5)
print("Cargando vectores de numeros pares")
mostrar(a, "mostrando el vector de pares")
print("Cargando multiplos de 5")
mostrar(b, "mostrar el vector nmultiplo de 5: ")
sumar_elementos(a, b, c )
mostrar (c, " mostrando vector generado con la suma de a y b")
concatenar_vectores(d, a, b)
mostrar(d, "mostrar el valor concatenado")
invertir_vector (a)
mostrar (a, "mostrar contenido invertido")
maximo_pos = buscar_maximo(b)
print(f"El elemento maximo del vector B es {b(maximo_pos)}en {maximo_pos} unbicacion")
poner_en_0(0, maximo_pos)
mostrar(b, "mostrando con las posiciones en cero desde el maximo")
prom = promediar(c)
#resumiendo pasos
print(f"la cantidad de valores del vector por arriba del promedio es {contar_arriba_promedio(promediar(c))}")
#version extendida
#prom = promediar(c)
#cantidad = contar_arriba_promedio(c, prom)
#print(f"La cantidad de valores del vetor de arriba del promedio es {cantidad}")