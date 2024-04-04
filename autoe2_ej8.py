num=int(input("ingrese la temperatura del dia"))
maxt=num
dia=1
for i in range (2,31):
    num= int(input("ingrese la temperatura del dia"))
    if num>maxt:
        maxt=num
        dia=i
print("el dia de mayor temperatura fue el ", dia)