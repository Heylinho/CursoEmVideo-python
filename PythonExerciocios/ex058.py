n1 = int(input('Escreva primeiro número: '))
n2 = int(input('Escreva segundo número: '))

opcao = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
------> '''))

while opcao != 5:
    match opcao:
        case 1:
            soma = n1 + n2
            print('Sua sopma é de {}' .format(soma))
        case 2:
            multiplicar = n1 * n2
            print('Sua multiplicação é de {}' .format(multiplicar))
        case 3:
            if n1 > n2:
                print('O PRIMEIRO número é maior que o SEGUNDO!')
            else:
                print('O SEGUNDO número é maior que o PRIMEIRO!')
        case 4:
            n1 = int(input('Escreva primeiro número: '))
            n2 = int(input('Escreva segundo número: '))
        case _:
            print('Inválido')

    opcao = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
------> '''))
    
print('Fim do código')


