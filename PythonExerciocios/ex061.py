termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1

while cont <= 10:
    print('O seu termo é de {}'.format(termo))
    termo += razao
    cont += 1

opcao = int(input('Você quer fazer mais quantos termos: '))

while opcao != 0:
    cont = 0
    while cont < opcao:
        print('O seu termo é de {}'.format(termo))
        termo += razao
        cont += 1
    opcao = int(input('Você quer fazer mais quantos termos: '))

print('Fim')
