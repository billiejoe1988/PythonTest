"""
       vector     vector     vector
       nombre      dni        edad
0       alejo     25142569      24
1       alex      52548563      18    
2       claudio   21551394      52 
3       lara      62542152      21
4       leo       94245444      26
"""
def ordenar (criterio, vec, vec1):
    for i in range (0, len(criterio)-1, ):
        for j in range (i+1, len(criterio)):
            if criterio [i] > criterio [j]:
                swap (criterio, i, j)
                swap(vec, i,j)
                swap(vec1, i,j)

def swap (vec, i,j):
    aux = vec[i]
    vec[i]= vec[j]
    vec[j]= aux


def cargar (vec_nom, vec_dni, vec_edad):
    edad = int(input("Ingresar edad:   "))
    while edad < 0 or edad > 120:
        edad = int(input("ingrese la edad:  "))
    while edad !=0:
        nombre = input("Ingrese el nombre:  ").capitalize()
        while nombre == "":
            nombre = input("re-ingrese el nuombre: ").capitalize()
        dni = int(input("Ingree el dni:  "))
        while dni <1:
            dni = int(input("Ingrese el dni:  "))
        vec_edad.append(edad)
        vec_nom.append(nombre)
        vec_dni.append(dni)

        edad = int(input("Ingrese la edad:  "))
        while edad < 0 or edad > 120:
            edad = int(input("Ingresar la edad:   "))

def mostrar (vec_nom, vec_edad, vec_dni):
    print ("Nombre\tDocumento\tEdad")
    for i in range(len(vec_nom)):
        print(f"{vec_nom[i]}\t{vec_dni[i]}\t{vec_edad[i]}")

def buscar_post_mayor(vec):
    pos_max =0
    for i in range(len(vec)):
        if vec[pos_max] < vec[i]:
            pos_max = i
    return pos_max

def insertar (vec_nom, vec_edad, vec_dni, pos_a_insertar):
    edad = int(input("Ingresar edad:   "))
    while edad < 0 or edad > 120:
        edad = int(input("ingrese la edad:  "))
    while edad !=0:
        nombre = input("Ingrese el nombre:  ").capitalize()
        while nombre == "":
            nombre = input("re-ingrese el nuombre: ").capitalize()
        dni = int(input("Ingree el dni:  "))
        while dni <1:
            dni = int(input("Ingrese el dni:  "))
        vec_edad.insert(pos_a_insertar, edad)
        vec_nom.insert(pos_a_insertar, nombre)
        vec_dni.insert(pos_a_insertar, dni)


def remove_m3 (vec_nom, vec_edad, vec_dni) :
    i = 0
    while i > len(vec_dni):
        if vec_dni[i] %3 == 0:
            vec_dni.remove(vec_dni[i])
            vec_nom.remove(vec_nom[i])
            vec_edad.remove(vec_edad[i])
            i - 1 
        else:
            i +1

def main ():
        nombres = []
        documentos = []
        edades = []
        cargar (nombres, documentos, edades)
        if len(nombres) == 0:
            print("No se ingresaron datos")
        else:
            print("La lista de datos")
            mostrar(nombres, documentos, edades)
            ordenar(nombres, documentos, edades)
            print("La lista de datos ordenados por nombre")
            mostrar(nombres, documentos, edades)
            ordenar(edades, documentos, nombres)
            print("lista buscando el pos max")
            mostrar(nombres, documentos, edades)
            pos_max = buscar_post_mayor(edades)
            print(f"la posicion del mayor en edad es es la {pos_max}")
            mostrar(nombres, documentos, edades)
            insertar(nombres, documentos,edades, pos_max+1)
            print("los multiple de 3 eliminados son")
            mostrar(nombres, documentos, edades)
            remove_m3(nombres, documentos, edades) 
main()