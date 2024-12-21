soma = 0
n1 = int(input('Digite um número (ou 999 para parar): '))

while n1 != 999:
    soma += n1
    n1 = int(input('Digite um número (ou 999 para parar): '))

print('A soma dos números digitados é: {}' .format(soma))
