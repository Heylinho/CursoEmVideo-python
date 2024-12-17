produto = float(input('Digite o valor do produto: '))
pagamento = int(input('Digite 1 - Dinhiero/ 2 - Cartão: '))

if pagamento == 1:
    produto = produto * 0.90
    print('Você recebeu um desconto de 10%, agora o seu produto vale R${}'.format(produto))

elif pagamento == 2:
    vezes = int(input('Quantas vezes você quer passar no cartão: '))

    if vezes == 1:
        produto = produto * 0.95
        print('Você recebeu um desconto de 5%, agora o produto vale R${}'.format(produto))

    elif vezes == 2:
        print('Produto passou com valor de R${}'.format(produto))
    
    else:
        produto = produto * 1.20
        print('Recebeu 20% de juros, agora o produto vale R${}'.format(produto))

else:
    print('Valor inválido')