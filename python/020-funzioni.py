#definisco una funzione
def hello():
    print('hello')

#la utilizzo
hello()

#funzione con parametri
def hello(name):
    print('hello ', name)

hello('paolo')

#funzione
def somma(a , b):
    n = a + b
    return n

s = somma(10, 20)
print('somma =', s)

#funzioni con più parametri
def supersomma(*addendi):
    print(len(addendi))
    s = 0
    for n in addendi:
        s += n
    return s

s = supersomma(12, 23, 5, 10)
print('supersomma =', s)

#unpack
def unpack(*args):
    a, b, c = args
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

unpack('mela', 'pera', 'ciliegia')
