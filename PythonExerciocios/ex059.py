n1 = int(input('Digite um número e mostrarei o fatorial: '))
inicio = n1
fatorial = 1

while n1 > 1:
    fatorial = fatorial * n1 
    n1 -= 1

print('O Fatorial de {} é de {}'.format(inicio, fatorial))
