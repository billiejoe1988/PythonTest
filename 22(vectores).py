vector = [1,2,2,3,4,5,6,7,8,9,2,10]

print(f"Primer elemento {vector[0]}")
print(f"primer elemento de otra forma {vector [-10]}")
print(f"muestro invertido {vector[::1]}")

#inserta elemento
vector.insert (3, "insertado")
print(f" insertando un elemento {vector}")

#eliminarelemento
vector.pop(0)
print(f"elimino por posicion {vector}")

#eliminar elemento remove
i=0
while i < len(vector):
    print(f"valor de {i} longitud {len(vector)}")
    if vector [i] ==2:
       vector.remove(2) #valor
       i -=1
    i += 1
    #o
    if vector [i] ==2:
       vector.pop(i) #posicion
    else:
         i += 1



print(f"Elimino por valor {vector}")#borra el primero repetido

for i in range  (len[vector]-1,-1,-1):
    if vector [i] ==2:
        vector.remove(2)

print(f"Elimino por valor {vector}")

#para cargar valores 

vec=  []
num = int(input("ingresar numero:  "))
while num !=0:
    vec.append(num)
    num =int(input("Ingresar numero:  "))
print (vec)

if len(vec) !=0:
    acum =0
    for i in range(len(vec)):
    
       acum += vec[i]
print(f"promedio valores leidos:  {acum/len(vec)}")

#i=0
#vec.append(input("ingrese un valor:   "))
#while vec [i] !=0:
#    vec.append(input("ingresar un valor:  "))
#    i += 1

#print (vec)

