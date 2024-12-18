num = int(input('Escreva um número inteiro: '))
tot = 0
for primo in range(1, num+1):
    if num % primo == 0:
        print('\033[33m{}\033[m' .format(primo))
        tot += 1
    else:
        print('\033[31m{}' .format(primo))

if tot == 2:
    print('Ele é número primo')
else:
    print('Ele não número primo')