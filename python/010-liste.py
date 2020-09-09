frutta = ['mela','pera','banana', 'cocco', 'pesche']
print('la lista: ', end=' ')
print(frutta)

#lista vuota
a = []
print(a)

#seleziono e stampo un singolo elemento
print(frutta[0])
print(frutta[1])
print(frutta[2])

#estraggo una parte della lista
lista2 = frutta[1:3]
print('Substringa 1.3: ',lista2)

#stampo il numero di elementi della lista
n = len(frutta)
print(f'la lista contiene {n} frutti')

#modifico un elemento
frutta[1] = 'fragola'
print(frutta)

#aggiungo un elemento
frutta.append('ciliegie')
print(frutta)

#aggiungo alla posizione
frutta.insert(1, 'kiwi')
print(frutta)

#tolgo un elemento
frutta.pop(0)
print(frutta)

#tolgo un elemento per nome
frutta.remove('kiwi')
print(frutta)

#ordino la lista
frutta.sort()
print(frutta)
