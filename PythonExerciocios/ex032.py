salario = float(input('Escreva seu salário: '))

if salario >= 1250:
    salario = salario * 1.10
    print('Você teve um aumento de 10% R${}'.format(salario))
else:
    salario = salario * 1.15
    print('Você teve um aumento de 15% R${}'.format(salario))
