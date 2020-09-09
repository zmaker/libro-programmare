# media di una lista di voti
lista = []

while input('Hai un voto (s/n)? ') == 's':
    lista.append(input('voto: '))

print(f'Abbiamo {len(lista)} voti.')

somma = 0
for voto in lista:
    somma += float(voto)
media = somma / len(lista)

print(f'Media:{media}.')
