def isPrimo(n):
    if n == 1:
        #è primo
        return True
    else:
        d = 2
        while not ((n % d) == 0):
            d += 1
        if d < n:
            #non è primo
            return False
        else:
            #è primo
            return True
    
def prossimoPrimo(n):
    while True:
        n += 1
        if isPrimo(n):
            break
    return n

n = int(input('dammi un numero (>0): '))
d = 2
primi = []
r = 0

while not n == 1:
    r = n%d
    if r == 0:
        primi.append(d)
        n = n/d
    else:
        d = prossimoPrimo(d)
print(primi)

