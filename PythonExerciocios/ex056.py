sexo = input('Digite seu sexo (F ou M): ').strip().upper()

while sexo != 'F' and sexo != 'M':
    sexo = input('Digite seu sexo (F ou M): ').strip().upper()

if sexo == 'F':
    print('Bem vinda!')
else:
    print('Bem vindo!')
