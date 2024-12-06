ano = int(input('Qual é seu ano e direi que é bisexo: '))

ano = ano % 4

if ano == 0:
    print('O Ano é bisexo')
else:
    print('Seu ano não bixo')