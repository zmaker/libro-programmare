a = input('primo numero:  ')
b = input('secondo numero:  ')
c = input('terzo numero:  ')
a = int(a)
b = int(b)
c = int(c)

if a >= b: 
    #ramo di destra: a e c
    if a >= c: 
        print(a)
    else:
        print(c)
else:
    #ramo di sinistra: b e c
    if b >= c:
        print(b)
    else:
        print(c)
