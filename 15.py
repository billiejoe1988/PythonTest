max = 0
temp = int(input("ingrese una temperatura: "))
while temp != 0:
    if (max == 0) or (temp > max):
        max = temp
    temp = int(input("ingrese una temperatura: "))
if max == 0:
    print("no se puede determinar la temperatura maxima")
    print("no se han ingresado a procesar")
else:
    print("la temperatura maxima es ", max)