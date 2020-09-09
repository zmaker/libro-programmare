lista = [12, 3, 7, 60, 2, 15]

for j in lista:
    for i in range(0, len(lista)-1):
        a = lista[i]
        b = lista[i+1]
        if a > b:
            lista[i] = b
            lista[i+1] = a
        print(lista)
