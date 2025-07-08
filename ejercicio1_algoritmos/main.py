# Ejercicio 1 – Algoritmos
numeros = [1, 10, 6, 8, 15, 2]

# 1.a) Mayor sin funciones
mayor = numeros[0]
posicion = 0
for i in range(1, len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i
print(f"Mayor (sin función): {mayor} - Posición: {posicion}")

# 1.b) Mayor con funciones
mayor = max(numeros)
posicion = numeros.index(mayor)
print(f"Mayor (con función): {mayor} - Posición: {posicion}")

# 2.a) Ordenamiento sin funciones (Bubble Sort)
ordenado = numeros.copy()
for i in range(len(ordenado)):
    for j in range(len(ordenado) - 1 - i):
        if ordenado[j] > ordenado[j + 1]:
            ordenado[j], ordenado[j + 1] = ordenado[j + 1], ordenado[j]
print("Ordenado (sin función):", ordenado)

# 2.b) Ordenamiento con función
print("Ordenado (con función):", sorted(numeros))

# 3) Pares y sus posiciones
print("Pares y posiciones:")
for i, num in enumerate(numeros):
    if num % 2 == 0:
        print(f"{num} en posición {i}")

# 4) Arreglo de pares
pares = [num for num in numeros if num % 2 == 0]
print("Arreglo de pares:", pares)
