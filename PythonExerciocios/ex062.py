num = int(input('Até qual número você quer ver na sequência de Fibonacci? '))

a = 0
b = 1
cont = 0

print('{} -> {} ' .format(a,b) , end='-> ')

while cont <=num:
    cont += 1
    c = a + b

    print('{}'.format(c), end=' -> ')

    a = b
    b = c


print('Fim')
