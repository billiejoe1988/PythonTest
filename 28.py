"""
Se ingresan números hasta que se llene 1 vector de 10 elementos
de números pares mayores e iguales a 12 y menores a 60 (VECTOR A)
a) Se genera otro vector con los valores que son superiores al promedio (VECTOR B)
b) Se genera otro vector con los valores que son inferiores a la posición del máximo (VECTOR C)
c) En el vector B insertar después de cada elemento mayor a 20 el numero 999
d) En el vector C insertar antes de cada elemento múltiplo de 7 en subíndice impar, el numero 222
e) Eliminar del vector C los números que no sean 222
f) Ordenar de menor a mayor de forma programática los números del vector A
-	Cada ítem solicitado se pide una vez realizado mostrarlo mediante función programática.
"""
#A = [12, 40, 14, 28, 50, 56, 58, 16, 20, 36]
#promedio = 33
#B = [40, 50, 56, 58, 36]
#pos_max = 6
#C = [12, 40, 14, 28, 50, 56]
# punto c
#B = [40, 999, 50, 999, 56, 999, 36, 999]
# punto d
#C = [12, 40, 14, 222, 28, 50, 56]
# punto e
#C = [222]
# punto f
#A = [12, 14, 16, 20, 28, 36, 40, 50, 56, 58]

def mostrar (vec):
    for i in range (len(vec)):
         print(vec[i], end = " ")
 
def cargar (vec, tope):
    while len(vec) < tope :
        num = int(input("Ingresar valor:  "))
        if num % 2 ==0:
            if num >= 12 and num < 60:
                vec.append(num)
            
def promedio (vec,tope):
    acum =0
    for i in range (len(vec)):
        acum += vec[i] 
        prom = acum / tope
    return prom

def pos_max(vec):
    posmax =0
    for i in range (len(vec)):
        if vec[posmax] < vec[i]:
            posmax = i
    return posmax

def carga_mayor (vec, vec1,prom):
    for i in range (len(vec)):
        if vec[i] > prom:
           vec1.append(vec)

def cargar_menor(vec,vec2,posmax):
    for i in range(len(vec)):
        if vec [i] < posmax:
            vec2.append(vec[i])

def insert_b (vec1, numero, tope):
    i = 0
    while i < (len(vec1)):
        if vec1[i] > tope:
            vec1.insert(numero)
            i += 1
        i += 1

def insert_c (vec2, multiplo,numero):
    i = 0
    while i < (len(vec2)):
        if vec2 [i] %multiplo == 0 and i %2 == 0:
           vec2.insert(i-1, numero)
           i += 1
        i += 1

def eliminar (vec2, numero): 
    i = 0
    while i < len(vec2):
        if vec2[i] != numero:
            vec2.remove(vec2[i])
            i -= 1
        else:
            i += 1

def ordenar (vec):
    for i in range (len(vec)):
       print(vec[i], end = " ")

    vec.sort()

    print("ordenado de menor a mayor")
    for i in range (len(vec)):
        print(vec[i], end = "  ")

#def ordenar (vec):
#    for i in range (0, len(vec)-1):
#        for j in range (i+1, len(vec)):
#            if (vec[i]) > vec[j]:
#                swap(vec, i,j) 
#            
#def swap (vec,i,j):
#    aux = vec[i]
#    vec [i] = vec[j]
#    vec[j] = aux

va=[]
vb=[]
vc=[]

cargar(va, 10)
mostrar(va)
print("Valores cargados")
prom = promedio(va, 10)
print(f"El promedio es {prom}")
carga_mayor(va, vb, prom)
mostrar(vb)
print("Son los cargados al vector b")
posmax = pos_max(va)
print(f"la Posicion maxima es {posmax}")
cargar_menor(va, vc, posmax)
mostrar(vc)
print("Son los cargados al vector c")
insert_b(vb, 999, 20)
mostrar(vb)
print("Con valores insertados en B")
insert_c(vc, 7, 222)
mostrar(vc)
print("con valores insertados en C")
eliminar(vc, 222)
mostrar(vc)
print("Con las eliminaciones")
ordenar (va)
