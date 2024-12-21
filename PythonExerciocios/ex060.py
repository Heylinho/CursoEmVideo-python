termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1

while cont <= 10:
    termo += razao  
    cont += 1

    print('O seu termo é de {}' .format(termo))

print('Fim')
