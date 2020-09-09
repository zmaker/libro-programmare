from random import randint

s = randint(1, 10)
t = 0
n = 0

while t < 3:
    n = int(input("che numero?"))
    if s == n:
        print("indovinato!")
        break
    else:
        if s > n:
            print('troppo basso!')
        else:
            print('troppo alto')
        t += 1        
print('fine del gioco')        
