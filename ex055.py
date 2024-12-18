cont = 1
soma = 0
mais_velho = 0
homem_velho = ''
qtn_nova = 0
print('-'*10, '{} Pessoa'.format(cont) ,'-'*10)
for pessoas in range (1,5):

    nome = str(input('Qual é o seu nome: '))
    idade = int(input('Qual é a sua idade: '))
    sexo = int(input('[1] Masculino [2] Feminino: '))

    #Contagem de Pessoas
    if cont < 4:
        cont += 1
        print('-'*10, '{} Pessoa' .format(cont),'-'*10)

    #Calculo da média
        soma += idade
        media = soma/4

    #Verificar qual é o HOMEM mais velho
        if sexo == 1:
            if idade > mais_velho:
                mais_velho = idade
                homem_velho = nome

    #Quantas mulheres tem menos de 20 anos
        if sexo == 2:
            if idade < 20:
                qtn_nova += 1


print('A Média da idade do grupo é de "{}"'.format(media))
print('O nome do homem é mais velho é "{}"'.format(homem_velho))
print('Quantas mulheres tem menos que 20 "{}"' .format(qtn_nova))