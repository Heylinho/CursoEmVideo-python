peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc= peso /(altura * altura)

print('seu imc é de {}'.format(imc))

if imc <18.5:
    print('Abaixo do peso')
elif imc <=25:
    print('Peso ideal')
elif imc <=30:
    print('Sobrepeso')
elif imc <=40:
    print('Obesidade')
else:
    print('Thais carla')