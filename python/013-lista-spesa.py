# lista della spesa
n = int(input('quanti articoli ti servono? '))

articoli = []
for i in range(n):
    item = input(f'Articolo {i+1}: ')
    articoli.append(item)

print('premi invio per stampare gli articoli')
input()

for x in articoli:
    print(x)
