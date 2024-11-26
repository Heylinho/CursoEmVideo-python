dias = float(input('Quantos dias você alugou o carro: '))

dias = dias * 60

km = float(input('Quantos km você andou: '))

km = km * 0.15

total = dias + km

print('O Valor total do alugamento foi de {}' .format(total))