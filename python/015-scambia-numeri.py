# scambia due numeri
a = int(input('A? '))
b = int(input('B? '))

print(f'prima:\tA={a} e B={b}')

t = a
a = b
b = t

print(f'dopo:\tA={a} e B={b}')

