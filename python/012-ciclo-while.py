from random import *

#ciclo while
n = 0
while not n == 5:
    n = randint(1,10)
    print(n, end=' ')
print('\n')

#while come un for
i = 0
while i < 5:
  print(i, end=' ')
  i += 1
print('\n')

#break
i = 0
while i < 10:
  if i == 3:
      break
  print(i, end=' ')
  i += 1
print('\n')

#continue
i = 0
while i < 10:
    i += 1
    if i == 5:
        print(' ', end=' ')   
        continue
    print(i, end=' ')
print('\n')

#repeat-until o do-while
i = 0
while True:
    i += 1
    print(i, end=' ')
    if i == 10:
        break

    
