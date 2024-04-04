cont=0
cont1=0
edad= int(input("ingresa la edad"))
while (edad >0):
    cont1+=1
    if (edad>18):
        cont=+1
if(cont !=0):
    print("porcentaje de personas mayores de edad: ", cont*100/cont1)