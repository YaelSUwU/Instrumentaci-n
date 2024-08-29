#Factorial de un número 

n = int(input("Ingrese n:\n"))

factorial = 1

if n<0:
    print("Ten cuidado papá")
else:
    if n==0:
        factorial = 1
    if n>0:
        for i in range(1,n+1):
            factorial*=i
print("Factorial de", n,"es igual a",factorial)
print("Factotial (%d) = %g"%(n,factorial))