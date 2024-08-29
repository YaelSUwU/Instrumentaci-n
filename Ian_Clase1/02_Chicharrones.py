#Chicharronera
#ax^2+bx+c=0
from math import pi

a = float(input("Ingresa a: \n"))
b = float(input("Ingresa b: \n"))
c = float(input("Ingresa c: \n"))

r1 = (-b+(b**2 - 4 * a * c)**(1/2))/(2*a)
r2 = (-b-(b**2 - 4 * a * c)**(1/2))/(2*a)

print("r1=",r1,"\tr2=",r2)
print(type(a),type(r1))

