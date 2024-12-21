import random

print('Jogo de Aletorio')

random = random.randint(1,10)
tentativa = int(input('Escreva um número de 1 a 10: '))

while tentativa != random:
    print('Você errou o número aletorio! Tente Denovo')
    tentativa = int(input('Escreva um número de 1 a 10: '))

print('Parabéns você acertou!!!!!!!!')