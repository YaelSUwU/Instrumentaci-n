a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1],[2],[3]]
c=[[0],[0],[0]]

m = len(a) #Número de renglones de a
l = len(a[0]) #Número de columnas de a
n = len(b[0]) #Número de columnas de b

for i in range(m):
    for j in range(n):
        sigma = 0
        for k in range(l):
            sigma += a[i][k]*b[k][j]
        c[i][j] = sigma

print("La respuesta de C es",c)
