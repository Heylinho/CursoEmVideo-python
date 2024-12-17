casa = float(input('Valor da Casa: '))
salario = float(input('Seu salario: '))
anos = int(input('Quantos anos de finacimento: '))

prestaçao = casa / (anos * 12)

minimo = salario * 30/100

print('Para pagar uma casa de R${:.2f} em {} anos' .format(casa, anos))
print('a prestação será de R${:.2f}'.format(prestaçao))

if prestaçao <= minimo:
    print('Emprestimo aceito')
else:
    print('Emprestimo NEGADO')

