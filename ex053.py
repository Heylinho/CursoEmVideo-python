cont = 0
for c in range(0,7):
    ano = int(input('Escreva o ano em que você nasceu: '))
    idade = 2024 - ano

    if idade >= 21:
        cont += 1

print('Apenas {} são maiores de idades!'.format(cont))