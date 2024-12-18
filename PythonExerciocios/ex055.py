cont = 1
soma = 0
mais_velho = -1  # Inicializa com valor negativo, para garantir que qualquer idade será maior
homem_velho = ""
qtn_nova = 0

print('-'*10, '{} Pessoa'.format(cont), '-'*10)

for pessoas in range(1, 5):  # Isso vai rodar 4 vezes
    nome = str(input('Qual é o seu nome: '))
    idade = int(input('Qual é a sua idade: '))
    sexo = int(input('[1] Masculino [2] Feminino: '))

    # Contagem de Pessoas
    if cont < 4:
        cont += 1
        print('-'*10, '{} Pessoa'.format(cont), '-'*10)

    # Cálculo da soma das idades
    soma += idade

    # Verificar qual é o homem mais velho
    if sexo == 1:  # Homem
        if idade > mais_velho:
            mais_velho = idade
            homem_velho = nome

    # Contagem de mulheres com menos de 20 anos
    if sexo == 2:  # Mulher
        if idade < 20:
            qtn_nova += 1

# Cálculo da média de idades
media = soma / 4  # Sempre divide pelo número de pessoas inseridas, que no caso é 4

# Exibição dos resultados
print('A média da idade do grupo é de "{}"'.format(media))
print('O nome do homem mais velho é "{}"'.format(homem_velho))
print('Quantas mulheres têm menos de 20 anos? "{}"'.format(qtn_nova))
