viagem = float(input('Quantos KM é sua viagem: '))

if viagem <= 200:
    viagem = viagem * 0.50
    print('O Preço da sua viagem é de R${}'.format(viagem))
else:
    viagem = viagem * 0.45
    print('O Preço da sua viagem é de R${}'.format(viagem))