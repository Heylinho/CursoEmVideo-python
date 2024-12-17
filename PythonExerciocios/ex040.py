ano = int(input('Em qual ano você nasceu: '))
idade = 2024 - ano

if idade <= 9:
    print('Nadador Mirim')
elif idade <=14:
    print('Nadador Infantil')
elif idade <=19:
    print('Nadador Junior')
elif idade ==20:
    print('Nadador Senior')
else:
    print('Master')