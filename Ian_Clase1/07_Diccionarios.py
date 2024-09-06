temperaturas = {"Londres":15,"Oslo":5,"Paris":10}
temperaturas["Mexico"]=23
print(temperaturas)

for ciudad in temperaturas:
    print("La temperatura en",ciudad,"es igual a",temperaturas[ciudad])

# Obtener las llaves de un diccionario
print(temperaturas.keys())
ba=list(temperaturas.keys())

print(ba)

# Obtener los valores de un diccionario
print(temperaturas.values())

