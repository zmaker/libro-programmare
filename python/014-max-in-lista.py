# trova il massimo in una lista
n = int(input('quanti numeri? '))

lista = []
for i in range(n):
    num = int(input(f'Numero {i+1}: '))
    lista.append(num)

print('premi invio per cercare il massimo')
input()

nmax = 0
for elemento in lista:
    if elemento >= nmax:
        nmax = elemento
print(f'Il max è: {nmax}')
