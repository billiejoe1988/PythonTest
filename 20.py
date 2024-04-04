"""
metodo ruso
Primero vamos a viajar a Rusia donde aprenderás cómo multiplicar por el método ruso.
En ambos casos vamos a utilizar como ejemplo la misma multiplicación: 34 x 21

Este método se basa en la descomposición de números en base 2. Aunque así explicado puede resultar un poco difícil, 
verás como realizar multiplicaciones con este método es sencillo. Solo hay que seguir los siguientes pasos.
"""
#multiplicacion de un numero y por otro lado dividiendo por 2... y dejas de hacer
#tachas pares. sumando valores es impar del la columna doble
#resultado es = a la multiplicacion de n1 y n2

multi = 0


num1 = int(input("Ingresar primer número:   "))
num2 = int(input("Ingresar segundo número:   "))

#%2==0  par
#%2 != 0 impar

while (num2 !=0):
      if (num2%2 != 0):
      
         multi += num1 
      num1 *= 2
      num2 = (num2//2) 
      print(num1)
      print(num2)
print(f"El resultado es, {multi}")
