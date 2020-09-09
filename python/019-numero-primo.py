# verifica se un numero è primo
n = int(input('Che numero? '))

if n == 1:
    print("1 è primo")
elif n > 0:
    d = 2
    while not ((n % d) == 0):
        d += 1
    if d < n:
        print(str(n) + " non è primo")
    else:
        print(str(n) + " è primo")

