import random
nome = ['pedra' , 'papel', 'tesoura']
random = random.choice(nome)

escolha = int(input('Digite 1 - pedra / 2 - papel / 3 - tesoura: '))
if escolha == 1:
    print('Você jogou pedra')
elif escolha == 2:
    print('Você pegou papel')
else:
    print('Você tesoura')

print('O computador jogou {}'. format(random))

if random == 'pedra':
    if escolha == 1:
        print('Empatou!')
    elif escolha == 2:
        print('Você ganhou!')
    else:
        print('Você perdeu!')

elif random == 'papel':
    if escolha == 1:
        print('Você perdeu!')
    elif escolha == 2:
        print('Empatou!')
    else:
     print('Você ganhou')

elif random == 'tesoura':
    if escolha == 1:
        print('Você ganhou!')
    elif escolha == 2:
        print('Você perdeu!')
    else:
     print('Empatou')
