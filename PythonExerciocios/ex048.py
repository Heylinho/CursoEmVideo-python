num = int(input('Escreva um numero: '))
cont = 0

for tab in range(0,10):
    cont += 1
    print('Seu número {} x {} = {}' .format(num,cont , num*cont))