##chicharronera


#ax^2 + bx + c=0

a=float(input("ingrese a: \n"))
b=float(input("ingrese b: \n"))
c=float(input("ingrese c: \n"))

r1=(-b+(b**2 - (4*a*c))**(1/2))/(2*a)
r2=(-b-(b**2 - (4*a*c))**(1/2))/(2*a)
print("r1=",r1,"\n r2=",r2)