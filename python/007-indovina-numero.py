from random import *

segreto = randint(1,10)
risposta = input('che numero ho pensato (da 1 a 10)? ')

if risposta == segreto:
    print('esatto!') 
else:
    print(f'sbagliato era {segreto}')
