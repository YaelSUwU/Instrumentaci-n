def sumatoria(x):
    n = len(x)
    sigma = 0
    for i in range(n):
        sigma += x[i]
    return sigma


def generacion(anio):
    if anio <= 1945:
        print("Tradicional")
    elif anio <= 1960:
        print("Baby Boomer")
    elif anio <= 1980:
        print("X")
    elif anio <= 1996:
        print("Milennial")
    else:
        print("Z")

generacion(int(input("Introduce tu año de nacimiento")))


def peri_circulo(rad):
    return 3.141596*(rad**2)

print(peri_circulo(float(input("Introduce un valor de radio"))))
