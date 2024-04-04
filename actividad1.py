num1 = int(input("Agregar primer numero: "))
num2 = int(input("Agregar segundo numero "))
operacion = int(input("1 -suma 2 -resta 3 -multi 4 -div 5-pot "))

if (operacion<1  or operacion>5):
    print("error, te equivocaste el numero")

elif (operacion==1):
    suma = num1 + num2
    print(f"la suma es: {suma}")
elif (operacion==2):
    resta = num1 - num2
    print(f"la resta es: {resta}")
elif (operacion==3):
    multi = num1 * num2
    print(f"la multiplicacion es: {multi}")
elif (operacion==4):
        if(num2 !=0):
                div = num1 / num2
                print(f"la division es: {div}")
        else:
                print("el segundo numero ingresado es 0. no se puede dividir")
elif(operacion==5):
    pot = num1 ** num2
    print(f"la potencia es: {pot}")



