frutta = ['mela','pera','banana', 'cocco', 'pesche']

for n in frutta:
    print(n)

#un ciclo sui numeri
for i in range(0,10):
    print(i, end=' ')
print('\n')

#un ciclo su una stringa
for c in "helloworld!":
    print(c , end=' ')
print('\n')

#cicli con range
for i in range(10):
    print(i, end=' ')
print('\n')

for i in range(5, 10):
    print(i, end=' ')
print('\n')

for i in range(0, 10, 2):
    print(i, end=' ')
print('\n')

#for con else
for i in range(0,10):
    print(i, end=' ')
else:
    print('\n')

#uso di break
for i in range(10):
    print(i, end=' ')
    if i == 4:
        break
print('\n')

#uso di continue
for i in range(10):
    if i == 4:
        print(' ', end=' ')
        continue
    print(i, end=' ')
    
print('\n')
