nome = str(input('Escreva seu nome completo: ')).strip()

divido = nome.split()

print('Seu nome completo é {}' . format(nome))

print('Primeira palavra do seu nome é {}'.format(divido[0]))

print('Ultima palavra do seu nome é {}'.format(divido[-1]))