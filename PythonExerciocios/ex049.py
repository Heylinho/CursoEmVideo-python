soma = 0
for cont in range(0,6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
        
print('A soma de todos os números pares são {}'.format(soma))