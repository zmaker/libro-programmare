# pari e dispari - v2
n = int(input('Che numero? '))
s = n

while s > 1:
    s = s - 2
    
if s == 0:
    print('pari')
else:
    print('dispari')
