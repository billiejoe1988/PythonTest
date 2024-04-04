vec = [1, 5, 1, 2, 36, 68,8]

productoria =1
#para acumular multiplicaciones buscar cual es el neutro.. osea 1.. sino se multiplica x 0 y es = 0
for i in range (1,len(vec),2):
    productoria *= vec[i]

auxiliar = vec [0]
vec[0] = vec[-1]
vec [-1] = auxiliar
